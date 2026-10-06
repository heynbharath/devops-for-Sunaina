html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>DevOps for Sunaina 🚀</title>
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
<style>
  :root {
    --bg: #0a0a0a;
    --surface: #171717;
    --surface-hover: #262626;
    --primary: #00ffaa;
    --primary-glow: rgba(0, 255, 170, 0.4);
    --secondary: #8a2be2;
    --text: #ffffff;
    --text-muted: #a3a3a3;
    --danger: #ff4444;
    --font: 'Inter', system-ui, -apple-system, sans-serif;
  }
  
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: var(--font); }
  
  body {
    background-color: var(--bg);
    color: var(--text);
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    overflow: hidden;
  }

  /* Cool background grid */
  body::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image: 
      linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
      linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
    background-size: 50px 50px;
    z-index: -1;
    pointer-events: none;
  }

  .app-container {
    width: 100%;
    max-width: 800px;
    height: 80vh;
    min-height: 600px;
    background: var(--surface);
    border-radius: 24px;
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5);
    display: flex;
    flex-direction: column;
    position: relative;
    overflow: hidden;
  }

  /* Header */
  .header {
    padding: 24px 32px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(255,255,255,0.05);
  }
  .progress-container {
    display: flex;
    gap: 8px;
    flex: 1;
    max-width: 300px;
  }
  .progress-pip {
    height: 6px;
    flex: 1;
    background: rgba(255,255,255,0.1);
    border-radius: 4px;
    transition: all 0.3s ease;
  }
  .progress-pip.active {
    background: var(--primary);
    box-shadow: 0 0 10px var(--primary-glow);
  }
  .progress-pip.completed {
    background: var(--secondary);
  }

  /* Content Area */
  .content {
    flex: 1;
    padding: 40px;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
    position: relative;
  }

  .screen {
    display: none;
    animation: slideIn 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  }
  .screen.active {
    display: flex;
    flex-direction: column;
    height: 100%;
  }

  @keyframes slideIn {
    from { opacity: 0; transform: translateY(20px) scale(0.98); }
    to { opacity: 1; transform: translateY(0) scale(1); }
  }

  h1 { font-size: 3rem; font-weight: 800; letter-spacing: -1px; margin-bottom: 16px; line-height: 1.1; }
  h2 { font-size: 2rem; font-weight: 700; letter-spacing: -0.5px; margin-bottom: 16px; }
  p { font-size: 1.2rem; color: var(--text-muted); line-height: 1.6; margin-bottom: 32px; }
  
  .highlight { color: var(--primary); }

  /* Buttons */
  .btn {
    background: var(--text);
    color: var(--bg);
    border: none;
    padding: 16px 32px;
    font-size: 1.1rem;
    font-weight: 600;
    border-radius: 12px;
    cursor: pointer;
    transition: all 0.2s;
    align-self: flex-start;
  }
  .btn:hover { transform: translateY(-2px); box-shadow: 0 10px 20px rgba(255,255,255,0.1); }
  .btn.primary { background: var(--primary); color: var(--bg); }
  .btn.primary:hover { box-shadow: 0 10px 25px var(--primary-glow); }

  /* Interactive Elements */
  .interactive-zone {
    background: rgba(0,0,0,0.3);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 24px;
  }

  /* Git Simulator */
  .git-boxes {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin-bottom: 24px;
  }
  .git-box {
    background: rgba(255,255,255,0.05);
    border: 1px dashed rgba(255,255,255,0.2);
    border-radius: 12px;
    padding: 16px 8px;
    text-align: center;
    font-size: 0.9rem;
    font-weight: 600;
    color: var(--text-muted);
    position: relative;
    transition: all 0.3s;
  }
  .git-box.has-file {
    border-color: var(--primary);
    background: rgba(0,255,170,0.05);
    color: var(--primary);
  }
  .file-token {
    width: 30px; height: 30px;
    background: var(--primary);
    border-radius: 8px;
    margin: 10px auto 0;
    animation: popIn 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  }
  @keyframes popIn { 0% { transform: scale(0); } 100% { transform: scale(1); } }

  .terminal {
    background: #000;
    border-radius: 8px;
    padding: 16px;
    font-family: 'Menlo', monospace;
    display: flex;
    align-items: center;
  }
  .terminal-prefix { color: var(--primary); margin-right: 12px; }
  .terminal-input {
    background: transparent;
    border: none;
    color: #fff;
    font-family: 'Menlo', monospace;
    font-size: 1rem;
    width: 100%;
    outline: none;
  }

  /* CI/CD Cards */
  .cicd-cards {
    display: flex;
    gap: 16px;
    margin-bottom: 24px;
  }
  .cicd-card {
    flex: 1;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 16px;
    padding: 24px;
    cursor: pointer;
    transition: all 0.2s;
  }
  .cicd-card:hover { background: rgba(255,255,255,0.1); border-color: var(--text); }
  .cicd-card.correct { border-color: var(--primary); background: rgba(0,255,170,0.1); }
  .cicd-card.wrong { border-color: var(--danger); background: rgba(255,68,68,0.1); animation: shake 0.4s; }

  @keyframes shake {
    0%, 100% { transform: translateX(0); }
    25% { transform: translateX(-5px); }
    75% { transform: translateX(5px); }
  }

