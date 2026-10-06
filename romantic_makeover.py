import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Update the CSS variables and Background
new_vars = """
:root{
  --bg:#12050f;--panel:rgba(30,10,25,0.7);--card:rgba(40,15,35,0.6);--text:#fff0f5;--muted:#ffb6c1;
  --cyan:#ff7eb3;--blue:#ffdf99;--green:#a1c4fd;--yellow:#fbc2eb;--red:#ff4e50;--purple:#c2e9fb;
  --line:rgba(255,118,179,0.25);--shadow:0 18px 50px rgba(0,0,0,.6);--radius:20px;
}
"""
content = re.sub(r':root\s*\{.*?\}', new_vars.strip(), content, flags=re.DOTALL)

# 2. Update the animated background to a romantic twilight / rose gold gradient
new_bg = """
body {
  margin: 0;
  background: linear-gradient(-45deg, #2a0845, #6441A5, #ff0844, #ffb199, #12050f);
  background-size: 400% 400%;
  animation: mesh 25s ease infinite;
  color: var(--text);
  font: 16px/1.7 'Outfit', ui-sans-serif, system-ui, sans-serif;
  letter-spacing: 0.3px;
}
"""
content = re.sub(r'body\s*\{.*?letter-spacing: 0\.3px;\s*\}', new_bg.strip(), content, flags=re.DOTALL)

# 3. Add pulsing heart CSS and change scrollbar to pink
romantic_css = """
::-webkit-scrollbar-thumb { background: rgba(255,126,179,0.5); border-radius: 10px; }
::-webkit-scrollbar-thumb:hover { background: rgba(255,126,179,0.8); }

@keyframes heartbeat {
  0% { transform: scale(1); }
  14% { transform: scale(1.3); }
  28% { transform: scale(1); }
  42% { transform: scale(1.3); }
  70% { transform: scale(1); }
}
.heart { display: inline-block; animation: heartbeat 2s infinite; color: #ff0844; }

.particle { position: absolute; border-radius: 50%; background: radial-gradient(circle, #ff7eb3, transparent); opacity: 0.4; animation: floatUp linear infinite; filter: blur(2px); }

.hero::before { content: ''; position: absolute; top: -50%; left: -50%; width: 200%; height: 200%; background: conic-gradient(transparent, rgba(255,126,179,0.4), transparent 30%); animation: rotate 12s linear infinite; z-index: -1; }
h1 { font-weight: 900; background: linear-gradient(135deg, #fff0f5, #ffb199); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
"""
content = content.replace("::-webkit-scrollbar-thumb { background: rgba(0,240,255,0.4); border-radius: 10px; }", "")
content = content.replace("::-webkit-scrollbar-thumb:hover { background: rgba(0,240,255,0.7); }", "")
content = content.replace(".particle { position: absolute; border-radius: 50%; background: white; opacity: 0.3; animation: floatUp linear infinite; }", "")
content = content.replace(".hero::before { content: ''; position: absolute; top: -50%; left: -50%; width: 200%; height: 200%; background: conic-gradient(transparent, rgba(0,240,255,0.3), transparent 30%); animation: rotate 10s linear infinite; z-index: -1; }", "")
content = content.replace("h1 { font-weight: 900; background: linear-gradient(135deg, #fff, #a5b4fc); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }", "")

content = content.replace("</style>", romantic_css + "\n</style>")

# 4. Update the Sidebar Logo
old_logo = """<div class="logo">DEV<span>OPS</span> LAB<br><span style="font-size:12px;color:var(--cyan);font-weight:normal">for Sunaina Mohapatra 👩🏻‍💻</span></div>"""
new_logo = """<div class="logo" style="text-shadow: 0 0 15px rgba(255,126,179,0.8);">SUNAINA'S <span>LAB</span> <span class="heart">❤️</span><br><span style="font-size:12px;color:var(--muted);font-weight:normal;letter-spacing:1px;">BUILT WITH LOVE BY BHARATH</span></div>"""
content = content.replace(old_logo, new_logo)

# 5. Update the Hero Content to be deeply romantic
old_hero = """<div class="hero">
  <div class="hero-content">
      <div class="kicker">DevOps + Git • MSE-1</div>
      <h1>You've got this, <span style="color:var(--cyan); text-shadow: 0 0 20px var(--cyan);" class="typewriter">Sunaina! 🚀</span></h1>
      <p class="lead">Good evening! Tomorrow is your MSE-1 for DevOps. Don't stress. This interactive lab is designed just for you to revise all 40 topics easily. Follow the story, click the moving parts, and crush that exam!</p>
      <div class="actions"><button class="btn primary" onclick="go('story')">Start the story →</button><button class="btn" onclick="go('quiz')">Test me</button></div>
  </div>
</div>"""

new_hero = """<div class="hero">
  <div class="hero-content" style="background: rgba(30,10,25,0.7); border: 1px solid rgba(255,126,179,0.3);">
      <div class="kicker" style="color: #ffdf99;">A SPECIAL GIFT FOR YOUR MSE-1</div>
      <h1 style="font-size: clamp(40px, 6vw, 75px); letter-spacing: -1px;">I built this just for you, <br><span style="color:var(--cyan); text-shadow: 0 0 30px rgba(255,126,179,0.6);">Sunaina.</span> <span class="heart" style="font-size: 50px;">💖</span></h1>
      <p class="lead" style="color: #ffb6c1; font-size: 22px; font-weight: 300;">I know how hard you've been working. So instead of you struggling with boring PDFs, I coded this entire interactive platform from scratch so you can study effortlessly tonight. You are brilliant, and you are going to absolutely crush this exam tomorrow. I believe in you.</p>
      <div class="actions"><button class="btn primary" style="background: linear-gradient(135deg, #ff0844, #ffb199); box-shadow: 0 8px 30px rgba(255,8,68,0.5); font-size: 18px; padding: 14px 28px; border-radius: 99px;" onclick="go('story')">Let's study together ✨</button></div>
  </div>
</div>"""
content = content.replace(old_hero, new_hero)

# 6. Change the primary button colors across the site
content = content.replace(".btn.primary { background: linear-gradient(135deg, #ff007a, #7a00ff); border-color: transparent; box-shadow: 0 5px 20px rgba(122,0,255,0.5); }", ".btn.primary { background: linear-gradient(135deg, #ff0844, #ffb199); border-color: transparent; box-shadow: 0 5px 20px rgba(255,8,68,0.5); }")
content = content.replace(".btn.primary:hover { background: linear-gradient(135deg, #ff2a8e, #8f2aff); box-shadow: 0 8px 25px rgba(255,0,122,0.6); }", ".btn.primary:hover { background: linear-gradient(135deg, #ff4e50, #f9d423); box-shadow: 0 8px 25px rgba(255,78,80,0.6); }")

# 7. Update footer text to show his effort
old_footer = "<footer>Built specially for Sunaina Mohapatra's MSE-1 Exam Prep ❤️ • You are going to ace it!</footer>"
new_footer = "<footer style=\"color: #ffb6c1; font-weight: 300; letter-spacing: 1px;\">Hand-coded with endless love for Sunaina ❤️ • Good luck on your exam tomorrow, beautiful!</footer>"
content = content.replace(old_footer, new_footer)

with open('index.html', 'w') as f:
    f.write(content)

print("Romantic makeover complete.")
