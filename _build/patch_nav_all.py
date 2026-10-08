#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
全站导航统一 + 清理编辑器注入属性（君子兰.cn）
用法： python _build/patch_nav_all.py
"""
import os
import re
import glob

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)

NAV = [
    ("品种图鉴", "/pinzhong/"),
    ("栽培养护", "/yanghu/"),
    ("文章总览", "/articles/"),
    ("市场行情", "/shichang/"),
    ("展会活动", "/zhanhui/"),
    ("君子兰文化", "/wenhua/"),
    ("花友交流", "/huayou/"),
    ("关于", "/about/"),
]

DIR2NAV = {"pinzhong": "品种图鉴", "yanghu": "栽培养护", "articles": "文章总览",
           "shichang": "市场行情", "zhanhui": "展会活动", "wenhua": "君子兰文化",
           "huayou": "花友交流", "about": "关于"}


def page_files():
    out = sorted(glob.glob(os.path.join(SITE, "**", "*.html"), recursive=True))
    return [p for p in out if "/_build/" not in p.replace("\\", "/")]


def nav_block(path):
    rel = os.path.relpath(path, SITE).replace("\\", "/")
    segs = rel.split("/")[:-1]
    depth = len(segs)
    prefix = "../" * depth if depth else "./"

    active = ""
    if segs:
        active = DIR2NAV.get(segs[0], "")

    links = ""
    for name, url in NAV:
        cls = ' class="active"' if name == active else ""
        links += '\n        <a href="%s%s"%s>%s</a>' % (prefix, url.lstrip("/"), cls, name)
    return ('<nav class="main-nav">%s\n      </nav>' % links)


def main():
    changed = 0
    for path in page_files():
        with open(path, encoding="utf-8") as f:
            src = f.read()
        orig = src
        src = re.sub(r'\s+data-page-node-id="[^"]*"', "", src)
        src, n = re.subn(r'<nav class="main-nav"[^>]*>.*?</nav>', nav_block(path), src, flags=re.S)
        if n == 0:
            print("  [跳过] 无导航: %s" % os.path.relpath(path, SITE))
        if src != orig:
            with open(path, "w", encoding="utf-8") as f:
                f.write(src)
            changed += 1
    print("处理页面 %d 个，更新 %d 个" % (len(page_files()), changed))


if __name__ == "__main__":
    main()