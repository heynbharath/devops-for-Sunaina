import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Add Google Fonts and VanillaTilt
fonts_and_libs = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800;900&family=Space+Grotesk:wght@400;700&display=swap" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/vanilla-tilt/1.8.0/vanilla-tilt.min.js"></script>
</head>
"""
content = content.replace("</head>", fonts_and_libs)

# 2. Update CSS font families and add custom scrollbar, floating animations
new_css_updates = """
  font: 16px/1.7 'Outfit', ui-sans-serif, system-ui, sans-serif;
"""
content = content.replace("font: 16px/1.7 Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, \"Segoe UI\", sans-serif;", new_css_updates)

# Update h1, h2, h3 to use Outfit if needed (it will inherit). Let's make code and kickers use Space Grotesk.
custom_css = """
::-webkit-scrollbar { width: 10px; }
::-webkit-scrollbar-track { background: rgba(0,0,0,0.3); }
::-webkit-scrollbar-thumb { background: rgba(0,240,255,0.4); border-radius: 10px; }
::-webkit-scrollbar-thumb:hover { background: rgba(0,240,255,0.7); }

.kicker, .badge, th { font-family: 'Space Grotesk', monospace; letter-spacing: 2px; }
.command { font-family: 'Space Grotesk', monospace; font-size: 16px; }

h1 { font-weight: 900; background: linear-gradient(135deg, #fff, #a5b4fc); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.hero { position: relative; border-radius: 32px; overflow: hidden; box-shadow: 0 30px 60px rgba(0,0,0,0.5), inset 0 0 0 1px rgba(255,255,255,0.2); }
.hero::before { content: ''; position: absolute; top: -50%; left: -50%; width: 200%; height: 200%; background: conic-gradient(transparent, rgba(0,240,255,0.3), transparent 30%); animation: rotate 10s linear infinite; z-index: -1; }
@keyframes rotate { 100% { transform: rotate(360deg); } }
.hero-content { background: rgba(10,15,30,0.85); backdrop-filter: blur(40px); padding: 50px; border-radius: 32px; height: 100%; width: 100%; }

.card { transform-style: preserve-3d; transform: perspective(1000px); }
.card > * { transform: translateZ(30px); }

/* Floating particles */
.particles { position: fixed; inset: 0; pointer-events: none; z-index: 0; overflow: hidden; }
.particle { position: absolute; border-radius: 50%; background: white; opacity: 0.3; animation: floatUp linear infinite; }
@keyframes floatUp { 
    0% { transform: translateY(100vh) scale(0); opacity: 0; }
    50% { opacity: 0.5; }
    100% { transform: translateY(-100px) scale(1); opacity: 0; }
}

"""
content = content.replace("</style>", custom_css + "</style>")

# 3. Update Hero section HTML to wrap content in .hero-content for the glowing border effect
old_hero = """<div class="hero">
  <div class="kicker">DevOps + Git • MSE-1</div>
  <h1>You've got this, <span style="color:var(--cyan)">Sunaina! 🚀</span></h1>
  <p class="lead">Good evening! Tomorrow is your MSE-1 for DevOps. Don't stress. This interactive lab is designed just for you to revise all 40 topics easily. Follow the story, click the moving parts, and crush that exam!</p>
  <div class="actions"><button class="btn primary" onclick="go('story')">Start the story →</button><button class="btn" onclick="go('quiz')">Test me</button></div>
</div>"""

new_hero = """<div class="hero">
  <div class="hero-content">
      <div class="kicker">DevOps + Git • MSE-1</div>
      <h1>You've got this, <span style="color:var(--cyan); text-shadow: 0 0 20px var(--cyan);" class="typewriter">Sunaina! 🚀</span></h1>
      <p class="lead">Good evening! Tomorrow is your MSE-1 for DevOps. Don't stress. This interactive lab is designed just for you to revise all 40 topics easily. Follow the story, click the moving parts, and crush that exam!</p>
      <div class="actions"><button class="btn primary" onclick="go('story')">Start the story →</button><button class="btn" onclick="go('quiz')">Test me</button></div>
  </div>
</div>"""
content = content.replace(old_hero, new_hero)

# 4. Inject Particles container in body and VanillaTilt init in script
particles_html = "<div class='particles' id='particles'></div>"
content = content.replace("<div class=\"app\">", particles_html + "\n<div class=\"app\">")

js_init = """
// Initialize 3D Tilt
VanillaTilt.init(document.querySelectorAll(".card"), { max: 5, speed: 400, glare: true, "max-glare": 0.2 });

// Create particles
const pCont = document.getElementById('particles');
for(let i=0; i<30; i++) {
    let p = document.createElement('div');
    p.className = 'particle';
    let size = Math.random() * 5 + 2;
    p.style.width = size + 'px'; p.style.height = size + 'px';
    p.style.left = Math.random() * 100 + 'vw';
    p.style.animationDuration = (Math.random() * 10 + 10) + 's';
    p.style.animationDelay = (Math.random() * 10) + 's';
    pCont.appendChild(p);
}
"""
content = content.replace("renderTopics();renderQuiz();updateProgress();", "renderTopics();renderQuiz();updateProgress();\n" + js_init)

# Fix double initialization of VanillaTilt on newly rendered items? The cards are static mostly except topic lists.
# Actually, VanillaTilt on `.card` is fine as they are static.

with open('index.html', 'w') as f:
    f.write(content)

print("Visuals stunning-ified.")
