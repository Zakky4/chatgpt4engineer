from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# 日本語フォントを登録
font_path = os.path.join('/mnt/data/fonts', 'BIZUDGothic-Regular.ttf')
pdfmetrics.registerFont(TTFont('BIZUDGothic', font_path))

def create_pdf_with_text_japanese_small(text, file_name):
    c = canvas.Canvas(file_name, pagesize=A4)
    width, height = A4
    c.setFont("BIZUDGothic", 18)  # フォントサイズを18ptに変更
    text_width = c.stringWidth(text, "BIZUDGothic", 18)
    text_x = (width - text_width) / 2
    text_y = height / 2 - 30  # 中央揃えのための位置調整
    c.drawString(text_x, text_y, text)
    c.showPage()
    c.save()

# PDFに追加するテキスト
texts = [
    "株式会社にゃんこ ご一行さま",
    "わんこ株式会社 ご一行さま",
    "わんことにゃんこの同好会 ご一行さま"
]

# PDFを保存するディレクトリ
pdf_dir_japanese = "/mnt/data/pdfs_japanese"
os.makedirs(pdf_dir_japanese, exist_ok=True)

# 日本語フォントを使用してPDFを作成（フォントサイズ18pt）
for i, text in enumerate(texts, start=1):
    file_name_japanese_small = f"{pdf_dir_japanese}/text_{i}_japanese_small.pdf"
    create_pdf_with_text_japanese_small(text, file_name_japanese_small)
