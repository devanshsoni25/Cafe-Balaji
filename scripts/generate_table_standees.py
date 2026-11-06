import os
import qrcode
import qrcode.image.svg
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = os.path.abspath('public/qr-codes')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Café Wi-Fi IP URL (points directly to the menu)
BASE_URL = "http://192.168.1.107:5173"

# Colors matching the warm design system
COLOR_BG = (250, 246, 239)        # Warm cream #FAF6EF
COLOR_CARD = (255, 255, 255)      # White
COLOR_DARK = (44, 26, 14)         # Dark Brown #2C1A0E
COLOR_TOMATO = (192, 57, 43)      # Tomato Red #C0392B
COLOR_SAFFRON = (230, 126, 34)    # Saffron #E67E22
COLOR_GREEN = (46, 125, 50)       # Veg Green #2E7D32
COLOR_BORDER = (234, 219, 206)    # Border #EADBCE

FONT_HELVETICA = "/System/Library/Fonts/Helvetica.ttc"
FONT_ARIAL = "/System/Library/Fonts/Supplemental/Arial.ttf"

def get_font(size, bold=False):
    try:
        if bold and os.path.exists(FONT_ARIAL):
            return ImageFont.truetype(FONT_ARIAL, size)
        elif os.path.exists(FONT_HELVETICA):
            return ImageFont.truetype(FONT_HELVETICA, size)
    except:
        pass
    return ImageFont.load_default()

def generate_svg_qr(url, filepath):
    factory = qrcode.image.svg.SvgPathImage
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2,
        image_factory=factory
    )
    qr.add_data(url)
    qr.make(fit=True)
    svg_img = qr.make_image(fill_color="#2C1A0E")
    svg_img.save(filepath)

