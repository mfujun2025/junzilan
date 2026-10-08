#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成君子兰.cn 的 6 个栏目 hub 页 + 关于页"""
import os, html as _h

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
DOMAIN = "https://xn--95qv8dfxj.cn"

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

def esc(s): return _h.escape(s, quote=False)

def header_nav(active):
    items = ""
    for n, u in NAV:
        cls = ' class="active"' if n == active else ""
        p = "../" if active else ""
        items += '\n        <a href="%s%s"%s>%s</a>' % (p, u.lstrip("/"), cls, n)
    return """  <header class="site-header">
    <div class="container">
      <a href="%s" class="logo">君子兰<span>.cn</span></a>
      <nav class="main-nav">%s
      </nav>
    </div>
  </header>""" % ("../" if active else "./", items)

FOOTER = """  <footer class="site-footer">
    <div class="container">
      <p class="disclaimer"><strong>免责声明：</strong>本站内容为君子兰养护经验与公开信息整理，非专业种植指导。植物生长受地域气候、品种个体差异影响，具体操作请结合本地实际情况并参考专业意见。市场价格信息仅供了解行情参考，不构成交易建议。本站不参与兰花交易、不收取商家费用。</p>
      <p class="copyright">© 2026 君子兰.cn · 君子兰资讯聚合 · <a href="%s">关于与联系</a></p>
    </div>
  </footer>"""

HUBS = {
    "pinzhong": {
        "title": "品种图鉴 | 君子兰.cn",
        "desc": "君子兰品种图鉴：大胜利、和尚、短叶、彩兰等经典名品的特征识别与鉴赏标准。",
        "h1": "品种图鉴",
        "intro": "君子兰品种繁多，从传统的大胜利、和尚到圆头、短叶，再到叶艺万千的彩兰，每个品种都有独特的叶形、脉纹和花型特征。本栏目系统梳理君子兰经典名品的识别要点、品评标准与育种谱系，帮助花友从「看热闹」走向「看门道」。",
        "sections": [
            ("品种识别基础", "认识品种是养兰的第一步。从叶片长度、宽度、厚度到脉纹的凸起程度、花型花色，每个维度都是区别品种的依据。"),
            ("经典名品系列", "大胜利、和尚、圆头、短叶——这些耳熟能详的名字背后，是数十年育种者的心血传承。"),
            ("彩兰叶艺体系", "金丝、覆轮、缟艺……彩兰以叶面条纹色块为美，分类体系自成一套。"),
        ],
    },
    "yanghu": {
        "title": "栽培养护 | 君子兰.cn",
        "desc": "君子兰栽培养护知识：配土、浇水、施肥、光照、促花、病虫害防治与分株繁殖全攻略。",
        "h1": "栽培养护",
        "intro": "养护是君子兰的核心功夫。从配土配方到浇水节奏，从施肥时机到促花技术，每一步都直接影响植株状态和开花品质。本栏目汇集配土、浇水、施肥、光照、促花、病虫害、分株七大方向的实操经验，给方法给步骤，不教条不僵化。",
        "sections": [
            ("配土与翻盆", "土壤是根基——松针土、腐叶土配方比例与翻盆换土时机全解。"),
            ("水肥光温管理", "四季浇水频率调整、薄肥勤施原则、光照需求与摆放位置选择。"),
            ("促花与繁殖", "低温春化促花技术、花箭夹箭处理、分株繁殖操作步骤指南。"),
        ],
    },
    "shichang": {
        "title": "市场行情 | 君子兰.cn",
        "desc": "君子兰市场行情动态：价格形成机制、交易渠道对比、收藏投资品相评判与市场周期观察。",
        "h1": "市场行情",
        "intro": "君子兰市场的魅力与风险并存。从 80 年代的「天价神话」到近年理性回归，品种、品相、血统是价格的核心变量。本栏目不讲具体价格、不给交易建议，只给估值逻辑、渠道对比、品评标准和趋势观察方法，帮你在信息充分的前提下做判断。",
        "sections": [
            ("价格与估值", "君子兰定价因素解析与行情查询渠道。"),
            ("交易与收藏", "花市、拍卖、线上平台对比，收藏级品种品相怎么看。"),
            ("市场周期", "从天价到理性，君子兰市场的历史脉络与趋势。"),
        ],
    },
    "zhanhui": {
        "title": "展会活动 | 君子兰.cn",
        "desc": "君子兰展会活动资讯：全国君子兰博览会、地方花展、评奖标准、参展攻略与花友组织参与方式。",
        "h1": "展会活动",
        "intro": "展会是君子兰界的盛事，也是花友交流学习的最佳场合。本栏目梳理君子兰展会的参赛报名流程、评审标准、参展攻略，以及花友会和地方俱乐部的参与方式——帮你从看展者变成参展者。",
        "sections": [
            ("展会资讯", "全国君子兰博览会概况与地方展会信息。"),
            ("参赛与评审", "报名条件、送展流程、评审标准和评奖规则。"),
            ("花友组织", "花友会、俱乐部和协会的参与方式。"),
        ],
    },
    "wenhua": {
        "title": "君子兰文化 | 君子兰.cn",
        "desc": "君子兰文化意象：花中君子的品格溯源、命名典故、书画艺术传统与家居美学摆放讲究。",
        "h1": "君子兰文化",
        "intro": "君子兰不只是一盆花，更是一种文化意象。「君子」二字承载着端庄、谦逊、坚韧的品格期许，从命名典故到书画传统，从诗词意境到家居美学，本栏目带你读懂花中君子的文化底蕴。",
        "sections": [
            ("君子意象", "君子兰与君子文化的精神关联与品格象征。"),
            ("命名与典故", "学名来源、中文命名故事与文化内涵。"),
            ("艺术与美学", "书画中的君子兰、家居摆放讲究与空间美学。"),
        ],
    },
    "huayou": {
        "title": "花友交流 | 君子兰.cn",
        "desc": "君子兰花友交流分享：新手常见错误、叶片品评标准、多年养护经验心得与叶面保养打理技巧。",
        "h1": "花友交流",
        "intro": "来自花友一线的真实经验比书本知识更鲜活。本栏目汇集新手避坑指南、养功品评交流、多年老花友心得精华与叶面保养日常——踩过的弯路你不必再走，悟出的道理你可以直接用。",
        "sections": [
            ("新手避坑", "五个最常见的新手错误与正确做法。"),
            ("养功品评", "叶片短宽厚标准怎么看——花友之间的品评交流。"),
            ("经验心得", "多年花友的养护哲学与叶面打理手法。"),
        ],
    },
}

