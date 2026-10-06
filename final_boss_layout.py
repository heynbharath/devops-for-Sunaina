import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Add Mobile Header and modify Sidebar HTML
mobile_header = """
<div class="mobile-header">
  <div class="logo">SUNAINA'S <span>LAB</span> <span class="heart">❤️</span></div>
  <button class="hamburger" onclick="document.getElementById('sidebar').classList.add('open')">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--cyan)" stroke-width="2" stroke-linecap="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
  </button>
</div>
"""

# Find the start of the app div
content = content.replace('<div class="app">', '<div class="app">\n' + mobile_header)

# Modify sidebar to include an ID and a close button
sidebar_start = '<aside class="sidebar">'
new_sidebar_start = """<aside class="sidebar" id="sidebar">
  <button class="close-btn" onclick="document.getElementById('sidebar').classList.remove('open')">✕</button>"""
content = content.replace(sidebar_start, new_sidebar_start)

# Make the nav buttons close the sidebar on click
content = content.replace("onclick=\"go(", "onclick=\"document.getElementById('sidebar').classList.remove('open'); go(")

# 2. Re-write the Media Queries completely. Remove old messy queries.
# First, strip out ALL existing media queries.
# Since regex matching blocks of CSS is tricky with nested braces, I'll use a safer approach:
# Just delete everything after `@media` and replace it.
css_split = content.split('@media')
# The first part is the base CSS. We keep that.
base_css = css_split[0]

# Now, add the perfect, industry-standard responsive CSS
perfect_responsive_css = """
/* Desktop Base Overrides */
.mobile-header { display: none; }
.close-btn { display: none; }

/* Tablet & Mobile (Industry Standard Drawer Menu) */
@media(max-width: 950px) {
  .mobile-header {
      display: flex; position: fixed; top: 0; left: 0; right: 0; height: 75px;
      background: rgba(20,5,15,0.85); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px);
      align-items: center; justify-content: space-between; padding: 0 24px;
      z-index: 900; border-bottom: 1px solid rgba(255,126,179,0.15);
      box-shadow: 0 10px 30px rgba(0,0,0,0.5);
  }
  .hamburger { background: transparent; border: none; padding: 10px; cursor: pointer; display: flex; align-items: center; justify-content: center; border-radius: 12px; }
  .hamburger:hover { background: rgba(255,126,179,0.1); }
  
  .sidebar {
      position: fixed; top: 0; left: -110%; width: 300px; height: 100vh;
      background: rgba(15,5,12,0.98) !important; backdrop-filter: blur(30px); -webkit-backdrop-filter: blur(30px);
      transition: left 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      z-index: 1000; display: block !important; border-right: 1px solid rgba(255,126,179,0.2);
      box-shadow: 20px 0 50px rgba(0,0,0,0.7);
  }
  .sidebar.open { left: 0; }
  
  .close-btn {
      display: block; position: absolute; top: 20px; right: 20px;
      background: rgba(255,255,255,0.1); border: none; color: white;
      width: 40px; height: 40px; border-radius: 50%; font-size: 18px;
      cursor: pointer; display: flex; align-items: center; justify-content: center;
  }
  
  /* Reset nav styling from any previous mobile hacks */
  .nav { display: grid !important; flex-direction: column !important; gap: 8px !important; overflow: visible !important; }
  .nav button { padding: 14px 20px !important; font-size: 16px !important; border-radius: 14px !important; text-align: left !important; background: transparent !important; border: 1px solid transparent !important; }
  .nav button:hover, .nav button.active { background: rgba(255,126,179,0.15) !important; color: #fff !important; transform: translateX(5px) !important; border-color: rgba(255,126,179,0.3) !important; }
  .logo { font-size: 20px !important; margin-bottom: 30px !important; text-align: left !important; }
  .logo br { display: block !important; }
  .logo span:last-child { display: inline !important; }
  .tag { display: block !important; }
  
  .main { margin-left: 0 !important; width: 100% !important; padding: 100px 20px 60px !important; }
  
  /* Responsive Grids */
  .grid, .grid2, .compare, .topic-list { grid-template-columns: 1fr; gap: 16px; }
  .hero-content { padding: 30px 24px !important; }
  h1 { font-size: 40px !important; line-height: 1.1 !important; margin-bottom: 16px !important; }
  
  /* Fix Connect the Dots for Mobile */
  .connect-step { flex-direction: column !important; align-items: flex-start !important; gap: 12px !important; }
  .connect-step > div:first-child { width: 36px !important; height: 36px !important; font-size: 16px !important; }
  
  .modalbox { width: 95% !important; padding: 24px !important; border-radius: 20px !important; margin: 10px; }
  
  /* Hide the top bar buttons on mobile as they clutter the view */
  .top { display: none !important; }
}

@media(max-width: 500px) {
  h1 { font-size: 34px !important; }
  .hero-content { padding: 24px 20px !important; }
  .lead { font-size: 16px !important; line-height: 1.6 !important; }
  .main { padding-top: 95px !important; padding-left: 16px !important; padding-right: 16px !important; }
}
"""

content = base_css + perfect_responsive_css + "\n</style>\n" + content.split('</style>')[1]

# Write back
with open('index.html', 'w') as f:
    f.write(content)

print("Final boss layout executed.")