# ── 1. Universal Table Standee (4" x 6" 300 DPI: 1200 x 1800 px) ──────────────
def create_universal_standee():
    width, height = 1200, 1800
    img = Image.new("RGB", (width, height), COLOR_BG)
    draw = ImageDraw.Draw(img)

    # Outer Decorative Borders
    draw.rectangle([30, 30, width - 30, height - 30], outline=COLOR_TOMATO, width=6)
    draw.rectangle([45, 45, width - 45, height - 45], outline=COLOR_SAFFRON, width=3)
    draw.rectangle([60, 60, width - 60, height - 60], outline=COLOR_BORDER, width=2)

    # Inner White Card
    card_margin_x = 90
    card_top = 100
    card_bottom = height - 100
    draw.rounded_rectangle(
        [card_margin_x, card_top, width - card_margin_x, card_bottom],
        radius=30,
        fill=COLOR_CARD,
        outline=COLOR_BORDER,
        width=3
    )

    # Top Gradient Line
    for i in range(12):
        t = i / 12.0
        r = int(COLOR_TOMATO[0] * (1 - t) + COLOR_SAFFRON[0] * t)
        g = int(COLOR_TOMATO[1] * (1 - t) + COLOR_SAFFRON[1] * t)
        b = int(COLOR_TOMATO[2] * (1 - t) + COLOR_SAFFRON[2] * t)
        draw.line([card_margin_x + 3, card_top + 3 + i, width - card_margin_x - 3, card_top + 3 + i], fill=(r, g, b))

    # Header Veg Badge
    font_badge = get_font(32, bold=True)
    veg_text = "● 100% PURE VEG"
    draw.rounded_rectangle([width // 2 - 190, card_top + 50, width // 2 + 190, card_top + 105], radius=15, fill=(232, 245, 233), outline=COLOR_GREEN, width=2)
    draw.text((width // 2, card_top + 77), veg_text, fill=COLOR_GREEN, font=font_badge, anchor="mm")

    # Café Title
    font_title1 = get_font(68, bold=True)
    font_title2 = get_font(52, bold=True)
    draw.text((width // 2, card_top + 175), "SHREE BALAJI", fill=COLOR_DARK, font=font_title1, anchor="mm")
    draw.text((width // 2, card_top + 245), "SNACKS & FOOD ZONE", fill=COLOR_DARK, font=font_title2, anchor="mm")

    # Tagline
    font_tagline = get_font(38, bold=True)
    draw.text((width // 2, card_top + 310), '"Tasty Food... Happy Mood..."', fill=COLOR_TOMATO, font=font_tagline, anchor="mm")

    # Divider
    draw.line([card_margin_x + 60, card_top + 355, width - card_margin_x - 60, card_top + 355], fill=COLOR_BORDER, width=3)

    # Call To Action Pill
    font_cta = get_font(42, bold=True)
    draw.rounded_rectangle([width // 2 - 240, card_top + 380, width // 2 + 240, card_top + 450], radius=20, fill=COLOR_TOMATO)
    draw.text((width // 2, card_top + 415), "SCAN FOR DIGITAL MENU", fill=(255, 255, 255), font=font_cta, anchor="mm")

    # Generate High-Res QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=18,
        border=2,
    )
    qr.add_data(BASE_URL)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color=COLOR_DARK, back_color=COLOR_CARD).convert("RGB")
    
    qr_size = 640
    qr_img = qr_img.resize((qr_size, qr_size), Image.Resampling.LANCZOS)
    qr_x = (width - qr_size) // 2
    qr_y = card_top + 485

    draw.rectangle([qr_x - 10, qr_y - 10, qr_x + qr_size + 10, qr_y + qr_size + 10], outline=COLOR_BORDER, width=4)
    img.paste(qr_img, (qr_x, qr_y))

    # Instructions Below QR
    scan_y = qr_y + qr_size + 50
    font_instruction = get_font(40, bold=True)
    font_sub = get_font(28, bold=False)
    
    draw.text((width // 2, scan_y), "POINT CAMERA TO VIEW MENU", fill=COLOR_DARK, font=font_instruction, anchor="mm")
    draw.text((width // 2, scan_y + 45), "No App Needed • Works On Any Phone", fill=(110, 91, 79), font=font_sub, anchor="mm")

    # Bottom Instructions Box
    box_y = scan_y + 100
    box_h = 160
    draw.rounded_rectangle(
        [card_margin_x + 40, box_y, width - card_margin_x - 40, box_y + box_h],
        radius=20,
        fill=COLOR_BG,
        outline=COLOR_BORDER,
        width=2
    )

    font_box_title = get_font(32, bold=True)
    font_box_desc = get_font(26, bold=False)
    draw.text((width // 2, box_y + 42), "⚡ Fast & Contactless Dining Experience", fill=COLOR_TOMATO, font=font_box_title, anchor="mm")
    draw.text((width // 2, box_y + 88), "1. Open camera & scan QR  •  2. Browse 66 dishes", fill=COLOR_DARK, font=font_box_desc, anchor="mm")
    draw.text((width // 2, box_y + 124), "3. Order at counter with your dish names", fill=COLOR_DARK, font=font_box_desc, anchor="mm")

    out_path = os.path.join(OUTPUT_DIR, "table_standee.png")
    img.save(out_path, quality=95, dpi=(300, 300))
    print(f"Generated universal standee: table_standee.png ({os.path.getsize(out_path)} bytes)")

# ── 2. Universal Table Sticker (Square 800 x 800 px) ─────────────────────────
def create_table_sticker():
    size = 800
    img = Image.new("RGB", (size, size), COLOR_CARD)
    draw = ImageDraw.Draw(img)

    # Rounded outer border
    draw.rounded_rectangle([15, 15, size - 15, size - 15], radius=24, outline=COLOR_TOMATO, width=6)
    draw.rounded_rectangle([25, 25, size - 25, size - 25], radius=18, outline=COLOR_SAFFRON, width=3)

    # Title
    font_t = get_font(38, bold=True)
    font_sub = get_font(24, bold=True)
    draw.text((size // 2, 60), "SHREE BALAJI", fill=COLOR_DARK, font=font_t, anchor="mm")
    draw.text((size // 2, 95), "SCAN FOR MENU", fill=COLOR_TOMATO, font=font_sub, anchor="mm")

    # QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=15,
        border=1,
    )
    qr.add_data(BASE_URL)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color=COLOR_DARK, back_color=COLOR_CARD).convert("RGB")
    qr_size = 520
    qr_img = qr_img.resize((qr_size, qr_size), Image.Resampling.LANCZOS)
    img.paste(qr_img, ((size - qr_size) // 2, 125))

    # Bottom
    font_b = get_font(26, bold=True)
    draw.text((size // 2, 680), "● 100% PURE VEG", fill=COLOR_GREEN, font=font_b, anchor="mm")
    font_tag = get_font(22, bold=False)
    draw.text((size // 2, 720), "Tasty Food... Happy Mood...", fill=COLOR_DARK, font=font_tag, anchor="mm")

    out_path = os.path.join(OUTPUT_DIR, "table_sticker.png")
    img.save(out_path, quality=95)
    print(f"Generated table sticker: table_sticker.png ({os.path.getsize(out_path)} bytes)")

# ── 3. Standalone Pure QR Codes ───────────────────────────────────────────────
qr_raw = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,
    border=2,
)
qr_raw.add_data(BASE_URL)
qr_raw.make(fit=True)
qr_png = qr_raw.make_image(fill_color=COLOR_DARK, back_color=(255, 255, 255)).convert("RGB")
qr_png.save(os.path.join(OUTPUT_DIR, "menu_qr.png"))

generate_svg_qr(BASE_URL, os.path.join(OUTPUT_DIR, "menu_qr.svg"))

create_universal_standee()
create_table_sticker()

print("\nSingle universal QR codes successfully generated!")
