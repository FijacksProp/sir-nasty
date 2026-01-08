# CSS Customization Reference

## 🎨 Color Schemes

### Current Neon Theme (Purple/Blue)
```css
:root {
    --neon-purple: #b026ff;
    --neon-blue: #00d4ff;
    --dark-bg: #0a0a0f;
    --dark-card: #14141f;
    --text-primary: #ffffff;
    --text-secondary: #a8a8b3;
}
```

### Alternative Theme Ideas

#### Green/Cyan (Matrix Style)
```css
:root {
    --neon-purple: #00ff41;  /* Neon green */
    --neon-blue: #00ffff;    /* Cyan */
    --dark-bg: #0d0d0d;
    --dark-card: #1a1a1a;
}
```

#### Red/Orange (Fire)
```css
:root {
    --neon-purple: #ff0844;  /* Hot pink/red */
    --neon-blue: #ffb700;    /* Orange */
    --dark-bg: #0a0a0f;
    --dark-card: #14141f;
}
```

#### Pink/Purple (Vaporwave)
```css
:root {
    --neon-purple: #ff006e;  /* Hot pink */
    --neon-blue: #8338ec;    /* Purple */
    --dark-bg: #0a0114;
    --dark-card: #1a0a28;
}
```

---

## ✨ Animation Speeds

### Background Animation
```css
/* Current: 25-30 seconds (very slow) */
.animated-bg::before {
    animation: float 25s ease-in-out infinite;
}

/* Faster: 15 seconds */
animation: float 15s ease-in-out infinite;

/* Slower: 40 seconds */
animation: float 40s ease-in-out infinite;
```

### Entrance Animations
```css
/* Current: 0.8 seconds */
.fade-in {
    animation: fadeIn 0.8s ease-out forwards;
}

/* Faster: 0.5 seconds */
animation: fadeIn 0.5s ease-out forwards;

/* Slower: 1.2 seconds */
animation: fadeIn 1.2s ease-out forwards;
```

### Stagger Delays
```css
/* Current delays */
.delay-100 { animation-delay: 0.1s; }
.delay-200 { animation-delay: 0.2s; }
.delay-300 { animation-delay: 0.3s; }

/* Faster (reduce by half) */
.delay-100 { animation-delay: 0.05s; }
.delay-200 { animation-delay: 0.1s; }
.delay-300 { animation-delay: 0.15s; }
```

---

## 🌟 Glow Intensity

### Text Glow
```css
/* Current intensity */
.neon-text {
    text-shadow: 
        0 0 10px var(--neon-purple),
        0 0 20px var(--neon-purple),
        0 0 30px var(--neon-purple);
}

/* Stronger glow */
text-shadow: 
    0 0 15px var(--neon-purple),
    0 0 30px var(--neon-purple),
    0 0 45px var(--neon-purple),
    0 0 60px var(--neon-purple);

/* Subtle glow */
text-shadow: 
    0 0 5px var(--neon-purple),
    0 0 10px var(--neon-purple);
```

### Card Border Glow (on hover)
```css
/* Current */
.neon-border:hover {
    box-shadow: 
        0 0 20px rgba(176, 38, 255, 0.3),
        0 0 40px rgba(0, 212, 255, 0.2);
}

/* Stronger */
box-shadow: 
    0 0 30px rgba(176, 38, 255, 0.5),
    0 0 60px rgba(0, 212, 255, 0.4),
    0 0 90px rgba(176, 38, 255, 0.2);

/* Subtle */
box-shadow: 
    0 0 10px rgba(176, 38, 255, 0.2),
    0 0 20px rgba(0, 212, 255, 0.1);
```

---

## 🎯 Background Effects

### Blur Amount
```css
/* Current: 80px blur */
filter: blur(80px);

/* More defined: 40px blur */
filter: blur(40px);

/* More abstract: 120px blur */
filter: blur(120px);
```

### Background Opacity
```css
/* Current: 15% visible */
.animated-bg {
    opacity: 0.15;
}

/* More visible: 25% */
opacity: 0.25;

/* Subtle: 8% */
opacity: 0.08;
```

### Background Size
```css
/* Current sizes */
.animated-bg::before {
    width: 500px;
    height: 500px;
}

.animated-bg::after {
    width: 600px;
    height: 600px;
}

/* Larger presence */
width: 800px;
height: 800px;

/* Smaller, more focused */
width: 300px;
height: 300px;
```

---

## 🔘 Button Effects

### Button Hover Lift
```css
/* Current: 2px lift */
.cta-button:hover {
    transform: translateY(-2px);
}

/* More dramatic: 5px */
transform: translateY(-5px);

/* Subtle: 1px */
transform: translateY(-1px);
```

