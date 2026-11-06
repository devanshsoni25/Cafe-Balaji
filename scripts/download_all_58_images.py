import urllib.request
import urllib.parse
import json
import os
import subprocess
import time
import sys

# Target directory
OUTPUT_DIR = os.path.abspath('public/images/items')
os.makedirs(OUTPUT_DIR, exist_ok=True)

HEADERS = {
    'User-Agent': 'BalajiCafeMenuApp/1.0 (devanshsoni@example.com)'
}

# 58 Menu items with prioritized search queries and backup specific Wikimedia files
MENU_ITEMS = [
    # ── DOSA (14) ──
    {
        "id": "masala-dosa",
        "name": "Masala Dosa",
        "queries": ["Masala Dosa", "South Indian Masala Dosa"],
        "direct_file": "File:Masala dosa 01.jpg"
    },
    {
        "id": "plain-dosa",
        "name": "Plain Dosa",
        "queries": ["Plain Dosa", "Sada Dosa"],
        "direct_file": "File:Plain Dosa from North India.jpg"
    },
    {
        "id": "sponge-dosa",
        "name": "Sponge Dosa",
        "queries": ["Set Dosa Karnataka", "Sponge Dosa"],
        "direct_file": "File:Dosa chutni.jpg"
    },
    {
        "id": "topi-plain-dosa",
        "name": "Topi Plain Dosa",
        "queries": ["Cone Dosa", "Paper Roast Dosa"],
        "direct_file": "File:Dosa 4.jpg"
    },
    {
        "id": "butter-sponge-dosa",
        "name": "Butter Sponge Dosa",
        "queries": ["Benne Dosa", "Butter Dosa"],
        "direct_file": "File:Davanagere Benne Dosa.jpg"
    },
    {
        "id": "cut-dosa",
        "name": "Cut Dosa",
        "queries": ["Mumbai Cut Dosa", "Cut Dosa"],
        "direct_file": "File:Aate ka dosa.jpg"
    },
    {
        "id": "cheese-masala-dosa",
        "name": "Cheese Masala Dosa",
        "queries": ["Cheese dosa", "Cheese Masala Dosa"],
        "direct_file": "File:Cheese dosa.jpg"
    },
    {
        "id": "shezwan-masala-dosa",
        "name": "Shezwan Masala Dosa",
        "queries": ["Schezwan dosa", "Schezwan masala dosa"],
        "direct_file": "File:Schezwan masala dosa.jpg"
    },
    {
        "id": "topi-masala-dosa",
        "name": "Topi Masala Dosa",
        "queries": ["Paper Masala Dosa", "Crispy Masala Dosa"],
        "direct_file": "File:A crispy golden dosa.jpg"
    },
    {
        "id": "cheese-set-dosa",
        "name": "Cheese Set Dosa",
        "queries": ["Cheese paneer dosa", "Cheese Dosa"],
        "direct_file": "File:Cheese paneer dosa.jpg"
    },
    {
        "id": "mysore-masala-dosa",
        "name": "Mysore Masala Dosa",
        "queries": ["Mysore masala dosa", "Mysore Dosa"],
        "direct_file": "File:Mysore masala dosa in Mysuru, July 2013.jpg"
    },
    {
        "id": "cheese-cut-dosa",
        "name": "Cheese Cut Dosa",
        "queries": ["Cheese dosa roll", "Cheese cut dosa"],
        "direct_file": "File:Butter Dosa.JPG"
    },
    {
        "id": "mysore-cheese-masala-dosa",
        "name": "Mysore Cheese Masala Dosa",
        "queries": ["Mysore cheese dosa", "Mysore Masala Dosa"],
        "direct_file": "File:Mysore masala dosa (2912728481).jpg"
    },
    {
        "id": "corn-cheese-dosa",
        "name": "Corn Cheese Dosa",
        "queries": ["Corn cheese dosa", "Corn Dosa"],
        "direct_file": "File:A Crispy Dosa.jpg"
    },

    # ── UTTAPPA (9) ──
    {
        "id": "plain-uttappa",
        "name": "Plain Uttappa",
        "queries": ["Plain Uttapam", "Uttapam South Indian"],
        "direct_file": "File:Indian Pancake.jpg"
    },
    {
        "id": "onion-uttappa",
        "name": "Onion Uttappa",
        "queries": ["Onion Uttapam", "Onion Uthappam"],
        "direct_file": "File:Onion \"Uttapam\".jpg"
    },
    {
        "id": "cheese-onion-uttappa",
        "name": "Cheese Onion Uttappa",
        "queries": ["Cheese uttapam", "Uttapam cheese"],
        "direct_file": "File:Mixed uthappam at Marksmen, Hazratganj, Lucknow (2025-08-02).jpg"
    },
    {
        "id": "masala-uttappa",
        "name": "Masala Uttappa",
        "queries": ["Masala Uttapam", "Uttapam masala"],
        "direct_file": "File:Aloo Masala, Tomato Chutney, Coconut Chutney, Uttapam and Dosa.jpg"
    },
    {
        "id": "tomato-onion-uttappa",
        "name": "Tomato Onion Uttappa",
        "queries": ["Tomato onion uttapam", "Tomato Uttapam"],
        "direct_file": "File:Onion Uttapam with butter.jpg"
    },
    {
        "id": "cheese-tomato-onion-uttappa",
        "name": "Cheese Tomato Onion Uttappa",
        "queries": ["Cheese tomato uttapam", "Vegetable uttapam"],
        "direct_file": "File:Cabbage uttapam.JPG"
    },
    {
        "id": "tomato-uttappa",
        "name": "Tomato Uttappa",
        "queries": ["Tomato uttapam", "Tomato Uthappam"],
        "direct_file": "File:Mini Uttappam.jpg"
    },
    {
        "id": "corn-cheese-uttappa",
        "name": "Corn Cheese Uttappa",
        "queries": ["Corn uttapam", "Vegetable uttapam Indian"],
        "direct_file": "File:\"Uthappam Overload \".jpg"
    },
    {
        "id": "corn-schezwan-cheese-uttappa",
        "name": "Corn Schezwan Cheese Uttappa",
        "queries": ["Spicy uttapam", "Schezwan uttapam"],
        "direct_file": "File:Mix lentils Uttapam IMG 5948.jpg"
    },

    # ── NOODLES (6) ──
    {
        "id": "veg-hakka-noodle",
        "name": "Veg Hakka Noodle",
        "queries": ["Hakka Noodles", "Veg Hakka Noodles"],
        "direct_file": "File:Tasty hakka noodles image.jpg"
    },
    {
        "id": "veg-schezwan-hakka-noodle",
        "name": "Veg Schezwan Hakka Noodle",
        "queries": ["Schezwan noodles", "Spicy noodles Indian"],
        "direct_file": "File:Schezwan noodles.jpg"
    },
    {
        "id": "veg-chilli-garlic-noodle",
        "name": "Veg Chilli Garlic Noodle",
        "queries": ["Chilli garlic noodles", "Garlic noodles"],
        "direct_file": "File:Schezwan noodles in india.jpg"
    },
    {
        "id": "veg-mushroom-noodle",
        "name": "Veg Mushroom Noodle",
        "queries": ["Mushroom noodles", "Stir fry noodles vegetables"],
        "direct_file": "File:Chowmein 1.jpg"
    },
    {
        "id": "veg-panner-noodle",
        "name": "Veg Panner Noodle",
        "queries": ["Paneer noodles", "Veg chowmein"],
        "direct_file": "File:Hakka Noodles, Veg Manchurian PK009.jpg"
    },
    {
        "id": "veg-panner-schezwan-noodle",
        "name": "Veg Panner Schezwan Noodle",
        "queries": ["Paneer schezwan noodles", "Spicy chowmein"],
        "direct_file": "File:Buff Chowmein 2.jpg"
    },

    # ── RICE (8) ──
    {
        "id": "veg-fried-rice",
        "name": "Veg Fried Rice",
        "queries": ["Veg Fried Rice", "Vegetable fried rice Indian"],
        "direct_file": "File:Veg Fried Rice (51465).jpg"
    },
    {
        "id": "veg-schezwan-rice",
        "name": "Veg Schezwan Rice",
        "queries": ["Schezwan fried rice", "Spicy fried rice Indian"],
        "direct_file": "File:Schezwan Egg Fried Rice with raitha 03.jpg"
    },
    {
        "id": "veg-chilly-garlic-rice",
        "name": "Veg Chilly Garlic Rice",
        "queries": ["Chilli garlic rice", "Garlic fried rice"],
        "direct_file": "File:Veg - Fried Rice.jpg"
    },
    {
        "id": "veg-mushroom-rice",
        "name": "Veg Mushroom Rice",
        "queries": ["Mushroom fried rice", "Mushroom rice"],
        "direct_file": "File:\"Mushroom Fried Rice\".jpg"
    },
    {
        "id": "veg-panner-fried-rice",
        "name": "Veg Panner Fried Rice",
        "queries": ["Paneer fried rice", "Paneer rice"],
        "direct_file": "File:Veg Chinese Fried Rice Recipe By Sonia Goyal.jpg"
    },
    {
        "id": "veg-panner-schezwan-rice",
        "name": "Veg Paneer Schezwan Rice",
        "queries": ["Paneer schezwan rice", "Schezwan rice"],
        "direct_file": "File:Schezwan Egg Fried Rice with raitha 04.jpg"
    },
    {
        "id": "gobi-fried-rice",
        "name": "Gobi Fried Rice",
        "queries": ["Gobi fried rice", "Cauliflower fried rice"],
        "direct_file": "File:Fried Rice & Chilli Gobi.JPG"
    },
    {
        "id": "soya-fried-rice",
        "name": "Soya Fried Rice",
        "queries": ["Soya chunk fried rice", "Veg fried rice Indian"],
        "direct_file": "File:VEG FRIED RICE.jpg"
    },

    # ── SOUP (4) ──
    {
        "id": "veg-manchow-soup",
        "name": "Veg Manchow Soup",
        "queries": ["Manchow soup Indian", "Veg manchow soup"],
        "direct_file": "File:Indian style manchow soup.jpg"
    },
    {
        "id": "veg-noodle-soup",
        "name": "Veg Noodle Soup",
        "queries": ["Vegetable noodle soup", "Noodle clear soup"],
        "direct_file": "File:Chinese noodles and manchow soup.jpg"
    },
    {
        "id": "veg-sweet-corn-soup",
        "name": "Veg Sweet Corn Soup",
        "queries": ["Sweet corn vegetable soup", "Sweet corn soup"],
        "direct_file": "File:An aesthetic Chicken Sweetcorn soup.jpg"
    },
    {
        "id": "veg-tomato-soup",
        "name": "Veg Tomato Soup",
        "queries": ["Tomato soup Indian", "Cream of tomato soup"],
        "direct_file": "File:Tomato, Basil and Red Pepper Soup.jpg"
    },

    # ── DRY & GRAVY (6) ──
    {
        "id": "gobi-manchurian",
        "name": "Gobi Manchurian",
        "queries": ["Gobi manchurian", "Dry Gobi manchurian"],
        "direct_file": "File:Gobi manchurian.jpg"
    },
    {
        "id": "veg-manchurian",
        "name": "Veg Manchurian",
        "queries": ["Veg manchurian gravy", "Vegetable manchurian"],
        "direct_file": "File:Delicious Gobi Manchurian.jpg"
    },
    {
        "id": "veg-shezwan-manchurian",
        "name": "Veg Shezwan Manchurian",
        "queries": ["Schezwan manchurian", "Spicy manchurian"],
        "direct_file": "File:Dry Gobi Manchurians.JPG"
    },
    {
        "id": "veg-chilli",
        "name": "Veg Chilli",
        "queries": ["Chilli gobi", "Veg chilli dry"],
        "direct_file": "File:Chilli gobi 2.jpg"
    },
    {
        "id": "paneer-chilly",
        "name": "Paneer Chilly",
        "queries": ["Chilli paneer dry", "Paneer chilli"],
        "direct_file": "File:Chilly Paneer 01.jpg"
    },
    {
        "id": "veg-crispy",
        "name": "Veg Crispy",
        "queries": ["Chilli gobi fried", "Veg crispy"],
        "direct_file": "File:Chilli gobi 3.jpg"
    },

    # ── CHOUPSEY (3) ──
    {
        "id": "veg-chinese-bhel",
        "name": "Veg Chinese Bhel",
        "queries": ["Chinese bhel", "Crispy noodles bhel"],
        "direct_file": "File:Chopsueywithrice.jpg"
    },
    {
        "id": "veg-sezwan-choupsey",
        "name": "Veg Sezwan Choupsey",
        "queries": ["Schezwan chop suey", "Crispy chopsuey"],
        "direct_file": "File:Chop suey (Philippines).jpg"
    },
    {
        "id": "american-choupsey",
        "name": "American Choupsey",
        "queries": ["American chop suey Indian", "American chopsuey"],
        "direct_file": "File:Chop suey made in Ankara.jpg"
    },

    # ── CHINESE COMBO (8) ──
    {
        "id": "veg-manchurian-noodle",
        "name": "Veg Manchurian Noodle",
        "queries": ["Noodles manchurian combo", "Manchurian noodles"],
        "direct_file": "File:Hakka Noodles, Veg Manchurian PK009.jpg"
    },
    {
        "id": "veg-triple-noodle",
        "name": "Veg Triple Noodle",
        "queries": ["Triple schezwan noodles", "Triple noodles"],
        "direct_file": "File:Char Kway Teow (1).jpg"
    },
    {
        "id": "panner-triple-noodle",
        "name": "Panner Triple Noodle",
        "queries": ["Paneer triple noodles", "Triple schezwan"],
        "direct_file": "File:Char Kway Teow in Hong Kong.jpg"
    },
    {
        "id": "veg-mushroom-triple-noodle",
        "name": "Veg Mushroom Triple Noodle",
        "queries": ["Mushroom triple noodles", "Mushroom chow mein"],
        "direct_file": "File:Char kway teow in parit buntar.jpg"
    },
    {
        "id": "veg-manchurian-rice",
        "name": "Veg Manchurian Rice",
        "queries": ["Fried rice and manchurian combo", "Manchurian rice"],
        "direct_file": "File:Homemade Veg Manchurian and fried rice.jpg"
    },
    {
        "id": "veg-triple-sezwan-rice",
        "name": "Veg Triple Sezwan Rice",
        "queries": ["Triple schezwan rice", "Triple fried rice"],
        "direct_file": "File:A blend of Home made Chinese Food.jpg"
    },
    {
        "id": "paneer-triple-rice",
        "name": "Paneer Triple Rice",
        "queries": ["Paneer triple rice", "Triple rice Indian"],
        "direct_file": "File:A Golden fried rice at Lunchbox.jpg"
    },
    {
        "id": "mushroom-triple-rice",
        "name": "Mushroom Triple Rice",
        "queries": ["Mushroom triple rice", "Triple schezwan fried rice"],
        "direct_file": "File:A plate of friend rice with sauce.jpg"
    },
]

