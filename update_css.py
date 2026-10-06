import re

with open('index.html', 'r') as f:
    content = f.read()

new_css = """
:root{
  --bg:#07111f;--panel:rgba(15,25,35,0.85);--card:rgba(20,30,45,0.85);--text:#ffffff;--muted:#c4d8eb;
  --cyan:#00f0ff;--blue:#3399ff;--green:#00ff88;--yellow:#ffea00;--red:#ff4466;--purple:#b892ff;
  --line:rgba(255,255,255,0.15);--shadow:0 18px 50px rgba(0,0,0,.4);--radius:20px;
}
* { box-sizing: border-box; } 
html { scroll-behavior: smooth; }
@keyframes mesh {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
body {
  margin: 0;
  background: linear-gradient(-45deg, #1f005c, #5b0060, #870160, #ac255e, #ca485c, #e16b5c, #f39060, #ffb56b);
  background-size: 400% 400%;
  animation: mesh 20s ease infinite;
  color: var(--text);
  font: 16px/1.7 Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  letter-spacing: 0.3px;
}
button, input { font: inherit; } 
button { cursor: pointer; transition: all 0.2s ease; }
a { color: inherit; text-decoration: none; }
.app { display: flex; min-height: 100vh; }
.sidebar { position: fixed; left: 0; top: 0; bottom: 0; width: 280px; padding: 24px 20px; background: rgba(10,15,25,0.85); backdrop-filter: blur(20px); border-right: 1px solid var(--line); z-index: 10; box-shadow: 5px 0 30px rgba(0,0,0,0.3); }
.logo { font-weight: 900; font-size: 20px; letter-spacing: -.5px; margin-bottom: 4px; text-shadow: 0 0 10px var(--cyan); }
.logo span { color: var(--cyan); }
.tag { font-size: 13px; color: var(--muted); margin-bottom: 25px; font-weight: 500; }
.nav { display: grid; gap: 8px; }
.nav button { border: 1px solid transparent; background: transparent; color: var(--muted); text-align: left; padding: 12px 16px; border-radius: 12px; font-weight: 600; font-size: 15px; }
.nav button:hover, .nav button.active { background: rgba(255,255,255,0.1); color: #fff; border-color: rgba(255,255,255,0.2); transform: translateX(5px); }
.progress { margin-top: 30px; padding: 16px; border: 1px solid var(--line); background: rgba(0,0,0,0.3); border-radius: 15px; }
.bar { height: 10px; background: rgba(255,255,255,0.1); border-radius: 99px; overflow: hidden; margin-top: 10px; box-shadow: inset 0 2px 5px rgba(0,0,0,0.5); }
.bar i { display: block; height: 100%; background: linear-gradient(90deg, var(--cyan), var(--green), var(--yellow)); width: 0; box-shadow: 0 0 10px var(--green); transition: width 0.5s ease; }
.main { margin-left: 280px; width: calc(100% - 280px); max-width: 1300px; padding: 40px 50px 100px; }
.top { display: flex; justify-content: space-between; align-items: center; gap: 20px; margin-bottom: 40px; }
.badge { display: inline-flex; padding: 8px 14px; border: 1px solid var(--cyan); border-radius: 99px; color: #fff; font-weight: bold; font-size: 13px; background: rgba(0,240,255,0.2); box-shadow: 0 0 15px rgba(0,240,255,0.3); text-shadow: 0 0 5px var(--cyan); }
h1 { font-size: clamp(38px, 5vw, 70px); line-height: 1.05; letter-spacing: -2px; margin: 10px 0 16px; text-shadow: 0 4px 20px rgba(0,0,0,0.5); }
h2 { font-size: 34px; line-height: 1.15; letter-spacing: -1px; margin: 0 0 14px; text-shadow: 0 2px 10px rgba(0,0,0,0.5); } 
h3 { margin: 0 0 10px; font-size: 20px; }
.lead { color: #eef2f6; font-size: 20px; max-width: 800px; font-weight: 500; text-shadow: 0 2px 5px rgba(0,0,0,0.5); }
.hero { padding: 40px; border: 1px solid rgba(255,255,255,0.3); border-radius: 28px; background: rgba(10,15,30,0.7); backdrop-filter: blur(25px); box-shadow: var(--shadow), 0 0 40px rgba(255,255,255,0.1) inset; overflow: hidden; position: relative; }
.hero:after { content: ""; position: absolute; width: 400px; height: 400px; border-radius: 50%; background: radial-gradient(circle, rgba(0,240,255,0.4) 0%, transparent 70%); right: -150px; top: -180px; filter: blur(40px); z-index: -1; }
.actions { display: flex; flex-wrap: wrap; gap: 14px; margin-top: 30px; }
.btn { border: 1px solid rgba(255,255,255,0.3); background: rgba(255,255,255,0.1); color: #fff; padding: 12px 20px; border-radius: 12px; font-weight: 800; font-size: 16px; backdrop-filter: blur(5px); text-transform: uppercase; letter-spacing: 1px; }
.btn.primary { background: linear-gradient(135deg, #ff007a, #7a00ff); border-color: transparent; box-shadow: 0 5px 20px rgba(122,0,255,0.5); }
.btn:hover { transform: translateY(-3px) scale(1.02); box-shadow: 0 8px 25px rgba(0,0,0,0.5); background: rgba(255,255,255,0.2); }
.btn.primary:hover { background: linear-gradient(135deg, #ff2a8e, #8f2aff); box-shadow: 0 8px 25px rgba(255,0,122,0.6); }
section { margin-top: 70px; scroll-margin-top: 40px; }
.section-head { display: flex; justify-content: space-between; gap: 15px; align-items: end; margin-bottom: 24px; }
.section-head p { color: var(--muted); margin: 0; font-size: 17px; }
.grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }
.grid2 { display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; }
.card { background: var(--card); backdrop-filter: blur(15px); border: 1px solid var(--line); border-radius: var(--radius); padding: 26px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); position: relative; overflow: hidden; }
.card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent); opacity: 0; transition: opacity 0.3s; }
.card.click { transition: all 0.25s cubic-bezier(0.2, 0.8, 0.2, 1); cursor: pointer; }
.card.click:hover { border-color: rgba(255,255,255,0.5); transform: translateY(-5px) scale(1.01); box-shadow: 0 15px 40px rgba(0,0,0,0.4); }
.card.click:hover::before { opacity: 1; }
.kicker { font-size: 13px; color: var(--cyan); font-weight: 900; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 8px; display: block; }
.muted { color: var(--muted); }
.flow { display: flex; gap: 12px; align-items: center; overflow: auto; padding: 12px 4px 20px; scrollbar-width: thin; }
.flow::-webkit-scrollbar { height: 8px; } .flow::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.2); border-radius: 4px; }
.node { min-width: 120px; padding: 16px 12px; text-align: center; border-radius: 16px; background: rgba(0,0,0,0.4); border: 1px solid var(--line); font-weight: 800; font-size: 14px; text-transform: uppercase; letter-spacing: 1px; box-shadow: inset 0 2px 10px rgba(255,255,255,0.05); }
.arrow { color: var(--yellow); font-weight: 900; font-size: 18px; text-shadow: 0 0 10px var(--yellow); }
.callout { padding: 20px; border-left: 5px solid var(--cyan); background: rgba(0,0,0,0.4); border-radius: 0 18px 18px 0; margin: 20px 0; font-size: 17px; box-shadow: 0 5px 15px rgba(0,0,0,0.2); backdrop-filter: blur(10px); }
.callout.green { border-color: var(--green); } .callout.yellow { border-color: var(--yellow); } .callout.red { border-color: var(--red); }
.tabs { display: flex; gap: 10px; flex-wrap: wrap; margin: 20px 0; }
.tab { padding: 10px 16px; border: 1px solid var(--line); background: rgba(0,0,0,0.3); color: var(--text); border-radius: 12px; font-weight: bold; }
.tab:hover { background: rgba(255,255,255,0.1); transform: translateY(-2px); }
.tab.active { color: #fff; border-color: var(--cyan); background: rgba(0,240,255,0.2); box-shadow: 0 0 15px rgba(0,240,255,0.3); }
.hidden { display: none !important; }
.modal { position: fixed; inset: 0; background: rgba(0,0,0,0.85); backdrop-filter: blur(12px); display: none; align-items: center; justify-content: center; padding: 20px; z-index: 100; }
.modal.open { display: flex; animation: fadeIn 0.3s ease; }
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
.modalbox { width: min(800px, 100%); max-height: 90vh; overflow: auto; background: rgba(15,20,35,0.95); border: 1px solid rgba(255,255,255,0.2); border-radius: 28px; padding: 34px; box-shadow: 0 20px 60px rgba(0,0,0,0.6); position: relative; animation: slideUp 0.3s ease; }
@keyframes slideUp { from { transform: translateY(30px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
.close { position: absolute; right: 24px; top: 24px; background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: #fff; border-radius: 50%; width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: bold; padding: 0; }
.close:hover { background: var(--red); border-color: var(--red); transform: rotate(90deg); }
.compare { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
.compare .card { min-height: 200px; display: flex; flex-direction: column; justify-content: space-between; }
.command { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; background: rgba(0,0,0,0.6); border: 1px solid rgba(255,255,255,0.1); padding: 16px 20px; border-radius: 14px; color: #00ffaa; margin: 12px 0; overflow: auto; font-size: 15px; box-shadow: inset 0 2px 10px rgba(0,0,0,0.5); }
table { width: 100%; border-collapse: collapse; margin-top: 10px; }
th, td { text-align: left; padding: 16px; border-bottom: 1px solid var(--line); vertical-align: top; }
th { color: var(--yellow); font-size: 14px; text-transform: uppercase; letter-spacing: 1px; }
td { font-size: 16px; }
.quiz { display: grid; gap: 20px; }
.q { padding: 24px; border: 1px solid rgba(255,255,255,0.2); border-radius: 22px; background: rgba(0,0,0,0.4); backdrop-filter: blur(10px); }
.options { display: grid; gap: 12px; margin-top: 16px; }
.opt { border: 1px solid rgba(255,255,255,0.2); background: rgba(255,255,255,0.05); color: #fff; text-align: left; padding: 16px 20px; border-radius: 14px; font-size: 16px; font-weight: 500; transition: all 0.2s; }
.opt:hover { background: rgba(255,255,255,0.15); transform: translateX(5px); }
.opt.correct { border-color: var(--green); background: rgba(0,255,136,0.2); box-shadow: 0 0 15px rgba(0,255,136,0.3); }
.opt.wrong { border-color: var(--red); background: rgba(255,68,102,0.2); box-shadow: 0 0 15px rgba(255,68,102,0.3); }
.score { font-size: 30px; font-weight: 900; background: linear-gradient(90deg, #ff007a, #00f0ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.search { width: 100%; padding: 16px 20px; border-radius: 16px; background: rgba(0,0,0,0.5); color: #fff; border: 1px solid rgba(255,255,255,0.2); font-size: 18px; box-shadow: inset 0 2px 10px rgba(0,0,0,0.3); transition: all 0.3s; }
.search:focus { outline: none; border-color: var(--cyan); box-shadow: 0 0 20px rgba(0,240,255,0.2); }
.topic-list { display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px; }
.topic { padding: 16px 20px; border: 1px solid rgba(255,255,255,0.15); border-radius: 16px; background: rgba(0,0,0,0.3); display: flex; justify-content: space-between; gap: 15px; align-items: center; transition: all 0.2s; text-align: left; }
.topic:hover { background: rgba(255,255,255,0.1); transform: translateY(-3px); border-color: rgba(255,255,255,0.3); box-shadow: 0 5px 15px rgba(0,0,0,0.2); }
.topic small { color: var(--muted); display: block; margin-top: 6px; font-size: 14px; line-height: 1.5; }
footer { text-align: center; color: rgba(255,255,255,0.6); padding: 60px 0 30px; font-size: 15px; font-weight: 500; }
@media(max-width:900px){
  .sidebar { width: 80px; padding: 20px 10px; }
  .logo { font-size: 0; } .logo span { font-size: 20px; }
  .tag, .nav button span, .progress { display: none; }
  .nav button { font-size: 0; text-align: center; padding: 14px 0; }
  .nav button:first-letter { font-size: 22px; }
  .main { margin-left: 80px; width: calc(100% - 80px); padding: 30px 24px; }
  .grid, .grid2, .compare, .topic-list { grid-template-columns: 1fr; }
}
@media(max-width:600px){
  .main { padding: 24px 16px; }
  .hero { padding: 30px 20px; }
  h1 { font-size: 42px; }
  .sidebar { width: 70px; }
  .main { margin-left: 70px; width: calc(100% - 70px); }
  .flow { gap: 8px; }
  .node { min-width: 100px; font-size: 13px; padding: 12px 8px; }
}
"""

start_idx = content.find('<style>') + len('<style>')
end_idx = content.find('</style>')

updated_content = content[:start_idx] + "\n" + new_css.strip() + "\n" + content[end_idx:]

with open('index.html', 'w') as f:
    f.write(updated_content)

print("Updated CSS successfully.")
