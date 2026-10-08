# 君子兰.cn（xn--95qv8dfxj.cn）

君子兰资讯站 — 品种图鉴、栽培养护、市场行情、展会活动、君子兰文化、花友交流。

## 站点结构

| 目录 | 说明 |
|---|---|
| `index.html` | 首页 |
| `pinzhong/` | 品种图鉴栏目 |
| `yanghu/` | 栽培养护栏目 |
| `shichang/` | 市场行情栏目 |
| `zhanhui/` | 展会活动栏目 |
| `wenhua/` | 君子兰文化栏目 |
| `huayou/` | 花友交流栏目 |
| `about/` | 关于页 |
| `articles/` | 文章总目录 + 各文章页 |
| `assets/css/` | 样式表 |
| `_build/` | 构建工具与文章源文件 |

## 构建管线

```bash
cd junzilan-cn
python _build/gen_hubs.py        # 生成栏目 hub 页
python _build/build_articles.py  # 构建：md → 文章页 + 目录 + sitemap/robots/404 + hub 注入
python _build/patch_nav_all.py   # 统一导航 + 清理注入属性
python _build/inline_css.py      # 内联样式表
python _build/check_site.py      # 静态自检
```

## 加文章

1. 在 `_build/_content/` 新建 `<slug>.md` 文件
2. 编写 frontmatter + markdown 正文
3. 重新运行构建管线
4. 提交推送

## 内容红线

- 不写死具体价格数字，给查询渠道和判断方法
- 不推荐具体商家/店铺
- 养护方法给操作步骤，但强调"因品种和气候调整"
- 每页保留免责声明

## 域名

- 中文域名：君子兰.cn
- Punycode：xn--95qv8dfxj.cn
- canonical / sitemap / CNAME 一律用 punycode
- GitHub Pages 部署

## 技术栈

- 纯静态 HTML + 内联 CSS
- Python 标准库构建脚本（无依赖）
- JSON-LD 结构化数据（Article + BreadcrumbList + FAQPage）
- 自适应布局（桌面 + 移动）