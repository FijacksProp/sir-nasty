# Sir Nasty Meme - Homepage Template

## 🎯 Overview

This is a premium, Web3-ready homepage template built with Django, Tailwind CSS, and minimal JavaScript. The design features a futuristic neon aesthetic with smooth animations, perfect for a crypto/Web3 meme token project.

## ✨ Features

### Design & UI
- **Dark Mode**: Neon purple/blue gradient theme
- **Animated Background**: Subtle flowing energy effects
- **Particle Click Effects**: Tiny particle drops on user interaction
- **Smooth Animations**: Fade-in, slide-up entrance effects
- **Responsive Design**: Mobile-first approach with hamburger menu
- **Neon Glow Effects**: Hover states and borders with neon highlights

### Sections Included
1. **Sticky Header/Navigation** - Logo, menu links, CTA button, mobile hamburger
2. **Hero Section** - Bold headline, tagline, primary CTAs
3. **Token Market Section** - DexScreener chart embed, token info cards, external links
4. **Ecosystem/Utility** - 6 feature cards explaining project value
5. **Staking Highlight** - Dedicated staking promotion section
6. **Roadmap** - Timeline with 4 phases
7. **Community/Social** - Social links, community stats
8. **Footer** - Complete footer with links and legal

### Technical Stack
- Django Template System
- Tailwind CSS (via CDN)
- Minimal JavaScript (mobile menu, scroll effects, particles)
- Google Fonts (Orbitron + Outfit)
- Performance-optimized CSS animations

---

## 📦 Installation & Setup

### 1. File Structure

Place the files in your Django project:

```
your_django_project/
├── templates/
│   ├── base.html           # Base template
│   └── homepage.html       # Homepage template
├── static/
│   └── images/
│       └── favicon.png     # Add your favicon here
└── your_app/
    └── views.py            # Add view for homepage
```

### 2. Django View Setup

In your `views.py`:

```python
from django.shortcuts import render

def homepage(view):
    context = {
        # Add any dynamic data here
    }
    return render(request, 'homepage.html', context)
```

### 3. URL Configuration

In your `urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    # ... other URLs
]
```

### 4. Static Files Setup

Ensure your `settings.py` has:

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

---

## 🎨 Customization Guide

### Colors

The neon theme uses CSS variables defined in the template. To change colors, update these values in `homepage.html`:

```css
:root {
    --neon-purple: #b026ff;  /* Primary neon purple */
    --neon-blue: #00d4ff;    /* Primary neon blue */
    --dark-bg: #0a0a0f;      /* Dark background */
    --dark-card: #14141f;    /* Card background */
    --text-primary: #ffffff;
    --text-secondary: #a8a8b3;
}
```

### DexScreener Chart

Replace the placeholder in the chart section (line ~407):

```html
<iframe 
    src="https://dexscreener.com/solana/YOUR_TOKEN_ADDRESS?embed=1&theme=dark&trades=0&info=0"
    title="DexScreener Chart">
</iframe>
```

Replace `YOUR_TOKEN_ADDRESS` with your actual Solana token address.

### External Links

Update these links throughout the template:
- Social media URLs (Twitter, Telegram, Discord)
- DEX platform links (Pump.fun, DexScreener, GeckoTerminal, Raydium)
- Staking platform URL: `https://stake.sirnastymeme.com`

### Logo

Update the logo section in the header (line ~232):

```html
<div class="w-12 h-12 rounded-lg bg-gradient-to-br from-purple-600 to-blue-500 flex items-center justify-center">
    <span class="text-2xl font-bold">SN</span>
</div>
```

Replace with:
```html
<img src="{% static 'images/logo.png' %}" alt="Sir Nasty Meme" class="w-12 h-12">
```

### Community Stats

Update the stats in the Community section (line ~775):

```html
<div class="text-4xl font-bold gradient-text mb-2">10K+</div>
<p class="text-gray-400">Community Members</p>
```

### Roadmap Phases

Customize roadmap content starting at line ~660. Each phase has:
- Phase label
- Title
- List of milestones
- Status indicators (✅ complete, 🔄 in progress, 📅 planned, 🔮 future)

---

## ⚙️ JavaScript Features (Optional)

All JavaScript is contained in the `{% block extra_js %}` section and is **optional**. The site works without it, but includes:

### 1. Mobile Menu Toggle
Handles hamburger menu on mobile devices.

### 2. Sticky Header
Adds backdrop blur when scrolling past 100px.

