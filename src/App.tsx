import { useState, useEffect, useRef } from 'react'
import { menuItems, categories } from './menuData'
import type { MenuItem } from './menuData'
import './App.css'

// ── Category Representative Food Images ───────────────────────────────────────
const CATEGORY_IMAGE_MAP: Record<string, string> = {
  'Dosa':          '/images/dosa.jpg',
  'Uttappa':       '/images/uttappa.jpg',
  'Noodles':       '/images/noodles.jpg',
  'Rice':          '/images/rice.jpg',
  'Soup':          '/images/soup.jpg',
  'Dry & Gravy':   '/images/dry-gravy.jpg',
  'Choupsey':      '/images/choupsey.jpg',
  'Chinese Combo': '/images/chinese-combo.jpg',
  'Beverages':     '/images/beverages.jpg',
}

// ── Food Card Component ─────────────────────────────────────────────────────────
function FoodCard({ item }: { item: MenuItem }) {
  const isPortioned = item.halfPrice !== undefined && item.fullPrice !== undefined
  const imageSrc = item.image || CATEGORY_IMAGE_MAP[item.category] || '/images/dosa.jpg'

  return (
    <article className="food-card" id={`item-${item.id}`}>
      {/* 4:3 Aspect Ratio Food Photograph */}
      <div className="food-card__media">
        <img
          src={imageSrc}
          alt={item.name}
          className="food-card__img"
          loading="lazy"
          onError={(e) => {
            const fallback = CATEGORY_IMAGE_MAP[item.category] || '/images/dosa.jpg'
            if (e.currentTarget.src !== fallback) {
              e.currentTarget.src = fallback
            }
          }}
        />
        <div className="veg-badge" title="Pure Veg" aria-label="Pure Vegetarian">
          <span className="veg-badge__circle" />
        </div>
      </div>

      {/* Dish Name & Price Block */}
      <div className="food-card__content">
        <h3 className="food-card__title">{item.name}</h3>

        {isPortioned ? (
          <div className="price-tag price-tag--portioned" aria-label={`Half: ₹${item.halfPrice}, Full: ₹${item.fullPrice}`}>
            <div className="portion-badge">
              <span className="portion-badge__label">HALF</span>
              <span className="portion-badge__price">₹{item.halfPrice}</span>
            </div>
            <div className="portion-divider" aria-hidden="true" />
            <div className="portion-badge">
              <span className="portion-badge__label">FULL</span>
              <span className="portion-badge__price">₹{item.fullPrice}</span>
            </div>
          </div>
        ) : (
          <div className="price-tag" aria-label={`Price: ₹${item.price}`}>
            <span className="single-price">₹{item.price}</span>
          </div>
        )}
      </div>
    </article>
  )
}

// ── Category Navigation Bar ────────────────────────────────────────────────────
function CategoryNav({
  activeCat,
  onSelectCat,
}: {
  activeCat: string
  onSelectCat: (cat: string) => void
}) {
  const navRef = useRef<HTMLDivElement>(null)

  // Scroll active tab into horizontal view WITHIN the nav only (never touches page scroll)
  useEffect(() => {
    const nav = navRef.current
    if (!nav) return
    const activeBtn = nav.querySelector<HTMLButtonElement>(`[data-category="${activeCat}"]`)
    if (!activeBtn) return
    // Calculate offset so the button is centred inside the scrollable nav strip
    const navWidth = nav.clientWidth
    const btnLeft = activeBtn.offsetLeft
    const btnWidth = activeBtn.offsetWidth
    const targetScrollLeft = btnLeft - navWidth / 2 + btnWidth / 2
    nav.scrollTo({ left: targetScrollLeft, behavior: 'smooth' })
  }, [activeCat])

  return (
    <nav className="category-nav-wrapper" aria-label="Menu category navigation">
      <div className="category-nav" ref={navRef}>
        {categories.map((cat) => {
          const isActive = activeCat === cat
          return (
            <button
              key={cat}
              type="button"
              data-category={cat}
              className={`cat-chip ${isActive ? 'cat-chip--active' : ''}`}
              onClick={() => onSelectCat(cat)}
              aria-current={isActive ? 'true' : undefined}
            >
              {cat}
            </button>
          )
        })}
      </div>
    </nav>
  )
}

// ── Universal Table QR Standee Modal Component ────────────────────────────────
function TableQrModal({
  isOpen,
  onClose,
}: {
  isOpen: boolean
  onClose: () => void
}) {
  const [format, setFormat] = useState<'standee' | 'sticker'>('standee')

  if (!isOpen) return null

  const previewImg = format === 'standee'
    ? '/qr-codes/table_standee.png'
    : '/qr-codes/table_sticker.png'

  const downloadFilename = format === 'standee'
    ? 'shree_balaji_table_standee.png'
    : 'shree_balaji_table_sticker.png'

  const handlePrint = () => {
    window.print()
  }

  return (
    <div className="qr-modal-backdrop" onClick={onClose} role="dialog" aria-modal="true">
      <div className="qr-modal" onClick={(e) => e.stopPropagation()}>
        <div className="qr-modal__header">
          <div>
            <h2 className="qr-modal__title">Café Table QR Code</h2>
            <p className="qr-modal__subtitle">Print identical copies of this single QR code for every table</p>
          </div>
          <button className="qr-modal__close" onClick={onClose} aria-label="Close modal">×</button>
        </div>

        {/* Format Selector Toggle */}
        <div className="qr-format-toggle">
          <button
            type="button"
            className={`toggle-btn ${format === 'standee' ? 'toggle-btn--active' : ''}`}
            onClick={() => setFormat('standee')}
          >
            📋 Acrylic Standee Card (4" × 6")
          </button>
          <button
            type="button"
            className={`toggle-btn ${format === 'sticker' ? 'toggle-btn--active' : ''}`}
            onClick={() => setFormat('sticker')}
          >
            🏷️ Table Sticker (Square)
          </button>
        </div>

        {/* Standee / Sticker Preview */}
        <div className="qr-modal__preview">
          <img
            src={previewImg}
            alt="Universal Table QR Code"
            className="qr-standee-preview"
          />
        </div>

        {/* Action Buttons */}
        <div className="qr-modal__actions">
          <button type="button" onClick={handlePrint} className="btn-print">
            🖨️ Print Copies For Tables
          </button>
          <a
            href={previewImg}
            download={downloadFilename}
            className="btn-download"
          >
            📥 Download High-Res PNG
          </a>
          <a
            href="/qr-codes/menu_qr.svg"
            download="shree_balaji_menu_qr.svg"
            className="btn-download-alt"
          >
            Download Pure Vector QR (SVG)
          </a>
        </div>

        <div className="qr-modal__tips">
          <p>💡 <strong>How to Use:</strong> Print 10–20 copies of this single QR card. Slide them into clear acrylic table tents or peel-and-stick them directly onto every table in your café. Every customer will scan and view this menu instantly!</p>
        </div>
      </div>
    </div>
  )
}

