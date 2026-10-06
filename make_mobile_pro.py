import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Inject Open Graph Tags
og_tags = """
<meta property="og:title" content="Sunaina's DevOps & Git Lab ❤️">
<meta property="og:description" content="A custom-built interactive study guide to help you crush your MSE-1 exam. I believe in you!">
<meta property="og:type" content="website">
<meta property="og:url" content="https://heynbharath.github.io/devops-for-Sunaina/">
<meta property="og:image" content="https://images.unsplash.com/photo-1550684848-fac1c5b4e853?q=80&w=1200&auto=format&fit=crop">
<meta name="twitter:card" content="summary_large_image">
"""
content = content.replace("<meta name=\"description\"", og_tags + "\n<meta name=\"description\"")

# 2. Add Mobile CSS Rules
mobile_css = """
@media(max-width:600px){
  .main { margin-left: 0 !important; width: 100% !important; padding: 100px 16px 24px !important; }
  .sidebar { width: 100% !important; height: 70px !important; bottom: auto !important; padding: 10px 16px !important; border-right: none !important; border-bottom: 1px solid var(--line); display: flex; align-items: center; justify-content: space-between; flex-direction: row; }
  .logo { font-size: 16px !important; margin: 0 !important; }
  .logo span.heart { font-size: 16px !important; }
  .logo br { display: none; }
  .logo span:last-child { display: none; }
  .nav { display: flex !important; flex-direction: row !important; gap: 4px !important; overflow-x: auto; padding-bottom: 5px; }
  .nav button { padding: 6px 12px !important; font-size: 12px !important; white-space: nowrap; }
  .nav button span { display: inline !important; font-size: 12px !important; }
  
  .connect-step { flex-direction: column !important; align-items: flex-start !important; gap: 10px !important; }
  .connect-step > div:first-child { width: 30px !important; height: 30px !important; font-size: 14px !important; }
  
  .modalbox { padding: 20px !important; border-radius: 16px !important; }
  .hero-content { padding: 30px 20px !important; }
  h1 { font-size: 32px !important; }
}
"""

content = content.replace("</style>", mobile_css + "\n</style>")

# 3. Add class to Connect steps to hook into mobile CSS
content = content.replace("display: flex; gap: 20px; align-items: stretch;", "display: flex; gap: 20px; align-items: stretch;\" class=\"connect-step")

# 4. Remove the extra closing </div> I deleted earlier (just in case I missed it)
# I already fixed it manually.

with open('index.html', 'w') as f:
    f.write(content)

print("Mobile and OG tags injected.")