def get_file_url(file_title):
    params = {
        'action': 'query',
        'titles': file_title,
        'prop': 'imageinfo',
        'iiprop': 'url',
        'format': 'json'
    }
    url = 'https://commons.wikimedia.org/w/api.php?' + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read().decode())
            pages = data.get('query', {}).get('pages', {})
            for pid, p in pages.items():
                infos = p.get('imageinfo', [])
                if infos:
                    return infos[0]['url']
    except Exception as e:
        print(f"Error querying {file_title}: {e}")
    return None

def download_and_crop(url, out_path):
    temp_path = out_path + '.temp.jpg'
    cmd = [
        'curl', '-s', '-L',
        '-A', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
        '-e', 'https://commons.wikimedia.org/',
        '-o', temp_path,
        url
    ]
    res = subprocess.run(cmd)
    if res.returncode != 0 or not os.path.exists(temp_path) or os.path.getsize(temp_path) < 1000:
        if os.path.exists(temp_path):
            os.remove(temp_path)
        return False

    # Resize using macOS sips tool: 640x480 (4:3 aspect ratio)
    crop_cmd = ['sips', '-z', '480', '640', temp_path, '--out', out_path]
    subprocess.run(crop_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if os.path.exists(temp_path):
        os.remove(temp_path)
    return os.path.exists(out_path) and os.path.getsize(out_path) > 1000

print(f"Starting distinct image download for all {len(MENU_ITEMS)} menu items...")
success_count = 0

for idx, item in enumerate(MENU_ITEMS):
    item_id = item['id']
    item_name = item['name']
    target_path = os.path.join(OUTPUT_DIR, f"{item_id}.jpg")

    print(f"[{idx+1}/{len(MENU_ITEMS)}] Processing '{item_name}' ({item_id})...")

    # If already downloaded and valid, skip
    if os.path.exists(target_path) and os.path.getsize(target_path) > 5000:
        print(f"  -> Already exists ({os.path.getsize(target_path)} bytes)")
        success_count += 1
        continue

    # 1. Try direct file if specified
    img_url = None
    if item.get('direct_file'):
        img_url = get_file_url(item['direct_file'])
        time.sleep(0.5)

    if img_url:
        ok = download_and_crop(img_url, target_path)
        if ok:
            print(f"  -> Downloaded & formatted: {target_path} ({os.path.getsize(target_path)} bytes)")
            success_count += 1
            continue

    print(f"  -> Direct file failed or missing for {item_id}")

print(f"\nCompleted: {success_count}/{len(MENU_ITEMS)} distinct images in {OUTPUT_DIR}")