// ── Main App ───────────────────────────────────────────────────────────────────
function App() {
  const [activeCategory, setActiveCategory] = useState<string>(categories[0])
  const [showQrModal, setShowQrModal] = useState<boolean>(false)
  const isClickScrolling = useRef(false)
  const clickTimeoutRef = useRef<number | null>(null)

  // Handle smooth scroll when category chip is clicked
  const handleSelectCategory = (cat: string) => {
    setActiveCategory(cat)
    isClickScrolling.current = true

    if (clickTimeoutRef.current) {
      window.clearTimeout(clickTimeoutRef.current)
    }

    const sectionId = `section-${cat.replace(/[^a-zA-Z0-9]/g, '-').toLowerCase()}`
    const el = document.getElementById(sectionId)
    if (el) {
      el.scrollIntoView({ behavior: 'smooth', block: 'start' })
    }

    // Release programmatic scroll flag after animation completes
    clickTimeoutRef.current = window.setTimeout(() => {
      isClickScrolling.current = false
    }, 800)
  }

  // Update active category on user manual scroll
  useEffect(() => {
    const handleScroll = () => {
      if (isClickScrolling.current) return

      const scrollPosition = window.scrollY + 120
      let currentSection: string = categories[0]

      for (const cat of categories) {
        const sectionId = `section-${cat.replace(/[^a-zA-Z0-9]/g, '-').toLowerCase()}`
        const el = document.getElementById(sectionId)
        if (el) {
          const top = el.offsetTop
          if (scrollPosition >= top) {
            currentSection = cat
          }
        }
      }

      setActiveCategory(currentSection)
    }

    window.addEventListener('scroll', handleScroll, { passive: true })
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  return (
    <div className="menu-app">
      {/* Compact Café Header */}
      <header className="cafe-header">
        <div className="cafe-header__stripe" aria-hidden="true" />
        <div className="cafe-header__inner">
          <div className="cafe-header__meta">
            <span className="pure-veg-tag" title="100% Pure Vegetarian">
              <span className="veg-badge__circle" />
              100% PURE VEG
            </span>
            <button
              type="button"
              className="qr-standee-trigger"
              onClick={() => setShowQrModal(true)}
              title="View and print table QR code"
            >
              📷 Table QR Code
            </button>
          </div>

          <h1 className="cafe-header__name">Shree Balaji Snacks &amp; Food Zone</h1>
          <p className="cafe-header__tagline">Tasty Food... Happy Mood...</p>
        </div>
      </header>

      {/* Horizontal Scrollable Category Navigation */}
      <CategoryNav
        activeCat={activeCategory}
        onSelectCat={handleSelectCategory}
      />

      {/* Menu Content Grid */}
      <main className="menu-content">
        {categories.map((cat) => {
          const items = menuItems.filter((item) => item.category === cat)
          const sectionId = `section-${cat.replace(/[^a-zA-Z0-9]/g, '-').toLowerCase()}`

          return (
            <section
              key={cat}
              id={sectionId}
              className="category-section"
            >
              <div className="category-section__header">
                <h2 className="category-section__title">{cat}</h2>
                <span className="category-section__count">{items.length} items</span>
              </div>

              <div className="food-grid">
                {items.map((item) => (
                  <FoodCard key={item.id} item={item} />
                ))}
              </div>
            </section>
          )
        })}
      </main>

      {/* Café Footer */}
      <footer className="cafe-footer">
        <div className="cafe-footer__inner">
          <h2 className="cafe-footer__name">Shree Balaji Snacks &amp; Food Zone</h2>
          <p className="cafe-footer__tagline">"Tasty Food... Happy Mood..."</p>
          <div className="cafe-footer__info">
            <p>Freshly prepared South Indian &amp; Chinese Street Specialties</p>
            <p className="cafe-footer__note">Please order at counter • Pure Veg</p>
          </div>

          <button
            type="button"
            className="footer-qr-btn"
            onClick={() => setShowQrModal(true)}
          >
            🖨️ Get Printable Table QR Code
          </button>
        </div>
      </footer>

      {/* Single Universal Table QR Standee Print/Download Modal */}
      <TableQrModal
        isOpen={showQrModal}
        onClose={() => setShowQrModal(false)}
      />
    </div>
  )
}

export default App
