import re

with open('index.html', 'r') as f:
    content = f.read()

# Update title
content = content.replace('<title>DevOps + Git — MSE-1 Interactive Learning Lab</title>', '<title>DevOps + Git — Sunaina\'s MSE-1 Lab</title>')

# Add confetti JS
confetti_script = '<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>\n</head>'
content = content.replace('</head>', confetti_script)

# Update Logo
content = content.replace('<div class="logo">DEV<span>OPS</span> LAB</div>', '<div class="logo">DEV<span>OPS</span> LAB<br><span style="font-size:12px;color:var(--cyan);font-weight:normal">for Sunaina Mohapatra 👩🏻‍💻</span></div>')

# Update Hero
old_hero = '<h1>Make the whole thing <span style="color:var(--cyan)">click.</span></h1>\n  <p class="lead">This is not another PDF. Follow one software-release story, click the moving parts, experiment with Git workflows, then prove you understand it.</p>'
new_hero = '<h1>You\'ve got this, <span style="color:var(--cyan)">Sunaina! 🚀</span></h1>\n  <p class="lead">Good evening! Tomorrow is your MSE-1 for DevOps. Don\'t stress. This interactive lab is designed just for you to revise all 40 topics easily. Follow the story, click the moving parts, and crush that exam!</p>'
content = content.replace(old_hero, new_hero)

# Update Footer
content = content.replace('<footer>Built as an interactive MSE-1 learning companion • No login • No backend • Works as a single HTML file</footer>', '<footer>Built specially for Sunaina Mohapatra\'s MSE-1 Exam Prep ❤️ • You are going to ace it!</footer>')

# Add confetti trigger on 100% quiz
quiz_js = '''b.classList.add(oi===q[2]?'correct':'wrong');document.getElementById('score').textContent=Object.entries(answers).filter(([k,v])=>questions[k][2]===v).length+' / 8';'''
new_quiz_js = '''
if(oi===q[2]) { b.classList.add('correct'); confetti({particleCount: 50, spread: 60, origin: { y: 0.8 }}); } else { b.classList.add('wrong'); }
let sc = Object.entries(answers).filter(([k,v])=>questions[k][2]===v).length;
document.getElementById('score').textContent = sc + ' / 8';
if(sc === 8) { confetti({particleCount: 200, spread: 100, origin: { y: 0.5 }}); }
'''
content = content.replace(quiz_js, new_quiz_js.strip().replace('\n', ''))

# Progress bar confetti
prog_js = "function mark(i){if(!explored.includes(i)){explored.push(i);save()}}"
new_prog_js = "function mark(i){if(!explored.includes(i)){explored.push(i);save(); if(explored.length===40) confetti({particleCount: 300, spread: 120, origin: { y: 0.5 }});}}"
content = content.replace(prog_js, new_prog_js)

with open('index.html', 'w') as f:
    f.write(content)

print("Updated index.html successfully.")