### 3. Particle Effects
Creates 3-5 small particles on every click. To disable, remove the click event listener:

```javascript
// Comment out or remove these lines:
// document.addEventListener('click', function(e) {
//     createParticles(e.clientX, e.clientY);
// });
```

### 4. Smooth Scroll
Enables smooth scrolling for anchor links.

**To disable all JavaScript**, simply remove or don't include the `{% block extra_js %}` section.

---

## 🎭 Animation Details

### Entrance Animations

Elements use CSS classes for staggered entrance:
- `.fade-in` - Fade in opacity
- `.slide-up` - Slide up with fade
- `.delay-100`, `.delay-200`, etc. - Stagger timing

### Background Animation

The animated background uses CSS `@keyframes` for smooth floating motion. To adjust speed:

```css
.animated-bg::before {
    animation: float 25s ease-in-out infinite;  /* Change 25s */
}
```

### Hover Effects

Cards and buttons have hover states with:
- `translateY(-2px)` - Subtle lift
- Neon glow shadows
- Smooth 0.3s transitions

---

## 📱 Responsive Breakpoints

Tailwind CSS breakpoints used:
- `sm:` - 640px and up
- `md:` - 768px and up
- `lg:` - 1024px and up

Mobile menu activates below `md` (768px).

---

## 🔧 Production Checklist

Before deploying:

- [ ] Replace placeholder token address in DexScreener embed
- [ ] Update all social media links
- [ ] Add actual logo image
- [ ] Update community stats with real numbers
- [ ] Configure Django static files for production
- [ ] Add actual whitepaper and documentation links
- [ ] Update legal pages (Terms, Privacy, etc.)
- [ ] Add Google Analytics or tracking (if needed)
- [ ] Test on multiple devices and browsers
- [ ] Optimize images and assets
- [ ] Set up proper SEO meta tags

---

## 🚀 Performance Notes

### CSS Animations
All animations use CSS for best performance. GPU-accelerated transforms (`translateY`, `scale`) are prioritized.

### Tailwind CDN
For production, consider:
1. Installing Tailwind via npm
2. Building a custom CSS file
3. Purging unused styles

This reduces file size from ~3MB to ~10KB.

### Particle Effects
Particles auto-remove after 1 second to prevent memory leaks. Limited to 3-5 per click for performance.

---

## 🎨 Typography

**Display Font**: Orbitron (headings, logo)  
**Body Font**: Outfit (paragraphs, UI text)

Both loaded from Google Fonts in `base.html`.

To change fonts, update the Google Fonts link and CSS in `base.html`:

```html
<link href="https://fonts.googleapis.com/css2?family=YOUR_FONT&display=swap" rel="stylesheet">
```

---

## 🔗 External Dependencies

- **Tailwind CSS**: CDN loaded in `base.html`
- **Google Fonts**: Orbitron + Outfit
- **DexScreener**: Embedded chart iframe

No other external libraries required!

---

## 💡 Customization Tips

### Adding New Sections

1. Copy an existing section structure
2. Wrap in `<section>` with appropriate classes
3. Add animation classes: `slide-up delay-X00`
4. Use `.neon-border` for cards
5. Use `.gradient-text` for highlighted text

### Creating More Cards

Template for feature cards:

```html
<div class="neon-border rounded-2xl p-8 feature-card">
    <div class="w-16 h-16 rounded-full bg-gradient-to-br from-purple-600 to-blue-500 flex items-center justify-center mb-6">
        <span class="text-3xl">🎯</span>
    </div>
    <h3 class="text-2xl font-bold mb-4 text-white">Title</h3>
    <p class="text-gray-400">Description text</p>
</div>
```

### Gradient Buttons

```html
<a href="#" class="cta-button px-8 py-4 rounded-lg font-semibold text-white relative z-10">
    Button Text
</a>
```

---

## 🐛 Troubleshooting

### Styles Not Loading
- Check that Tailwind CDN is loading in `base.html`
- Verify Django static files configuration
- Clear browser cache

### Animations Not Working
- Ensure CSS in `{% block extra_css %}` is included
- Check browser console for errors
- Test in different browsers

### Mobile Menu Not Opening
- Verify JavaScript is loading
- Check element IDs match in HTML and JS
- Test on actual mobile device, not just browser resize

---

## 📄 License

This template is for Sir Nasty Meme LLC. All rights reserved.

---

## 🤝 Support

For integration support or customization requests, contact the development team.

---

**Built with 💜 for the Sir Nasty Meme community**
