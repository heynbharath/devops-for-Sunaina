import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Update Logo (keep the heart but make text subtle)
# Old: <div class="logo" style="text-shadow: 0 0 15px rgba(255,126,179,0.8);">SUNAINA'S <span>LAB</span> <span class="heart">❤️</span><br><span style="font-size:12px;color:var(--muted);font-weight:normal;letter-spacing:1px;">BUILT WITH LOVE BY N BHARATH</span></div>
new_logo = """<div class="logo" style="text-shadow: 0 0 15px rgba(255,126,179,0.8);">SUNAINA'S <span>LAB</span> <span class="heart">❤️</span><br><span style="font-size:12px;color:var(--muted);font-weight:normal;letter-spacing:1px;">BY N BHARATH</span></div>"""
content = re.sub(r'<div class="logo".*?</div>', new_logo, content, flags=re.DOTALL)

# 2. Update Hero text to be supportive but subtle (not "I built this just for you I love you")
old_hero_search = r'<div class="hero">.*?</div>\s*</div>'
new_hero = """<div class="hero">
  <div class="hero-content" style="background: rgba(30,10,25,0.7); border: 1px solid rgba(255,126,179,0.3);">
      <div class="kicker" style="color: #ffdf99;">DEVOPS + GIT • MSE-1 PREP</div>
      <h1 style="font-size: clamp(40px, 6vw, 75px); letter-spacing: -1px;">You've got this,<br><span style="color:var(--cyan); text-shadow: 0 0 30px rgba(255,126,179,0.6);">Sunaina.</span> 🚀</h1>
      <p class="lead" style="color: #ffb6c1; font-size: 22px; font-weight: 300;">Tomorrow is your MSE-1 for DevOps. Don't stress. This interactive lab is designed to help you revise all 40 topics effortlessly tonight. Follow the story, connect the concepts, and absolutely crush that exam!</p>
      <div class="actions"><button class="btn primary" style="background: linear-gradient(135deg, #ff0844, #ffb199); box-shadow: 0 8px 30px rgba(255,8,68,0.5); font-size: 18px; padding: 14px 28px; border-radius: 99px;" onclick="go('story')">Start the revision ✨</button></div>
  </div>
</div>"""
content = re.sub(old_hero_search, new_hero, content, flags=re.DOTALL)

# 3. Update Footer
old_footer_search = r'<footer style=".*?">.*?</footer>'
new_footer = """<footer style="color: #ffb6c1; font-weight: 300; letter-spacing: 1px;">Designed for Sunaina Mohapatra's MSE-1 • You're going to ace it! ✨</footer>"""
content = re.sub(old_footer_search, new_footer, content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(content)

print("Text made subtle.")
