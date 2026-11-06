import urllib.request
import urllib.parse
import json
import os
import subprocess
import time

ITEMS = [
    # DOSA (14)
    {"id": "masala-dosa", "name": "Masala Dosa", "queries": ["Masala Dosa", "Dosa sambar", "South Indian Dosa"]},
    {"id": "plain-dosa", "name": "Plain Dosa", "queries": ["Plain Dosa", "Sada Dosa", "Paper Dosa"]},
    {"id": "sponge-dosa", "name": "Sponge Dosa", "queries": ["Set Dosa", "Sponge Dosa", "Dosa chutney"]},
    {"id": "topi-plain-dosa", "name": "Topi Plain Dosa", "queries": ["Cone Dosa", "Paper Roast Dosa", "Ghee Roast Dosa"]},
    {"id": "butter-sponge-dosa", "name": "Butter Sponge Dosa", "queries": ["Benne Dosa", "Butter Dosa", "Davangere Benne Dosa"]},
    {"id": "cut-dosa", "name": "Cut Dosa", "queries": ["Cut Dosa", "Mumbai Dosa", "Dosa street food"]},
    {"id": "cheese-masala-dosa", "name": "Cheese Masala Dosa", "queries": ["Cheese Dosa", "Cheese Masala Dosa", "Fusion Dosa"]},
    {"id": "shezwan-masala-dosa", "name": "Shezwan Masala Dosa", "queries": ["Schezwan Dosa", "Chinese Dosa", "Spicy Dosa"]},
    {"id": "topi-masala-dosa", "name": "Topi Masala Dosa", "queries": ["Paper Masala Dosa", "Crispy Dosa", "Roast Dosa"]},
    {"id": "cheese-set-dosa", "name": "Cheese Set Dosa", "queries": ["Set Dosa cheese", "Cheese Dosa", "Set Dosa"]},
    {"id": "mysore-masala-dosa", "name": "Mysore Masala Dosa", "queries": ["Mysore Masala Dosa", "Mysore Dosa", "Red chutney Dosa"]},
    {"id": "cheese-cut-dosa", "name": "Cheese Cut Dosa", "queries": ["Cheese Dosa Mumbai", "Cut Dosa cheese", "Cheese Dosa"]},
    {"id": "mysore-cheese-masala-dosa", "name": "Mysore Cheese Masala Dosa", "queries": ["Mysore Cheese Dosa", "Mysore Masala", "Masala Dosa"]},
    {"id": "corn-cheese-dosa", "name": "Corn Cheese Dosa", "queries": ["Corn Dosa", "Cheese Dosa", "Dosa street"]},

    # UTTAPPA (9)
    {"id": "plain-uttappa", "name": "Plain Uttappa", "queries": ["Plain Uttapam", "Uttapam", "Uthappam"]},
    {"id": "onion-uttappa", "name": "Onion Uttappa", "queries": ["Onion Uttapam", "Onion Uthappam", "Uttapam onion"]},
    {"id": "cheese-onion-uttappa", "name": "Cheese Onion Uttappa", "queries": ["Cheese Uttapam", "Onion Uttapam", "Uthappam"]},
    {"id": "masala-uttappa", "name": "Masala Uttappa", "queries": ["Masala Uttapam", "Uttapam South Indian", "Uttapam"]},
    {"id": "tomato-onion-uttappa", "name": "Tomato Onion Uttappa", "queries": ["Tomato Onion Uttapam", "Tomato Uttapam", "Uthappam"]},
    {"id": "cheese-tomato-onion-uttappa", "name": "Cheese Tomato Onion Uttappa", "queries": ["Cheese Tomato Uttapam", "Mixed veg Uttapam", "Uttapam"]},
    {"id": "tomato-uttappa", "name": "Tomato Uttappa", "queries": ["Tomato Uttapam", "Tomato Uthappam", "Uttapam tomato"]},
    {"id": "corn-cheese-uttappa", "name": "Corn Cheese Uttappa", "queries": ["Corn Uttapam", "Cheese Uttapam", "Uttapam"]},
    {"id": "corn-schezwan-cheese-uttappa", "name": "Corn Schezwan Cheese Uttappa", "queries": ["Schezwan Uttapam", "Spicy Uttapam", "Uttapam"]},

    # NOODLES (6)
    {"id": "veg-hakka-noodle", "name": "Veg Hakka Noodle", "queries": ["Hakka Noodles", "Veg Noodles", "Chow mein"]},
    {"id": "veg-schezwan-hakka-noodle", "name": "Veg Schezwan Hakka Noodle", "queries": ["Schezwan Noodles", "Spicy Hakka Noodles", "Chilli noodles"]},
    {"id": "veg-chilli-garlic-noodle", "name": "Veg Chilli Garlic Noodle", "queries": ["Chilli garlic noodles", "Garlic noodles", "Veg noodles"]},
    {"id": "veg-mushroom-noodle", "name": "Veg Mushroom Noodle", "queries": ["Mushroom noodles", "Stir fry noodles", "Veg noodles"]},
    {"id": "veg-panner-noodle", "name": "Veg Panner Noodle", "queries": ["Paneer noodles", "Tofu noodles", "Hakka noodles"]},
    {"id": "veg-panner-schezwan-noodle", "name": "Veg Panner Schezwan Noodle", "queries": ["Paneer Schezwan Noodles", "Schezwan noodles", "Spicy noodles"]},

    # RICE (8)
    {"id": "veg-fried-rice", "name": "Veg Fried Rice", "queries": ["Vegetable fried rice", "Veg Fried Rice", "Fried rice"]},
    {"id": "veg-schezwan-rice", "name": "Veg Schezwan Rice", "queries": ["Schezwan Fried Rice", "Schezwan Rice", "Spicy fried rice"]},
    {"id": "veg-chilly-garlic-rice", "name": "Veg Chilly Garlic Rice", "queries": ["Chilli garlic fried rice", "Garlic fried rice", "Fried rice"]},
    {"id": "veg-mushroom-rice", "name": "Veg Mushroom Rice", "queries": ["Mushroom fried rice", "Mushroom rice", "Fried rice"]},
    {"id": "veg-panner-fried-rice", "name": "Veg Panner Fried Rice", "queries": ["Paneer fried rice", "Paneer rice", "Veg fried rice"]},
    {"id": "veg-panner-schezwan-rice", "name": "Veg Paneer Schezwan Rice", "queries": ["Paneer Schezwan Rice", "Schezwan rice", "Fried rice"]},
    {"id": "gobi-fried-rice", "name": "Gobi Fried Rice", "queries": ["Gobi fried rice", "Cauliflower fried rice", "Fried rice"]},
    {"id": "soya-fried-rice", "name": "Soya Fried Rice", "queries": ["Soya fried rice", "Veg fried rice", "Fried rice"]},

    # SOUP (4)
    {"id": "veg-manchow-soup", "name": "Veg Manchow Soup", "queries": ["Manchow soup", "Vegetable soup noodles", "Hot and sour soup"]},
    {"id": "veg-noodle-soup", "name": "Veg Noodle Soup", "queries": ["Vegetable noodle soup", "Noodle soup", "Clear soup"]},
    {"id": "veg-sweet-corn-soup", "name": "Veg Sweet Corn Soup", "queries": ["Sweet corn soup", "Corn soup", "Vegetable soup"]},
    {"id": "veg-tomato-soup", "name": "Veg Tomato Soup", "queries": ["Tomato soup", "Indian tomato soup", "Cream of tomato soup"]},

    # DRY & GRAVY (6)
    {"id": "gobi-manchurian", "name": "Gobi Manchurian", "queries": ["Gobi manchurian", "Cauliflower manchurian", "Manchurian"]},
    {"id": "veg-manchurian", "name": "Veg Manchurian", "queries": ["Veg manchurian", "Vegetable manchurian", "Manchurian balls"]},
    {"id": "veg-shezwan-manchurian", "name": "Veg Shezwan Manchurian", "queries": ["Schezwan manchurian", "Spicy manchurian", "Veg manchurian"]},
    {"id": "veg-chilli", "name": "Veg Chilli", "queries": ["Chilli vegetable", "Veg chilli gravy", "Chilli paneer"]},
    {"id": "paneer-chilly", "name": "Paneer Chilly", "queries": ["Chilli paneer", "Paneer chilli dry", "Paneer chilli"]},
    {"id": "veg-crispy", "name": "Veg Crispy", "queries": ["Crispy corn", "Crispy veg", "Fried vegetables Indian"]},

    # CHOUPSEY (3)
    {"id": "veg-chinese-bhel", "name": "Veg Chinese Bhel", "queries": ["Chinese bhel", "Crispy noodles salad", "Bhel"]},
    {"id": "veg-sezwan-choupsey", "name": "Veg Sezwan Choupsey", "queries": ["Schezwan chopsuey", "Chop suey", "Crispy noodles"]},
    {"id": "american-choupsey", "name": "American Choupsey", "queries": ["American chop suey", "American choupsey", "Chopsuey"]},

    # CHINESE COMBO (8)
    {"id": "veg-manchurian-noodle", "name": "Veg Manchurian Noodle", "queries": ["Noodles with manchurian", "Manchurian noodles", "Hakka noodles combo"]},
    {"id": "veg-triple-noodle", "name": "Veg Triple Noodle", "queries": ["Triple schezwan noodles", "Triple noodles", "Schezwan noodles"]},
    {"id": "panner-triple-noodle", "name": "Panner Triple Noodle", "queries": ["Paneer triple noodles", "Paneer noodles gravy", "Triple noodles"]},
    {"id": "veg-mushroom-triple-noodle", "name": "Veg Mushroom Triple Noodle", "queries": ["Mushroom triple noodles", "Mushroom noodles", "Triple schezwan"]},
    {"id": "veg-manchurian-rice", "name": "Veg Manchurian Rice", "queries": ["Manchurian with fried rice", "Manchurian rice", "Fried rice manchurian"]},
    {"id": "veg-triple-sezwan-rice", "name": "Veg Triple Sezwan Rice", "queries": ["Triple schezwan rice", "Triple fried rice", "Schezwan rice combo"]},
    {"id": "paneer-triple-rice", "name": "Paneer Triple Rice", "queries": ["Paneer triple rice", "Paneer schezwan rice", "Triple schezwan"]},
    {"id": "mushroom-triple-rice", "name": "Mushroom Triple Rice", "queries": ["Mushroom triple rice", "Mushroom fried rice combo", "Triple rice"]},
]

def search_wikimedia(query):
    params = {
        'action': 'query',
        'generator': 'search',
        'gsrsearch': query,
        'gsrnamespace': 6,
        'gsrlimit': 6,
        'prop': 'imageinfo',
        'iiprop': 'url|mime',
        'format': 'json'
    }
    url = 'https://commons.wikimedia.org/w/api.php?' + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={'User-Agent': 'BalajiCafeMenu/1.0 (contact@example.com)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read().decode())
            pages = data.get('query', {}).get('pages', {})
            urls = []
            for pid, p in pages.items():
                title = p.get('title', '')
                mime = p.get('imageinfo', [{}])[0].get('mime', '')
                if 'image' in mime and not title.lower().endswith('.svg') and not title.lower().endswith('.png') and not title.lower().endswith('.tif'):
                    u = p.get('imageinfo', [{}])[0].get('url', '')
                    if u:
                        urls.append((title, u))
            return urls
    except Exception as e:
        return []

print(f"Total items to fetch: {len(ITEMS)}")
