// All prices are confirmed from the physical café menu board.
// halfPrice and fullPrice are used for portion-based items (Noodles, Rice, Chinese Combo).
// price is used for single-portion items (Dosa, Uttappa, Soup, Dry & Gravy, Choupsey).
// image specifies the distinct representative food photograph for each dish.

export type MenuItem = {
  id: string
  name: string
  category: string
  price?: number
  halfPrice?: number
  fullPrice?: number
  image?: string
}

export const categories = [
  'Dosa',
  'Uttappa',
  'Noodles',
  'Rice',
  'Soup',
  'Dry & Gravy',
  'Choupsey',
  'Chinese Combo',
] as const

export const menuItems: MenuItem[] = [
  // ── DOSA ────────────────────────────────────────────────────────────
  { id: 'masala-dosa',              name: 'Masala Dosa',              category: 'Dosa', price: 90,  image: '/images/items/masala-dosa.jpg' },
  { id: 'plain-dosa',               name: 'Plain Dosa',               category: 'Dosa', price: 70,  image: '/images/items/plain-dosa.jpg' },
  { id: 'sponge-dosa',              name: 'Sponge Dosa',              category: 'Dosa', price: 100, image: '/images/items/sponge-dosa.jpg' },
  { id: 'topi-plain-dosa',          name: 'Topi Plain Dosa',          category: 'Dosa', price: 110, image: '/images/items/topi-plain-dosa.jpg' },
  { id: 'butter-sponge-dosa',       name: 'Butter Sponge Dosa',       category: 'Dosa', price: 110, image: '/images/items/butter-sponge-dosa.jpg' },
  { id: 'cut-dosa',                 name: 'Cut Dosa',                 category: 'Dosa', price: 100, image: '/images/items/cut-dosa.jpg' },
  { id: 'cheese-masala-dosa',       name: 'Cheese Masala Dosa',       category: 'Dosa', price: 120, image: '/images/items/cheese-masala-dosa.jpg' },
  { id: 'shezwan-masala-dosa',      name: 'Shezwan Masala Dosa',      category: 'Dosa', price: 60,  image: '/images/items/shezwan-masala-dosa.jpg' },
  { id: 'topi-masala-dosa',         name: 'Topi Masala Dosa',         category: 'Dosa', price: 80,  image: '/images/items/topi-masala-dosa.jpg' },
  { id: 'cheese-set-dosa',          name: 'Cheese Set Dosa',          category: 'Dosa', price: 120, image: '/images/items/cheese-set-dosa.jpg' },
  { id: 'mysore-masala-dosa',       name: 'Mysore Masala Dosa',       category: 'Dosa', price: 80,  image: '/images/items/mysore-masala-dosa.jpg' },
  { id: 'cheese-cut-dosa',          name: 'Cheese Cut Dosa',          category: 'Dosa', price: 110, image: '/images/items/cheese-cut-dosa.jpg' },
  { id: 'mysore-cheese-masala-dosa',name: 'Mysore Cheese Masala Dosa',category: 'Dosa', price: 110, image: '/images/items/mysore-cheese-masala-dosa.jpg' },
  { id: 'corn-cheese-dosa',         name: 'Corn Cheese Dosa',         category: 'Dosa', price: 100, image: '/images/items/corn-cheese-dosa.jpg' },

  // ── UTTAPPA ──────────────────────────────────────────────────────────
  { id: 'plain-uttappa',                  name: 'Plain Uttappa',                  category: 'Uttappa', price: 80,  image: '/images/items/plain-uttappa.jpg' },
  { id: 'onion-uttappa',                  name: 'Onion Uttappa',                  category: 'Uttappa', price: 100, image: '/images/items/onion-uttappa.jpg' },
  { id: 'cheese-onion-uttappa',           name: 'Cheese Onion Uttappa',           category: 'Uttappa', price: 120, image: '/images/items/cheese-onion-uttappa.jpg' },
  { id: 'masala-uttappa',                 name: 'Masala Uttappa',                 category: 'Uttappa', price: 110, image: '/images/items/masala-uttappa.jpg' },
  { id: 'tomato-onion-uttappa',           name: 'Tomato Onion Uttappa',           category: 'Uttappa', price: 110, image: '/images/items/tomato-onion-uttappa.jpg' },
  { id: 'cheese-tomato-onion-uttappa',    name: 'Cheese Tomato Onion Uttappa',    category: 'Uttappa', price: 120, image: '/images/items/cheese-tomato-onion-uttappa.jpg' },
  { id: 'tomato-uttappa',                 name: 'Tomato Uttappa',                 category: 'Uttappa', price: 100, image: '/images/items/tomato-uttappa.jpg' },
  { id: 'corn-cheese-uttappa',            name: 'Corn Cheese Uttappa',            category: 'Uttappa', price: 130, image: '/images/items/corn-cheese-uttappa.jpg' },
  { id: 'corn-schezwan-cheese-uttappa',   name: 'Corn Schezwan Cheese Uttappa',   category: 'Uttappa', price: 130, image: '/images/items/corn-schezwan-cheese-uttappa.jpg' },

  // ── NOODLES (Half / Full) ────────────────────────────────────────────
  { id: 'veg-hakka-noodle',               name: 'Veg Hakka Noodle',               category: 'Noodles', halfPrice: 120, fullPrice: 150, image: '/images/items/veg-hakka-noodle.jpg' },
  { id: 'veg-schezwan-hakka-noodle',      name: 'Veg Schezwan Hakka Noodle',      category: 'Noodles', halfPrice: 120, fullPrice: 160, image: '/images/items/veg-schezwan-hakka-noodle.jpg' },
  { id: 'veg-chilli-garlic-noodle',       name: 'Veg Chilli Garlic Noodle',       category: 'Noodles', halfPrice: 120, fullPrice: 160, image: '/images/items/veg-chilli-garlic-noodle.jpg' },
  { id: 'veg-mushroom-noodle',            name: 'Veg Mushroom Noodle',            category: 'Noodles', halfPrice: 140, fullPrice: 190, image: '/images/items/veg-mushroom-noodle.jpg' },
  { id: 'veg-panner-noodle',              name: 'Veg Panner Noodle',              category: 'Noodles', halfPrice: 140, fullPrice: 190, image: '/images/items/veg-panner-noodle.jpg' },
  { id: 'veg-panner-schezwan-noodle',     name: 'Veg Panner Schezwan Noodle',     category: 'Noodles', halfPrice: 140, fullPrice: 190, image: '/images/items/veg-panner-schezwan-noodle.jpg' },

  // ── RICE (Half / Full) ───────────────────────────────────────────────
  { id: 'veg-fried-rice',                 name: 'Veg Fried Rice',                 category: 'Rice', halfPrice: 120, fullPrice: 160, image: '/images/items/veg-fried-rice.jpg' },
  { id: 'veg-schezwan-rice',              name: 'Veg Schezwan Rice',              category: 'Rice', halfPrice: 120, fullPrice: 160, image: '/images/items/veg-schezwan-rice.jpg' },
  { id: 'veg-chilly-garlic-rice',         name: 'Veg Chilly Garlic Rice',         category: 'Rice', halfPrice: 140, fullPrice: 190, image: '/images/items/veg-chilly-garlic-rice.jpg' },
  { id: 'veg-mushroom-rice',              name: 'Veg Mushroom Rice',              category: 'Rice', halfPrice: 140, fullPrice: 190, image: '/images/items/veg-mushroom-rice.jpg' },
  { id: 'veg-panner-fried-rice',          name: 'Veg Panner Fried Rice',          category: 'Rice', halfPrice: 140, fullPrice: 190, image: '/images/items/veg-panner-fried-rice.jpg' },
  { id: 'veg-panner-schezwan-rice',       name: 'Veg Paneer Schezwan Rice',       category: 'Rice', halfPrice: 140, fullPrice: 190, image: '/images/items/veg-panner-schezwan-rice.jpg' },
  { id: 'gobi-fried-rice',                name: 'Gobi Fried Rice',                category: 'Rice', halfPrice: 120, fullPrice: 190, image: '/images/items/gobi-fried-rice.jpg' },
  { id: 'soya-fried-rice',                name: 'Soya Fried Rice',                category: 'Rice', halfPrice: 120, fullPrice: 160, image: '/images/items/soya-fried-rice.jpg' },

  // ── SOUP ─────────────────────────────────────────────────────────────
  { id: 'veg-manchow-soup',       name: 'Veg Manchow Soup',       category: 'Soup', price: 100, image: '/images/items/veg-manchow-soup.jpg' },
  { id: 'veg-noodle-soup',        name: 'Veg Noodle Soup',        category: 'Soup', price: 110, image: '/images/items/veg-noodle-soup.jpg' },
  { id: 'veg-sweet-corn-soup',    name: 'Veg Sweet Corn Soup',    category: 'Soup', price: 110, image: '/images/items/veg-sweet-corn-soup.jpg' },
  { id: 'veg-tomato-soup',        name: 'Veg Tomato Soup',        category: 'Soup', price: 110, image: '/images/items/veg-tomato-soup.jpg' },

  // ── DRY & GRAVY ───────────────────────────────────────────────────────
  { id: 'gobi-manchurian',          name: 'Gobi Manchurian',          category: 'Dry & Gravy', price: 180, image: '/images/items/gobi-manchurian.jpg' },
  { id: 'veg-manchurian',           name: 'Veg Manchurian',           category: 'Dry & Gravy', price: 160, image: '/images/items/veg-manchurian.jpg' },
  { id: 'veg-shezwan-manchurian',   name: 'Veg Shezwan Manchurian',   category: 'Dry & Gravy', price: 160, image: '/images/items/veg-shezwan-manchurian.jpg' },
  { id: 'veg-chilli',               name: 'Veg Chilli',               category: 'Dry & Gravy', price: 160, image: '/images/items/veg-chilli.jpg' },
  { id: 'paneer-chilly',            name: 'Paneer Chilly',            category: 'Dry & Gravy', price: 180, image: '/images/items/paneer-chilly.jpg' },
  { id: 'veg-crispy',               name: 'Veg Crispy',               category: 'Dry & Gravy', price: 180, image: '/images/items/veg-crispy.jpg' },

  // ── CHOUPSEY ──────────────────────────────────────────────────────────
  { id: 'veg-chinese-bhel',       name: 'Veg Chinese Bhel',       category: 'Choupsey', price: 150, image: '/images/items/veg-chinese-bhel.jpg' },
  { id: 'veg-sezwan-choupsey',    name: 'Veg Sezwan Choupsey',    category: 'Choupsey', price: 150, image: '/images/items/veg-sezwan-choupsey.jpg' },
  { id: 'american-choupsey',      name: 'American Choupsey',      category: 'Choupsey', price: 150, image: '/images/items/american-choupsey.jpg' },

  // ── CHINESE COMBO (Half / Full) ───────────────────────────────────────
  { id: 'veg-manchurian-noodle',      name: 'Veg Manchurian Noodle',      category: 'Chinese Combo', halfPrice: 160, fullPrice: 220, image: '/images/items/veg-manchurian-noodle.jpg' },
  { id: 'veg-triple-noodle',          name: 'Veg Triple Noodle',          category: 'Chinese Combo', halfPrice: 160, fullPrice: 230, image: '/images/items/veg-triple-noodle.jpg' },
  { id: 'panner-triple-noodle',       name: 'Panner Triple Noodle',       category: 'Chinese Combo', halfPrice: 160, fullPrice: 240, image: '/images/items/panner-triple-noodle.jpg' },
  { id: 'veg-mushroom-triple-noodle', name: 'Veg Mushroom Triple Noodle', category: 'Chinese Combo', halfPrice: 160, fullPrice: 240, image: '/images/items/veg-mushroom-triple-noodle.jpg' },
  { id: 'veg-manchurian-rice',        name: 'Veg Manchurian Rice',        category: 'Chinese Combo', halfPrice: 160, fullPrice: 220, image: '/images/items/veg-manchurian-rice.jpg' },
  { id: 'veg-triple-sezwan-rice',     name: 'Veg Triple Sezwan Rice',     category: 'Chinese Combo', halfPrice: 160, fullPrice: 230, image: '/images/items/veg-triple-sezwan-rice.jpg' },
  { id: 'paneer-triple-rice',         name: 'Paneer Triple Rice',         category: 'Chinese Combo', halfPrice: 160, fullPrice: 240, image: '/images/items/paneer-triple-rice.jpg' },
  { id: 'mushroom-triple-rice',       name: 'Mushroom Triple Rice',       category: 'Chinese Combo', halfPrice: 160, fullPrice: 240, image: '/images/items/mushroom-triple-rice.jpg' },
]
