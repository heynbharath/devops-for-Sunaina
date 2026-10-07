import re

with open('index.html', 'r') as f:
    content = f.read()

# Extract just the HTML part before and after style
head_before_style = content.split('<style>')[0]
after_style = content.split('</style>')[1]

clean_css = """
:root{
  --bg:#12050f;--panel:rgba(30,10,25,0.7);--card:rgba(40,15,35,0.6);--text:#fff0f5;--muted:#ffb6c1;
  --cyan:#ff7eb3;--blue:#ffdf99;--green:#a1c4fd;--yellow:#fbc2eb;--red:#ff4e50;--purple:#c2e9fb;
  --line:rgba(255,118,179,0.25);--shadow:0 18px 50px rgba(0,0,0,.6);--radius:20px;
}
* { box-sizing: border-box; } 
html { scroll-behavior: smooth; }
body {
  margin: 0;
  background: linear-gradient(-45deg, #2a0845, #6441A5, #ff0844, #ffb199, #12050f);
  background-size: 400% 400%;
  animation: mesh 25s ease infinite;
  color: var(--text);
  font: 16px/1.7 'Outfit', ui-sans-serif, system-ui, sans-serif;
  letter-spacing: 0.3px;
}
@keyframes mesh { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
button, input { font: inherit; } 
button { cursor: pointer; transition: all 0.2s ease; }
a { color: inherit; text-decoration: none; }
.app { display: flex; min-height: 100vh; }

/* Desktop Sidebar */
.sidebar { position: fixed; left: 0; top: 0; bottom: 0; width: 280px; padding: 24px 20px; background: rgba(10,5,15,0.98); border-right: 1px solid var(--line); z-index: 1000; box-shadow: 5px 0 30px rgba(0,0,0,0.5); }
.logo { font-weight: 900; font-size: 20px; letter-spacing: -.5px; margin-bottom: 4px; text-shadow: 0 0 10px rgba(255,126,179,0.8); }
.logo span { color: var(--cyan); }
.tag { font-size: 13px; color: var(--muted); margin-bottom: 25px; font-weight: 500; }
.nav { display: grid; gap: 8px; }
.nav button { border: 1px solid transparent; background: transparent; color: var(--muted); text-align: left; padding: 12px 16px; border-radius: 12px; font-weight: 600; font-size: 15px; }
.nav button:hover, .nav button.active { background: rgba(255,126,179,0.15); color: #fff; border-color: rgba(255,126,179,0.3); transform: translateX(5px); }
.progress { margin-top: 30px; padding: 16px; border: 1px solid var(--line); background: rgba(0,0,0,0.3); border-radius: 15px; }
.bar { height: 6px; background: rgba(255,255,255,0.1); border-radius: 6px; margin: 8px 0; overflow: hidden; }
.bar i { display: block; height: 100%; background: var(--cyan); transition: width 0.3s; box-shadow: 0 0 10px var(--cyan); }

.main { margin-left: 280px; width: calc(100% - 280px); max-width: 1300px; padding: 40px 50px 100px; }
.top { display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px; }
.badge { background: rgba(255,126,179,0.1); color: var(--cyan); padding: 6px 12px; border-radius: 20px; font-size: 12px; border: 1px solid rgba(255,126,179,0.3); }

/* Typography */
h1, h2, h3 { line-height: 1.2; margin: 0 0 16px; }
h2 { font-size: 32px; font-weight: 800; letter-spacing: -1px; }
h3 { font-size: 20px; font-weight: 700; }
p { margin: 0 0 16px; }
.lead { font-size: 20px; color: var(--muted); }
.muted { color: var(--muted); }

/* Layouts */
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; }
.grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
.section-head { margin: 60px 0 30px; border-bottom: 1px solid var(--line); padding-bottom: 20px; }

/* Components */
.card { background: var(--card); border: 1px solid var(--line); padding: 24px; border-radius: var(--radius); box-shadow: var(--shadow); position: relative; }
.btn { background: rgba(255,255,255,0.1); color: #fff; border: 1px solid rgba(255,255,255,0.2); padding: 12px 24px; border-radius: 12px; font-weight: 600; }
.btn:hover { background: rgba(255,255,255,0.2); }
.btn.primary { background: linear-gradient(135deg, #ff0844, #ffb199); border-color: transparent; box-shadow: 0 5px 20px rgba(255,8,68,0.5); }
.btn.primary:hover { background: linear-gradient(135deg, #ff4e50, #f9d423); box-shadow: 0 8px 25px rgba(255,78,80,0.6); }

/* Decorative */
.kicker, .badge, th { font-family: 'Space Grotesk', monospace; letter-spacing: 2px; }
.command { font-family: 'Space Grotesk', monospace; font-size: 16px; background: rgba(0,0,0,0.5); padding: 8px 12px; border-radius: 8px; color: #00ffaa; margin-bottom: 8px; border: 1px solid rgba(0,255,170,0.2); }
.hero { position: relative; border-radius: 32px; overflow: hidden; box-shadow: 0 30px 60px rgba(0,0,0,0.5), inset 0 0 0 1px rgba(255,255,255,0.2); }
.hero-content { background: rgba(10,15,30,0.85); padding: 50px; border-radius: 32px; height: 100%; width: 100%; }
.hero::before { content: ''; position: absolute; top: -50%; left: -50%; width: 200%; height: 200%; background: conic-gradient(transparent, rgba(255,126,179,0.4), transparent 30%); animation: rotate 12s linear infinite; z-index: -1; }
@keyframes rotate { 100% { transform: rotate(360deg); } }
h1 { font-weight: 900; background: linear-gradient(135deg, #fff0f5, #ffb199); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }

/* 3D and floating */
.card { transform-style: preserve-3d; transform: perspective(1000px); }
.card > * { transform: translateZ(30px); }
.particles { position: fixed; inset: 0; pointer-events: none; z-index: 0; overflow: hidden; }
@keyframes floatUp { 0% { transform: translateY(100vh) scale(0); opacity: 0; } 50% { opacity: 0.5; } 100% { transform: translateY(-100px) scale(1); opacity: 0; } }
.particle { position: absolute; border-radius: 50%; background: radial-gradient(circle, #ff7eb3, transparent); opacity: 0.4; animation: floatUp linear infinite; filter: blur(2px); }
::-webkit-scrollbar { width: 10px; }
::-webkit-scrollbar-track { background: rgba(0,0,0,0.3); }
::-webkit-scrollbar-thumb { background: rgba(255,126,179,0.5); border-radius: 10px; }
::-webkit-scrollbar-thumb:hover { background: rgba(255,126,179,0.8); }

/* Heart */
@keyframes heartbeat { 0% { transform: scale(1); } 14% { transform: scale(1.3); } 28% { transform: scale(1); } 42% { transform: scale(1.3); } 70% { transform: scale(1); } }
.heart { display: inline-block; animation: heartbeat 2s infinite; color: #ff0844; }

/* Modal */
.modal { position: fixed; inset: 0; background: rgba(0,0,0,0.85); backdrop-filter: blur(12px); display: none; align-items: center; justify-content: center; padding: 20px; z-index: 9999; }
.modal.open { display: flex; animation: fadeIn 0.3s ease; }
.modalbox { width: min(800px, 100%); max-height: 90vh; overflow: auto; background: rgba(15,20,35,1); border: 1px solid rgba(255,255,255,0.2); border-radius: 28px; padding: 34px; box-shadow: 0 20px 60px rgba(0,0,0,0.9); position: relative; animation: slideUp 0.3s ease; }
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
@keyframes slideUp { from { transform: translateY(20px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }

/* Fix Connect the dots */
.connect-step { display: flex; gap: 20px; align-items: stretch; }

/* MISC classes */
.actions { margin-top: 24px; display: flex; gap: 12px; }
.flow { display: flex; align-items: center; gap: 12px; overflow-x: auto; padding-bottom: 12px; }
.node { background: rgba(0,0,0,0.4); padding: 16px 24px; border-radius: 12px; border: 1px solid var(--line); text-align: center; font-weight: 600; white-space: nowrap; flex: 1; }
.arrow { color: var(--cyan); font-weight: 900; }
.callout { background: rgba(255,255,255,0.1); padding: 16px; border-radius: 12px; border-left: 4px solid var(--cyan); margin-top: 16px; }
.callout.green { border-color: var(--green); }
.callout.yellow { border-color: var(--yellow); }
.compare { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; margin-top: 16px; }
table { width: 100%; border-collapse: collapse; margin-top: 16px; }
th, td { padding: 16px; text-align: left; border-bottom: 1px solid var(--line); }
th { color: var(--muted); font-size: 13px; text-transform: uppercase; }
.topic-list { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
.topic { padding: 16px 20px; border: 1px solid rgba(255,255,255,0.15); border-radius: 16px; background: rgba(0,0,0,0.3); display: flex; justify-content: space-between; gap: 15px; align-items: center; transition: all 0.2s; text-align: left; cursor: pointer; }
.topic:hover { background: rgba(255,255,255,0.1); transform: translateY(-3px); border-color: rgba(255,255,255,0.3); box-shadow: 0 5px 15px rgba(0,0,0,0.2); }
.topic small { color: var(--muted); display: block; margin-top: 6px; font-size: 14px; line-height: 1.5; }
footer { text-align: center; color: rgba(255,255,255,0.6); padding: 60px 0 30px; font-size: 15px; font-weight: 500; }
.click { cursor: pointer; }
.tabs { margin-top: 16px; display: flex; gap: 8px; }
.tab { padding: 8px 16px; background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); border-radius: 8px; color: var(--text); }
.tab.active { background: var(--cyan); color: #000; border-color: var(--cyan); }


/* ----------------------------------------------------
   FINAL BOSS MOBILE / TABLET RESPONSIVENESS
------------------------------------------------------- */
.mobile-header { display: none; }
.close-btn { display: none; }

@media(max-width: 950px) {
  /* Top Header */
  .mobile-header {
      display: flex; position: fixed; top: 0; left: 0; right: 0; height: 75px;
      background: #150a13; /* Solid background to guarantee no transparency issues */
      border-bottom: 1px solid rgba(255,126,179,0.3);
      align-items: center; justify-content: space-between; padding: 0 24px;
      z-index: 900; box-shadow: 0 10px 30px rgba(0,0,0,0.8);
  }
  .hamburger { background: transparent; border: none; padding: 10px; cursor: pointer; display: flex; align-items: center; justify-content: center; border-radius: 12px; }
  .hamburger:hover { background: rgba(255,126,179,0.2); }
  
  /* The Off-Canvas Drawer (No longer transparent!) */
  .sidebar {
      position: fixed; top: 0; left: -110%; width: 320px; height: 100vh;
      background: #11050d !important; /* Solid, dark, opaque color */
      transition: left 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      z-index: 10000; display: block !important; border-right: 1px solid rgba(255,126,179,0.3);
      box-shadow: 30px 0 60px rgba(0,0,0,0.9);
  }
  .sidebar.open { left: 0; }
  
  /* Close Button inside Drawer */
  .close-btn {
      display: block; position: absolute; top: 20px; right: 20px;
      background: rgba(255,255,255,0.15); border: none; color: white;
      width: 40px; height: 40px; border-radius: 50%; font-size: 18px;
      cursor: pointer; display: flex; align-items: center; justify-content: center;
  }
  
  /* Reset nav styling */
  .nav { display: grid !important; flex-direction: column !important; gap: 8px !important; overflow: visible !important; }
  .nav button { padding: 14px 20px !important; font-size: 16px !important; border-radius: 14px !important; text-align: left !important; background: transparent !important; border: 1px solid transparent !important; }
  .nav button:hover, .nav button.active { background: rgba(255,126,179,0.15) !important; color: #fff !important; transform: translateX(5px) !important; border-color: rgba(255,126,179,0.3) !important; }
  
  .logo { font-size: 20px !important; margin-bottom: 30px !important; text-align: left !important; }
  .logo br { display: block !important; }
  .logo span:last-child { display: inline !important; }
  .tag { display: block !important; }
  
  /* Main Content */
  .main { margin-left: 0 !important; width: 100% !important; padding: 100px 20px 60px !important; }
  
  /* Responsive Grids */
  .grid, .grid2, .compare, .topic-list { grid-template-columns: 1fr; gap: 16px; }
  .hero-content { padding: 30px 24px !important; }
  h1 { font-size: 40px !important; line-height: 1.1 !important; margin-bottom: 16px !important; }
  
  /* Fix Connect the Dots for Mobile */
  .connect-step { flex-direction: column !important; align-items: flex-start !important; gap: 12px !important; }
  .connect-step > div:first-child { width: 36px !important; height: 36px !important; font-size: 16px !important; }
  
  /* Hide Clutter */
  .top { display: none !important; }
}

@media(max-width: 500px) {
  h1 { font-size: 34px !important; }
  .hero-content { padding: 24px 20px !important; }
  .lead { font-size: 16px !important; line-height: 1.6 !important; }
  .main { padding-top: 95px !important; padding-left: 16px !important; padding-right: 16px !important; }
  .modalbox { width: 95% !important; padding: 20px !important; border-radius: 16px !important; margin: 10px; }
}
"""

content = head_before_style + "<style>\n" + clean_css + "\n</style>" + after_style

with open('index.html', 'w') as f:
    f.write(content)

print("Cleaned CSS and forced solid background for sidebar.")