</style>
</head>
<body>

<div class="app-container">
  <div class="header">
    <div style="font-weight: 800; letter-spacing: -0.5px;">DEV<span class="highlight">OPS</span></div>
    <div class="progress-container" id="progress">
      <!-- Pips injected via JS -->
    </div>
  </div>

  <div class="content" id="content">
    
    <!-- Screen 0: Welcome -->
    <div class="screen active" id="screen-0">
      <div style="margin: auto 0;">
        <h1>Hey Sunaina, <br>let's crush MSE-1.</h1>
        <p>No boring PDFs. No walls of text.<br>Just pure, interactive mental models.</p>
        <button class="btn primary" onclick="nextScreen()">Start Learning</button>
      </div>
    </div>

    <!-- Screen 1: Dev vs Ops -->
    <div class="screen" id="screen-1">
      <h2>1. The Core Idea</h2>
      <p>Before DevOps, developers wrote code and tossed it over a "wall" to Operations. If it broke, they blamed each other.</p>
      
      <div class="interactive-zone" style="display: flex; justify-content: space-between; align-items: center; padding: 40px;">
        <div style="font-size: 24px; font-weight: bold; color: #8a2be2;">DEV</div>
        <div id="wall" style="width: 4px; height: 100px; background: #fff; cursor: pointer; transition: all 0.3s;" onclick="smashWall()">
          <div style="position:absolute; margin-left:-25px; margin-top:110px; font-size:12px; color:var(--text-muted)">Click to smash</div>
        </div>
        <div style="font-size: 24px; font-weight: bold; color: #00ffaa;">OPS</div>
      </div>
      
      <p id="wall-text" style="opacity: 0.3;">DevOps is the culture and practice of uniting these two. Shared ownership.</p>
      <button class="btn primary" id="btn-1" style="display:none;" onclick="nextScreen()">Makes sense →</button>
    </div>

    <!-- Screen 2: Git Simulator -->
    <div class="screen" id="screen-2">
      <h2>2. See Git Happen</h2>
      <p>Don't memorize commands. See where the code moves. Type the command to move the file forward.</p>
      
      <div class="interactive-zone">
        <div class="git-boxes">
          <div class="git-box has-file" id="gb-work">Working Dir<div class="file-token" id="file-tok"></div></div>
          <div class="git-box" id="gb-stage">Staging Area</div>
          <div class="git-box" id="gb-local">Local Repo</div>
          <div class="git-box" id="gb-remote">GitHub</div>
        </div>
        
        <div class="terminal">
          <span class="terminal-prefix">~</span>
          <input type="text" class="terminal-input" id="git-input" placeholder="type 'git add .' and press Enter" autocomplete="off" spellcheck="false">
        </div>
      </div>
      
      <p id="git-hint" style="color: var(--primary); font-family: monospace;"></p>
      <button class="btn primary" id="btn-2" style="display:none;" onclick="nextScreen()">Next: CI/CD →</button>
    </div>

    <!-- Screen 3: CI/CD -->
    <div class="screen" id="screen-3">
      <h2>3. CI vs CD vs CD</h2>
      <p>Your code passes all tests. It is automatically pushed to production and live for users immediately. What is this called?</p>
      
      <div class="cicd-cards">
        <div class="cicd-card" onclick="checkCICD(this, false)">Continuous<br>Integration</div>
        <div class="cicd-card" onclick="checkCICD(this, false)">Continuous<br>Delivery</div>
        <div class="cicd-card" onclick="checkCICD(this, true)">Continuous<br>Deployment</div>
      </div>
      
      <p id="cicd-explanation" style="opacity: 0; transition: opacity 0.3s;"></p>
      <button class="btn primary" id="btn-3" style="display:none; margin-top: 20px;" onclick="nextScreen()">Nailed it →</button>
    </div>

    <!-- Screen 4: Quality Gates & DORA -->
    <div class="screen" id="screen-4">
      <h2>4. Measuring Success</h2>
      <p>Which DORA metric answers: <span style="color:white;font-weight:bold;">"How long does it take to go from code committed to code running in production?"</span></p>
      
      <div class="interactive-zone" style="display: flex; flex-direction: column; gap: 10px;">
        <button class="btn" style="width:100%; background:rgba(255,255,255,0.05); color:white;" onclick="checkDora(this, false)">Deployment Frequency</button>
        <button class="btn" style="width:100%; background:rgba(255,255,255,0.05); color:white;" onclick="checkDora(this, true)">Lead Time for Changes</button>
        <button class="btn" style="width:100%; background:rgba(255,255,255,0.05); color:white;" onclick="checkDora(this, false)">Change Failure Rate</button>
      </div>

      <button class="btn primary" id="btn-4" style="display:none; margin-top: 20px;" onclick="nextScreen()">Almost done →</button>
    </div>

    <!-- Screen 5: Final -->
    <div class="screen" id="screen-5">
      <div style="margin: auto 0; text-align: center;">
        <h1 style="font-size: 4rem;">🎉</h1>
        <h2>You are ready, Sunaina!</h2>
        <p>You've mastered the core mental models. You know Git flows, CI/CD distinctions, and DORA metrics. Sleep well and ace that MSE-1 tomorrow.</p>
        <button class="btn primary" style="margin: 0 auto; display: block;" onclick="location.reload()">Restart Review</button>
      </div>
    </div>

  </div>
