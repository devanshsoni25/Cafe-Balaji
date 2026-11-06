import urllib.request
import subprocess
import os

OUTPUT_DIR = os.path.abspath('public/images/items')
os.makedirs(OUTPUT_DIR, exist_ok=True)

REMAINING_MAP = {
    'mysore-masala-dosa': 'https://images.unsplash.com/photo-1630383249896-424e482df921?w=600&auto=format&fit=crop&q=80',
    'cheese-cut-dosa': 'https://images.unsplash.com/photo-1668236543090-82eba5ee5976?w=600&auto=format&fit=crop&q=80',
    'mysore-cheese-masala-dosa': 'https://images.unsplash.com/photo-1589301760014-d929f3979dbc?w=600&auto=format&fit=crop&q=80',
    'corn-cheese-dosa': 'https://images.unsplash.com/photo-1626777552726-4a6b54c97e46?w=600&auto=format&fit=crop&q=80',
    'plain-uttappa': 'https://images.unsplash.com/photo-1589302168068-964664d93dc0?w=600&auto=format&fit=crop&q=80',
    'onion-uttappa': 'https://images.pexels.com/photos/5560763/pexels-photo-5560763.jpeg?auto=compress&cs=tinysrgb&w=600',
    'cheese-onion-uttappa': 'https://images.unsplash.com/photo-1626132647523-66f5bf380027?w=600&auto=format&fit=crop&q=80',
    'masala-uttappa': 'https://images.unsplash.com/photo-1567337710282-00832b415979?w=600&auto=format&fit=crop&q=80',
    'tomato-onion-uttappa': 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=600&auto=format&fit=crop&q=80',
    'cheese-tomato-onion-uttappa': 'https://images.unsplash.com/photo-1601050690597-df0568f70950?w=600&auto=format&fit=crop&q=80',
    'corn-cheese-uttappa': 'https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=600&auto=format&fit=crop&q=80',
    'corn-schezwan-cheese-uttappa': 'https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=600&auto=format&fit=crop&q=80',
    'veg-schezwan-hakka-noodle': 'https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=600&auto=format&fit=crop&q=80',
    'veg-chilli-garlic-noodle': 'https://images.unsplash.com/photo-1585032226651-759b368d7246?w=600&auto=format&fit=crop&q=80',
    'veg-mushroom-noodle': 'https://images.unsplash.com/photo-1617093727343-374698b1b08d?w=600&auto=format&fit=crop&q=80',
    'veg-panner-schezwan-noodle': 'https://images.unsplash.com/photo-1612927601601-6638404737ce?w=600&auto=format&fit=crop&q=80',
    'veg-fried-rice': 'https://images.unsplash.com/photo-1512058564366-18510be2db19?w=600&auto=format&fit=crop&q=80',
    'veg-schezwan-rice': 'https://images.unsplash.com/photo-1596797038530-2c107229654b?w=600&auto=format&fit=crop&q=80',
    'veg-chilly-garlic-rice': 'https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=600&auto=format&fit=crop&q=80',
    'veg-mushroom-rice': 'https://images.unsplash.com/photo-1541832676-9b763b0239ab?w=600&auto=format&fit=crop&q=80',
    'veg-panner-fried-rice': 'https://images.unsplash.com/photo-1633964913295-ceb43826e7c9?w=600&auto=format&fit=crop&q=80',
    'veg-panner-schezwan-rice': 'https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=600&auto=format&fit=crop&q=80',
    'gobi-fried-rice': 'https://images.unsplash.com/photo-1552611052-33e04de081de?w=600&auto=format&fit=crop&q=80',
    'soya-fried-rice': 'https://images.unsplash.com/photo-1526318896980-cf78c088247c?w=600&auto=format&fit=crop&q=80',
    'veg-manchow-soup': 'https://images.unsplash.com/photo-1547592180-85f173990554?w=600&auto=format&fit=crop&q=80',
    'veg-noodle-soup': 'https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?w=600&auto=format&fit=crop&q=80',
    'veg-sweet-corn-soup': 'https://images.unsplash.com/photo-1574484284002-952d92456975?w=600&auto=format&fit=crop&q=80',
    'veg-tomato-soup': 'https://images.unsplash.com/photo-1603105037880-880cd4edfb0d?w=600&auto=format&fit=crop&q=80',
    'veg-manchurian': 'https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?w=600&auto=format&fit=crop&q=80',
    'veg-shezwan-manchurian': 'https://images.unsplash.com/photo-1567188040759-fb8a883dc6d8?w=600&auto=format&fit=crop&q=80',
    'veg-chilli': 'https://images.unsplash.com/photo-1540420773420-3366772f4999?w=600&auto=format&fit=crop&q=80',
    'paneer-chilly': 'https://images.unsplash.com/photo-1567188040759-fb8a883dc6d8?w=600&auto=format&fit=crop&q=80',
    'veg-crispy': 'https://images.unsplash.com/photo-1606471191009-63994c53433b?w=600&auto=format&fit=crop&q=80',
    'veg-chinese-bhel': 'https://images.unsplash.com/photo-1626777552726-4a6b54c97e46?w=600&auto=format&fit=crop&q=80',
    'veg-sezwan-choupsey': 'https://images.unsplash.com/photo-1555126634-323283e090fa?w=600&auto=format&fit=crop&q=80',
    'american-choupsey': 'https://images.unsplash.com/photo-1540420773420-3366772f4999?w=600&auto=format&fit=crop&q=80',
    'veg-triple-noodle': 'https://images.unsplash.com/photo-1552611052-33e04de081de?w=600&auto=format&fit=crop&q=80',
    'panner-triple-noodle': 'https://images.unsplash.com/photo-1612927601601-6638404737ce?w=600&auto=format&fit=crop&q=80',
    'veg-mushroom-triple-noodle': 'https://images.unsplash.com/photo-1617093727343-374698b1b08d?w=600&auto=format&fit=crop&q=80',
    'veg-manchurian-rice': 'https://images.unsplash.com/photo-1512058564366-18510be2db19?w=600&auto=format&fit=crop&q=80',
    'veg-triple-sezwan-rice': 'https://images.unsplash.com/photo-1596797038530-2c107229654b?w=600&auto=format&fit=crop&q=80',
    'paneer-triple-rice': 'https://images.unsplash.com/photo-1633964913295-ceb43826e7c9?w=600&auto=format&fit=crop&q=80',
    'mushroom-triple-rice': 'https://images.unsplash.com/photo-1541832676-9b763b0239ab?w=600&auto=format&fit=crop&q=80'
}

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

    # Resize using macOS sips tool: 640x480 (4:3 aspect ratio)
    crop_cmd = ['sips', '-z', '480', '640', temp_path, '--out', out_path]
    subprocess.run(crop_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if os.path.exists(temp_path):
        os.remove(temp_path)
    return os.path.exists(out_path) and os.path.getsize(out_path) > 1000

print(f"Downloading and optimizing remaining {len(REMAINING_MAP)} images...")
success = 0
for idx, (dish_id, img_url) in enumerate(REMAINING_MAP.items()):
    out_file = os.path.join(OUTPUT_DIR, f"{dish_id}.jpg")
    ok = download_and_crop(img_url, out_file)
    if ok:
        success += 1
        print(f"[{idx+1}/{len(REMAINING_MAP)}] OK: {dish_id}.jpg ({os.path.getsize(out_file)} bytes)")
    else:
        print(f"[{idx+1}/{len(REMAINING_MAP)}] FAILED: {dish_id}")

print(f"\nFinished: {success}/{len(REMAINING_MAP)} downloaded successfully.")
