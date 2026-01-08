# Quick Integration Checklist

## 🚀 5-Minute Setup
 ac
### Step 1: Place Files
```
your_django_project/
├── templates/
│   ├── base.html          ← Place here
│   └── homepage.html      ← Place here
```

### Step 2: Create View (views.py)
```python
def homepage(request):
    return render(request, 'homepage.html')
```

### Step 3: Add URL (urls.py)
```python
path('', views.homepage, name='homepage'),
```

### Step 4: Run Server
```bash
python manage.py runserver
```

---

## ⚡ Critical Customizations

### 1. DexScreener Chart (Line ~407 in homepage.html)
```html
<!-- REPLACE THIS: -->
src="https://dexscreener.com/solana/YOUR_TOKEN_ADDRESS?embed=1&theme=dark"

<!-- WITH YOUR ACTUAL TOKEN ADDRESS -->
```

### 2. Social Links
Update these throughout homepage.html:
- Line ~741: Twitter URL
- Line ~748: Telegram URL  
- Line ~755: Discord URL

### 3. Staking URL
- Line ~248, ~371, ~654: Update `https://stake.sirnastymeme.com`

---

## 🎨 Styling Quick Reference

### Colors (CSS Variables)
```css
--neon-purple: #b026ff;
--neon-blue: #00d4ff;
--dark-bg: #0a0a0f;
```

### Key CSS Classes
- `.gradient-text` - Purple to blue gradient
- `.neon-border` - Glowing border on hover
- `.cta-button` - Gradient button with effects
- `.slide-up` - Entrance animation
- `.fade-in` - Fade animation

---

## 🔧 Optional Customizations

### Disable Particle Effects
Comment out lines ~876-878 in homepage.html:
```javascript
// document.addEventListener('click', function(e) {
//     createParticles(e.clientX, e.clientY);
// });
```

### Disable All JavaScript
Remove the entire `{% block extra_js %}` section (lines ~853-925).

### Change Logo
Replace lines ~232-235 with:
```html
<img src="{% static 'images/logo.png' %}" alt="Logo" class="w-12 h-12">
```

---

## 📱 Testing Checklist

- [ ] Desktop view (1920px)
- [ ] Tablet view (768px)
- [ ] Mobile view (375px)
- [ ] Mobile menu works
- [ ] All links work
- [ ] Scroll animations trigger
- [ ] Hover effects work

---

## 🐛 Common Issues

### Issue: Tailwind styles not working
**Fix**: Ensure `<script src="https://cdn.tailwindcss.com"></script>` is in base.html

### Issue: Animations not showing
**Fix**: Check that CSS in `{% block extra_css %}` is loaded

### Issue: Mobile menu not opening
**Fix**: Verify JavaScript is enabled and element IDs match

---

## 📞 Need Help?

Refer to the comprehensive README.md for detailed documentation.

Key sections:
- Full customization guide
- JavaScript documentation
- Responsive design details
- Production deployment checklist