</div>

<script>
  let currentScreen = 0;
  const totalScreens = 6;
  
  // Init progress pips
  const progressCont = document.getElementById('progress');
  for(let i=0; i<totalScreens; i++){
    const pip = document.createElement('div');
    pip.className = 'progress-pip' + (i===0 ? ' active' : '');
    progressCont.appendChild(pip);
  }

  function nextScreen() {
    document.getElementById('screen-' + currentScreen).classList.remove('active');
    
    // Update pips
    progressCont.children[currentScreen].classList.remove('active');
    progressCont.children[currentScreen].classList.add('completed');
    
    currentScreen++;
    
    if(currentScreen < totalScreens) {
      document.getElementById('screen-' + currentScreen).classList.add('active');
      progressCont.children[currentScreen].classList.add('active');
    }
    
    if(currentScreen === 2) {
      document.getElementById('git-input').focus();
    }
    
    if(currentScreen === 5) {
      confetti({ particleCount: 150, spread: 80, origin: { y: 0.6 } });
    }
  }

  // Screen 1 Logic
  function smashWall() {
    const wall = document.getElementById('wall');
    wall.style.transform = 'scaleY(0)';
    wall.style.opacity = '0';
    document.getElementById('wall-text').style.opacity = '1';
    document.getElementById('btn-1').style.display = 'block';
    confetti({ particleCount: 50, spread: 60, origin: { y: 0.7 } });
  }

  // Screen 2 Logic
  let gitState = 0;
  const gitInput = document.getElementById('git-input');
  const gitHint = document.getElementById('git-hint');
  
  gitInput.addEventListener('keydown', function(e) {
    if(e.key === 'Enter') {
      const val = gitInput.value.trim().toLowerCase();
      gitInput.value = '';
      
      if(gitState === 0 && (val === 'git add .' || val === 'git add')) {
        moveFile('gb-work', 'gb-stage');
        gitState++;
        gitHint.innerText = "Staged! Now commit it (e.g. git commit -m 'msg').";
      } 
      else if(gitState === 1 && val.startsWith('git commit')) {
        moveFile('gb-stage', 'gb-local');
        gitState++;
        gitHint.innerText = "Committed to local repo! Now push it to GitHub (git push).";
      }
      else if(gitState === 2 && val.startsWith('git push')) {
        moveFile('gb-local', 'gb-remote');
        gitState++;
        gitHint.innerText = "Pushed! You've mastered the flow.";
        document.getElementById('btn-2').style.display = 'block';
        confetti({ particleCount: 100, spread: 70, origin: { y: 0.6 } });
      }
      else {
        gitHint.innerText = "Not quite. Try what makes sense for the current state.";
        gitInput.parentElement.style.animation = 'none';
        setTimeout(() => gitInput.parentElement.style.animation = 'shake 0.4s', 10);
      }
    }
  });

  function moveFile(fromId, toId) {
    document.getElementById(fromId).classList.remove('has-file');
    document.getElementById(fromId).innerHTML = document.getElementById(fromId).innerHTML.replace('<div class="file-token" id="file-tok"></div>', '');
    
    document.getElementById(toId).classList.add('has-file');
    document.getElementById(toId).innerHTML += '<div class="file-token" id="file-tok"></div>';
  }

  // Screen 3 Logic
  function checkCICD(el, isCorrect) {
    document.querySelectorAll('.cicd-card').forEach(c => c.className = 'cicd-card');
    if(isCorrect) {
      el.classList.add('correct');
      document.getElementById('cicd-explanation').innerHTML = "<b>Correct!</b> 'Deployment' means it goes to production automatically. 'Delivery' means it's ready, but waits for a human to click deploy.";
      document.getElementById('cicd-explanation').style.opacity = '1';
      document.getElementById('btn-3').style.display = 'block';
      confetti({ particleCount: 50 });
    } else {
      el.classList.add('wrong');
    }
  }

  // Screen 4 Logic
  function checkDora(el, isCorrect) {
    if(isCorrect) {
      el.style.background = 'rgba(0,255,170,0.2)';
      el.style.borderColor = 'var(--primary)';
      el.style.color = 'var(--primary)';
      document.getElementById('btn-4').style.display = 'block';
      confetti({ particleCount: 50 });
    } else {
      el.style.background = 'rgba(255,68,68,0.2)';
      el.style.borderColor = 'var(--danger)';
      el.style.color = 'var(--danger)';
      el.style.animation = 'none';
      setTimeout(() => el.style.animation = 'shake 0.4s', 10);
    }
  }

</script>
</body>
</html>
"""
with open('index.html', 'w') as f:
    f.write(html_content)

print("Created YC-style gamified learning app.")
