import urllib.request
import subprocess
import os

OUTPUT_DIR = os.path.abspath('public/images/items')
os.makedirs(OUTPUT_DIR, exist_ok=True)

BEVERAGES_MAP = {
    'special-chai': 'https://images.unsplash.com/photo-1576092768241-dec231879fc3?w=600&auto=format&fit=crop&q=80',
    'filter-coffee': 'https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=600&auto=format&fit=crop&q=80',
    'cold-coffee': 'https://images.unsplash.com/photo-1517701550927-30cf4ba1dba5?w=600&auto=format&fit=crop&q=80',
    'cold-drinks': 'https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=600&auto=format&fit=crop&q=80',
    'mineral-water': 'https://images.unsplash.com/photo-1559839914-17aae19cec71?w=600&auto=format&fit=crop&q=80',
    'masala-chaas': 'https://images.unsplash.com/photo-1556881286-fc6915169721?w=600&auto=format&fit=crop&q=80',
    'fresh-lime-soda': 'https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd?w=600&auto=format&fit=crop&q=80',
    'sweet-lassi': 'https://images.unsplash.com/photo-1571115177098-24ec42ed204d?w=600&auto=format&fit=crop&q=80',
}

CATEGORY_BEV = ('public/images/beverages.jpg', 'https://images.unsplash.com/photo-1544787219-7f47ccb76574?w=600&auto=format&fit=crop&q=80')

def download_and_crop(url, out_path):
    temp_path = out_path + '.temp.jpg'
    cmd = [
        'curl', '-s', '-L',
        '-A', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
        '-o', temp_path,
        url
    ]
    res = subprocess.run(cmd)
    if res.returncode != 0 or not os.path.exists(temp_path) or os.path.getsize(temp_path) < 1000:
        if os.path.exists(temp_path):
            os.remove(temp_path)
        return False

    crop_cmd = ['sips', '-z', '480', '640', temp_path, '--out', out_path]
    subprocess.run(crop_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if os.path.exists(temp_path):
        os.remove(temp_path)
    return os.path.exists(out_path) and os.path.getsize(out_path) > 1000

print("Downloading beverage category image...")
download_and_crop(CATEGORY_BEV[1], CATEGORY_BEV[0])

print(f"Downloading {len(BEVERAGES_MAP)} individual beverage images...")
for name, url in BEVERAGES_MAP.items():
    out_file = os.path.join(OUTPUT_DIR, f"{name}.jpg")
    ok = download_and_crop(url, out_file)
    print(f" - {name}.jpg: {'OK' if ok else 'FAILED'} ({os.path.getsize(out_file) if ok else 0} bytes)")

print("\nDone downloading beverages!")