def gen_hub(slug):
    h = HUBS[slug]
    depth = 1
    canon = DOMAIN + "/" + slug + "/"
    sections = ""
    for title, desc in h["sections"]:
        sections += '\n        <div class="feature-card"><h3>%s</h3><p>%s</p></div>' % (esc(title), esc(desc))

    html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>%s</title>
  <meta name="description" content="%s">
  <link rel="canonical" href="%s">
  <script type="application/ld+json">{"@context":"https://schema.org","@type":"CollectionPage","name":"%s","description":"%s","url":"%s","inLanguage":"zh-CN"}</script>
  <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>
%s

  <main class="sub-page">
    <div class="container">
      <h1>%s</h1>
      <p class="subtitle">%s</p>
      <div class="hub-intro">
        <div class="feature-grid">%s
        </div>
      </div>
    </div>
  </main>

%s
</body>
</html>""" % (
        esc(h["title"]), esc(h["desc"]), canon,
        esc(h["h1"]), esc(h["desc"]), canon,
        header_nav(h["h1"]),
        esc(h["h1"]), esc(h["intro"]),
        sections,
        FOOTER % "../about/"
    )
    out_dir = os.path.join(SITE, slug)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("  生成: %s/index.html" % slug)


def gen_about():
    depth = 1
    canon = DOMAIN + "/about/"
    html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>关于君子兰.cn | 君子兰.cn</title>
  <meta name="description" content="君子兰.cn 是专注君子兰的资讯网站，提供品种图鉴、栽培养护、市场行情、展会活动与文化鉴赏等内容。">
  <link rel="canonical" href="%s">
  <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>
%s

  <main class="sub-page">
    <div class="container">
      <h1>关于君子兰.cn</h1>
      <p class="subtitle">专注君子兰品种、养护、市场、展会与文化的资讯平台。</p>
      <div class="about-body">
        <p>君子兰.cn 是一个以君子兰为主题的资讯网站，旨在为广大君子兰爱好者、养植者和收藏者提供系统、实用的信息参考。内容覆盖品种图鉴、栽培养护、市场行情、展会活动、君子兰文化与花友交流六大板块。</p>
        <h2>站定位</h2>
        <p>本站只做信息整理与经验分享，不参与兰花交易、不收取商家费用、不推荐具体品牌。养护方法给操作步骤和配比范围，市场价格信息仅供了解行情，不构成交易建议。</p>
        <h2>内容来源</h2>
        <p>文章内容由养兰经验整理和公开资料梳理而成。植物生长受地域气候、品种个体差异影响，具体操作请结合本地实际情况并参考专业意见。</p>
        <h2>联系方式</h2>
        <p>如需联系站长或有内容建议，请发邮件至 mfujun@agent.qq.com。</p>
      </div>
    </div>
  </main>

%s
</body>
</html>""" % (canon, header_nav("关于"), FOOTER % "./")
    out_dir = os.path.join(SITE, "about")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("  生成: about/index.html")


if __name__ == "__main__":
    for slug in HUBS:
        gen_hub(slug)
    gen_about()
    print("hub 页生成完毕")