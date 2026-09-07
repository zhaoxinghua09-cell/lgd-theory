# -*- coding: utf-8 -*-
"""书 v1.1 定稿徽章入书：七字铭文圆徽上 COS + 附录 D 三格式配图。"""
import os, re, zipfile, pathlib, configparser, io
from PIL import Image

KIT = pathlib.Path(r"D:/Workbuddy/08-理论体系/发布/徽章kit")
BOOK = pathlib.Path(r"D:/Workbuddy/08-理论体系/发布/lgd-theory/book")
REPO_BADGE = pathlib.Path(r"D:/Workbuddy/08-理论体系/发布/lgd-theory/badge")
AVATAR = pathlib.Path(r"C:/Users/Administrator/.workbuddy/skills/a3-law-operational/lgd-avatar.png")
COIN_URL = "https://medxpert.cn/badge/lgd-coin.png"
COIN_KEY = "badge/lgd-coin.png"

# ---------- 1) 生成书用圆徽（512 上 COS / 256 内嵌 epub） ----------
img = Image.open(AVATAR)
c512 = img.resize((512, 512), Image.LANCZOS); c256 = img.resize((256, 256), Image.LANCZOS)
buf512 = io.BytesIO(); c512.save(buf512, "PNG", optimize=True)
png512 = buf512.getvalue()
buf256 = io.BytesIO(); c256.save(buf256, "PNG", optimize=True)
png256 = buf256.getvalue()
print("coin 512:", len(png512)//1024, "KB | 256:", len(png256)//1024, "KB")

# ---------- 2) 上传 COS（密钥内存读，不落日志） ----------
cfg = configparser.ConfigParser(); cfg.read(os.path.expanduser("~/.cos.conf")); cfg = cfg["common"]
from qcloud_cos import CosConfig, CosS3Client
client = CosS3Client(CosConfig(Region=cfg["region"], SecretId=cfg["secret_id"], SecretKey=cfg["secret_key"]))
client.put_object(Bucket=cfg["bucket"], Key=COIN_KEY, Body=png512)
print("COS UP", COIN_KEY)

# ---------- 3) 附录 D V2（含定稿徽章图） ----------
META_DIV = """<div class="meta"><span class="tag">LGD</span><span class="dom">全程治理</span>
附录 ｜ TID TH-META-006-C ｜ 源文档 docs/（本章为文库专稿） ｜ DOI 10.5281/zenodo.22456647</div>"""

HEAD_HTML = f"""<p style="text-align:center;margin:14px 0 4px"><img src="{COIN_URL}" alt="LGD 三律之盾定版圆徽（铭文：有籍·有证·有门禁）" width="190"/></p>
<p style="text-align:center;margin:0 0 10px"><span class="meta">定版圆徽：真源币章 + 下弧铭文「有籍 · 有证 · 有门禁」（2026-09-06 定稿）</span></p>
<h1>附录 D · 引用方式与 LGD 徽章体系</h1>"""

D2_HTML = f"""<h2 id="d2">D.2 「三律之盾」参照徽章（LGD-aligned · 声明制）</h2>
<p>参照徽章有三个形态，按场合选用（均为声明制，非认证；须链接回仓库或 DOI）：</p>
<p><strong>① 定版圆徽</strong>——头像、封面、文章首图用（真源币章 + 七字铭文）：</p>
<p style="text-align:center"><img src="{COIN_URL}" alt="LGD 定版圆徽" width="150"/></p>
<pre>![LGD](https://medxpert.cn/badge/lgd-coin.png)</pre>
<p><strong>② 方向横条徽章（v8 定版 · 16 领域 × 中英）</strong>——GitHub README 徽章行用，左侧为真源币章、右侧为领域色条，挂与你领域最近的一枚：</p>
<p><img src="https://medxpert.cn/badge/directions/svg/lgd-aligned-lgd-en.svg" alt="LGD-aligned 全程治理（通用）" width="270"/>　<img src="https://medxpert.cn/badge/directions/svg/lgd-aligned-med-en.svg" alt="LGD-aligned 医疗" width="270"/></p>
<pre>[![LGD-aligned](https://medxpert.cn/badge/directions/svg/lgd-aligned-{{domain}}-en.svg)](https://github.com/zhaoxinghua09-cell/lgd-theory)</pre>
<p>领域代码：<code>lgd</code>（全程治理·通用）/ <code>med</code>（医疗）/ <code>reg</code>（监管）/ <code>fin</code>（金融）/ <code>law</code>（法律）/ <code>gov</code> / <code>gov-ai</code> / <code>dat</code>（数据）/ <code>edu</code>（教育）/ <code>bio</code>（生物）/ <code>crypt</code>（链上）/ <code>aut</code>（自动驾驶）/ <code>rob</code>（机器人）/ <code>ind</code>（工业）/ <code>tool</code>（工具）/ <code>uas</code>（无人机）。线上主 URL：<code>https://medxpert.cn/badge/directions/svg/lgd-aligned-{{domain}}-{{en,cn}}.svg</code>。</p>
<p><strong>③ 盾形横幅（紧凑场景）</strong>：</p>
<pre>[![LGD-aligned](https://medxpert.cn/badge/lgd-shield-color.svg)](https://github.com/zhaoxinghua09-cell/lgd-theory)</pre>
<p>论文 / 文档脚注用：</p>
<p><em>This work is LGD-aligned (Lifecycle Governance Doctrine, DOI: 10.5281/zenodo.22456647). 本文参照《全程治理论》（有籍·有证·有门禁）设计治理。</em></p>"""

def d2_epub(coin):
    return D2_HTML.replace(f'src="{COIN_URL}"', f'src="../images/{coin}"')

# D.2 之外的公共部分（D1/D3/D4/D5/D6 文字与嵌入码，与 V1 相同，仅加展示图）
D3_IMGS_HTML = '<p><img src="https://medxpert.cn/badge/laws/svg/lgd-registered-en.svg" alt="有籍 Registered" width="210"/>　<img src="https://medxpert.cn/badge/laws/svg/lgd-evidenced-en.svg" alt="有证 Evidenced" width="210"/>　<img src="https://medxpert.cn/badge/laws/svg/lgd-gated-en.svg" alt="有门禁 Gated" width="210"/></p>'
D3_IMGS_EPUB = '<p><img src="../images/lgd-registered-en.png" alt="有籍 Registered" width="210"/>　<img src="../images/lgd-evidenced-en.png" alt="有证 Evidenced" width="210"/>　<img src="../images/lgd-gated-en.png" alt="有门禁 Gated" width="210"/></p>'
D4_IMG_HTML = '<p><img src="https://medxpert.cn/badge/powered/svg/lgd-powered-en.svg" alt="LGD-Powered" width="230"/></p>'
D4_IMG_EPUB = '<p><img src="../images/lgd-powered-en.png" alt="LGD-Powered" width="230"/></p>'

BODY_REST = """<p>徽章是 LGD 的视觉协议层：把「有籍·有证·有门禁」外化为可挂载、可核查、分级的身份标识——<strong>参照挂盾、进度挂律、工具挂 Powered、认证有指纹</strong>。本章给出引用格式与四族徽章的取用方式。</p>
<h2 id="d1">D.1 引用格式（概念 DOI，自动指向最新版）</h2>
<p><strong>APA 7</strong><br>Zhao, X. (2026). <em>Lifecycle Governance Doctrine: Every self-governing entity shall carry a registry, evidence, and evolution gates</em> (Version 1.1). Zenodo. https://doi.org/10.5281/zenodo.22456647</p>
<p><strong>GB/T 7714</strong><br>赵兴华. 全程治理论：凡自治之物必有籍、有证、有门禁[EB/OL]. (2026-09-06). https://doi.org/10.5281/zenodo.22456647.</p>
<p><strong>BibTeX</strong></p>
<pre>@misc{zhao2026lgd,
  author       = {Zhao, Xinghua},
  title        = {Lifecycle Governance Doctrine},
  year         = {2026},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.22456647},
  url          = {https://github.com/zhaoxinghua09-cell/lgd-theory}
}</pre>"""

D3_REST = """<h2 id="d3">D.3 三律徽章族（Laws Badges · 进度徽章）</h2>
<p>三律各有一枚进度徽章，标记你的自治系统走到了哪一步——<strong>做到哪步，挂哪枚</strong>：</p>
<ul>
<li><strong>有籍 Registered</strong>：完成登记（凡造必登）——系统 / 算法已在册，可标识、可追溯；</li>
<li><strong>有证 Evidenced</strong>：证据链在位（凡所行必有证据）——关键行为与决策可溯源、可核查；</li>
<li><strong>有门禁 Gated</strong>：门禁评审通过（凡演化必经门禁）——重大变更须经评审方可部署。</li>
</ul>
<p>三枚全挂，即达 LGD-aligned；此时宜并挂 D.2 参照徽章作为总体声明。嵌入示例（GitHub README）：</p>
<pre>[![LGD Registered 有籍](https://medxpert.cn/badge/laws/svg/lgd-registered-en.svg)](https://github.com/zhaoxinghua09-cell/lgd-theory)
[![LGD Evidenced 有证](https://medxpert.cn/badge/laws/svg/lgd-evidenced-en.svg)](https://github.com/zhaoxinghua09-cell/lgd-theory)
[![LGD Gated 有门禁](https://medxpert.cn/badge/laws/svg/lgd-gated-en.svg)](https://github.com/zhaoxinghua09-cell/lgd-theory)</pre>
<p>线上主 URL：<code>https://medxpert.cn/badge/laws/svg/lgd-{{registered,evidenced,gated}}-{{en,cn}}.svg</code>（PNG 同路径换扩展名；中英双语可选）。</p>
<h2 id="d4">D.4 LGD-Powered 工具徽章</h2>
<p>凡以 LGD 工具链构建的工具与产品，按《徽章章程》<strong>必须挂载</strong> LGD-Powered 徽章，声明其治理能力来自 LGD 工具链：</p>
{D4IMG}
<pre>[![LGD-Powered](https://medxpert.cn/badge/powered/svg/lgd-powered-en.svg)](https://github.com/zhaoxinghua09-cell/lgd-theory)</pre>
<p>线上主 URL：<code>https://medxpert.cn/badge/powered/svg/lgd-powered-{{en,cn}}.svg</code>（PNG 同路径换扩展名）。</p>
<h2 id="d5">D.5 从声明到认证：lgd-certify</h2>
<p>D.2–D.4 是<strong>声明制</strong>（自声明 + 回链，零门槛）；需要可验证的治理证明时，走 <strong>lgd-certify 认证线</strong>——三个命令走完三律：</p>
<ul>
<li><code>register</code>（有籍）：为算法生成「护照」——身份锚、性能锚、行为锚三锚同源，附验证票据；</li>
<li><code>evidence</code>（有证）：扫描六类证据（身份 / 数据 / 验证 / 行为边界 / 变更 / 签发），逐件哈希成链式证据链，任何一块被篡改整链即断；</li>
<li><code>gate</code>（有门禁）：三律检查全过即签发 <code>certification.json</code>（含认证指纹 cert_hash），并自动生成徽章嵌入码 <code>BADGES.md</code>。</li>
</ul>
<p>认证通过的产物可挂 D.3 三律徽章 + D.4 LGD-Powered，并在徽章注释中附认证指纹——让「我有治理」从一句话变成一个可核验的哈希。</p>
<h2 id="d6">D.6 理论文库在线源</h2>
<ul>
<li>仓库：https://github.com/zhaoxinghua09-cell/lgd-theory</li>
<li>DOI：https://doi.org/10.5281/zenodo.22456647</li>
<li>Hugging Face 镜像：https://huggingface.co/datasets/zhaoxinghua09/lgd-theory</li>
</ul>
<p class="meta" style="margin-top:26px">来源：https://github.com/zhaoxinghua09-cell/lgd-theory ｜ CC BY 4.0 ｜ 署名 赵兴华 / Steven Zhao·China（ORCID 0009-0001-0512-1237）</p>"""

D3_AFTER = """<p>三枚全挂，即达 LGD-aligned；此时宜并挂 D.2 参照徽章作为总体声明。嵌入示例（GitHub README）：</p>"""

def build_section(coin_fname, d3_imgs, d4_img):
    d2 = d2_epub(coin_fname) if coin_fname.startswith("images/") else D2_HTML
    head = HEAD_HTML if not coin_fname.startswith("images/") else HEAD_HTML.replace(f'src="{COIN_URL}"', f'src="../images/{coin_fname}"')
    d3pos = D3_REST.find(D3_AFTER)
    d3 = D3_REST[:d3pos] + d3_imgs + "\n" + D3_REST[d3pos:]
    d3 = d3.replace("{D4IMG}", d4_img)
    return ('<section class="chapter" id="ch18">\n' + META_DIV + "\n" + head + "\n"
            + BODY_REST + "\n" + d2 + "\n" + d3 + "\n</section>")

SEC_HTML = build_section(COIN_URL, D3_IMGS_HTML, D4_IMG_HTML)
SEC_EPUB_BODY = build_section("images/lgd-coin.png", D3_IMGS_EPUB, D4_IMG_EPUB)

def patch_html(src, out):
    t = (BOOK / src).read_text(encoding="utf-8")
    m = re.search(r'<section class="chapter" id="ch18"[^>]*>', t)
    assert m, "ch18 section 未找到"
    k = m.start()
    e = t.find("</section>", m.end()); assert e != -1
    t = t[:k] + SEC_HTML + t[e + len("</section>"):]
    (BOOK / out).write_text(t, encoding="utf-8")
    print(f"[ok] {out}: {len(t)} chars")

patch_html("LGD-Library-v1.1.html", "LGD-Library-v1.1.html")
patch_html("LGD-Library-v1.1-print.html", "LGD-Library-v1.1-print.html")

# ---------- 4) epub 重打包（内嵌 8 png） ----------
EPUB_IMGS = {
    "lgd-coin.png": png256,
    "lgd-aligned-lgd-en.png": (KIT / "directions/png/lgd-aligned-lgd-en.png").read_bytes(),
    "lgd-aligned-med-en.png": (KIT / "directions/png/lgd-aligned-med-en.png").read_bytes(),
    "lgd-registered-en.png": (KIT / "laws/png/lgd-registered-en.png").read_bytes(),
    "lgd-evidenced-en.png": (KIT / "laws/png/lgd-evidenced-en.png").read_bytes(),
    "lgd-gated-en.png": (KIT / "laws/png/lgd-gated-en.png").read_bytes(),
    "lgd-powered-en.png": (KIT / "powered/png/lgd-powered-en.png").read_bytes(),
}
EPUB_IMGS["lgd-coin.png"] = png256

zin = zipfile.ZipFile(BOOK / "LGD-Library-v1.0.epub")  # 从完好的 v1.0 重建（读写同路径会自毁）
x = zin.read("OEBPS/text/ch18.xhtml").decode("utf-8")
m = re.search(r"<body>(.*)</body>", x, re.S)
body_new = SEC_EPUB_BODY
body_new = re.sub(r"^<section[^>]*>\n?", "", body_new).replace("\n</section>$", "").rstrip()
if body_new.endswith("</section>"): body_new = body_new[:-len("</section>")].rstrip()
new_x = x[:m.start(1)] + "\n" + body_new + "\n" + x[m.end(1):]
new_x = new_x.replace("附录 D · 引用方式与 LGD 参照徽章", "附录 D · 引用方式与 LGD 徽章体系")
opf = zin.read("OEBPS/content.opf").decode("utf-8").replace("理论文库 v1.0", "理论文库 v1.1")
toc = zin.read("OEBPS/text/toc.xhtml").decode("utf-8").replace("附录 D · 引用方式与 LGD 参照徽章", "附录 D · 引用方式与 LGD 徽章体系")
img_items = "".join(f'<item id="bimg{i}" href="images/{n}" media-type="image/png"/>'
                    for i, n in enumerate(EPUB_IMGS))
opf = opf.replace("</manifest>", img_items + "</manifest>")
TMP = BOOK / "_tmp_v11.epub"
with zipfile.ZipFile(TMP, "w") as zout:
    zout.writestr(zipfile.ZipInfo("mimetype"), zin.read("mimetype"), zipfile.ZIP_STORED)
    for item in zin.infolist():
        if item.filename == "mimetype":
            continue
        data = zin.read(item.filename)
        if item.filename == "OEBPS/text/ch18.xhtml":
            data = new_x.encode("utf-8")
        elif item.filename == "OEBPS/content.opf":
            data = opf.encode("utf-8")
        elif item.filename == "OEBPS/text/toc.xhtml":
            data = toc.encode("utf-8")
        zout.writestr(item, data, zipfile.ZIP_DEFLATED)
    for n, b in EPUB_IMGS.items():
        zout.writestr(f"OEBPS/images/{n}", b, zipfile.ZIP_DEFLATED)
zin.close()
TMP.replace(BOOK / "LGD-Library-v1.1.epub")
print("[ok] epub:", (BOOK / "LGD-Library-v1.1.epub").stat().st_size, "bytes,", len(EPUB_IMGS), "images embedded")

# ---------- 5) 定稿圆徽同步进仓库 badge/（待下次推送带上） ----------
(REPO_BADGE / "lgd-coin.png").write_bytes(png512)
print("[ok] repo badge/lgd-coin.png saved")
print("DONE")