### Button Ripple Effect
```css
/* Current ripple size */
.cta-button:hover::before {
    width: 300px;
    height: 300px;
}

/* Larger ripple */
width: 500px;
height: 500px;

/* Smaller ripple */
width: 150px;
height: 150px;
```

---

## 💫 Particle Customization

### Particle Count
```javascript
// Current: 3-5 particles
const particleCount = Math.floor(Math.random() * 3) + 3;

// More particles: 5-10
const particleCount = Math.floor(Math.random() * 6) + 5;

// Fewer particles: 2-3
const particleCount = Math.floor(Math.random() * 2) + 2;
```

### Particle Size
```css
/* Current: 4px */
.particle {
    width: 4px;
    height: 4px;
}

/* Larger: 6px */
width: 6px;
height: 6px;

/* Smaller: 2px */
width: 2px;
height: 2px;
```

### Particle Fall Distance
```css
/* Current: 50px fall */
@keyframes particleFall {
    100% {
        transform: translateY(50px) scale(0);
    }
}

/* Longer fall: 100px */
transform: translateY(100px) scale(0);

/* Shorter fall: 30px */
transform: translateY(30px) scale(0);
```

---

## 📐 Spacing & Layout

### Section Padding
```html
<!-- Current padding -->
<section class="py-16">  <!-- 64px top/bottom -->

<!-- More spacing -->
<section class="py-24">  <!-- 96px top/bottom -->

<!-- Less spacing -->
<section class="py-12">  <!-- 48px top/bottom -->
```

### Container Width
```html
<!-- Current max width -->
<div class="max-w-6xl">  <!-- 1152px -->

<!-- Wider -->
<div class="max-w-7xl">  <!-- 1280px -->

<!-- Narrower -->
<div class="max-w-4xl">  <!-- 896px -->
```

---

## 🎨 Border Radius

### Card Corners
```html
<!-- Current -->
<div class="rounded-2xl">  <!-- 16px radius -->

<!-- More rounded -->
<div class="rounded-3xl">  <!-- 24px radius -->

<!-- Less rounded -->
<div class="rounded-xl">   <!-- 12px radius -->

<!-- Sharp corners -->
<div class="rounded-lg">   <!-- 8px radius -->
```

---

## 📝 Typography Adjustments

### Font Weights
```html
<!-- Headers -->
<h1 class="font-bold">    <!-- 700 -->
<h1 class="font-extrabold"> <!-- 800 -->
<h1 class="font-black">    <!-- 900 -->

<!-- Body text -->
<p class="font-normal">    <!-- 400 -->
<p class="font-medium">    <!-- 500 -->
<p class="font-semibold">  <!-- 600 -->
```

### Font Sizes
```html
<!-- Hero title current: text-7xl (72px) -->
<h1 class="text-7xl">

<!-- Larger: text-8xl (96px) -->
<h1 class="text-8xl">

<!-- Smaller: text-6xl (60px) -->
<h1 class="text-6xl">
```

---

## 🎬 Disable Features

### Remove Background Animation
```css
/* Comment out or delete this entire block */
.animated-bg::before,
.animated-bg::after {
    /* ... */
}
```

### Remove All Animations
```css
/* Add this at the top of the style block */
* {
    animation: none !important;
    transition: none !important;
}
```

### Simplify Hover Effects
```css
/* Replace complex hover with simple color change */
.neon-border:hover {
    border-color: var(--neon-purple);
    /* Remove: box-shadow, transform */
}
```

---

## 🔍 Quick Find & Replace

### Change All Purple
Find: `#b026ff` or `var(--neon-purple)`  
Replace with your color

### Change All Blue
Find: `#00d4ff` or `var(--neon-blue)`  
Replace with your color

### Change Animation Duration
Find: `0.8s ease-out`  
Replace with: `0.5s ease-out` (faster) or `1.2s ease-out` (slower)

---

## 💡 Pro Tips

1. **Test color changes** using browser DevTools first
2. **Keep contrast ratio** above 4.5:1 for accessibility
3. **Match animation speeds** - fast entrance + fast hover = cohesive
4. **Less is more** with particle effects on mobile
5. **Preview on actual devices** - animations behave differently

---

## 🎯 Most Impactful Changes

If you only change 3 things, change:
1. **Colors** (lines 16-21 in homepage.html)
2. **Animation speed** (lines ~94, ~122)
3. **Glow intensity** (lines ~56, ~76)

These give the biggest visual impact with minimal effort.
