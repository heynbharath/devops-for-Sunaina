import re

with open('index.html', 'r') as f:
    content = f.read()

old_screen1 = """    <!-- Screen 1: Dev vs Ops -->
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
    </div>"""

new_screen1 = """    <!-- Screen 1: Dev vs Ops -->
    <div class="screen" id="screen-1">
      <h2>1. The Core Idea</h2>
      <p>Before DevOps, developers wrote code and tossed it over a "wall" to Operations. If it broke, they blamed each other.</p>
      
      <div class="interactive-zone" style="position: relative; height: 200px; display: flex; justify-content: center; align-items: center; overflow: hidden; perspective: 1000px;">
        <div id="dev-text" style="font-size: 3rem; font-weight: 900; color: #8a2be2; position: absolute; left: 10%; transition: all 0.8s cubic-bezier(0.25, 1, 0.5, 1);">DEV</div>
        
        <button id="wall" onclick="smashWall()" style="position: absolute; z-index: 10; background: linear-gradient(to bottom, #ff4444, #ff8800); border: none; width: 140px; height: 100%; color: white; font-weight: 900; font-size: 1.2rem; cursor: pointer; transition: all 0.2s; box-shadow: 0 0 30px rgba(255,68,68,0.6); text-transform: uppercase; letter-spacing: 2px;">
          Smash<br>The Wall!
        </button>
        
        <div id="ops-text" style="font-size: 3rem; font-weight: 900; color: #00ffaa; position: absolute; right: 10%; transition: all 0.8s cubic-bezier(0.25, 1, 0.5, 1);">OPS</div>
      </div>
      
      <p id="wall-text" style="opacity: 0; transform: translateY(10px); transition: all 0.5s; text-align: center; font-size: 1.3rem; margin-top: 20px;">
        <span style="color:var(--primary); font-weight:bold;">Boom!</span> DevOps unites them. Shared ownership.
      </p>
      <button class="btn primary" id="btn-1" style="display:none; margin: 0 auto;" onclick="nextScreen()">Makes sense →</button>
    </div>"""

content = content.replace(old_screen1, new_screen1)

# Update the smashWall logic
old_logic = """  function smashWall() {
    const wall = document.getElementById('wall');
    wall.style.transform = 'scaleY(0)';
    wall.style.opacity = '0';
    document.getElementById('wall-text').style.opacity = '1';
    document.getElementById('btn-1').style.display = 'block';
    confetti({ particleCount: 50, spread: 60, origin: { y: 0.7 } });
  }"""

new_logic = """  function smashWall() {
    const wall = document.getElementById('wall');
    wall.style.transform = 'translateZ(-500px) rotateX(90deg)';
    wall.style.opacity = '0';
    wall.style.pointerEvents = 'none';
    
    // Merge DEV and OPS together
    const dev = document.getElementById('dev-text');
    const ops = document.getElementById('ops-text');
    dev.style.left = 'calc(50% - 60px)';
    ops.style.right = 'calc(50% - 65px)';
    
    setTimeout(() => {
        document.getElementById('wall-text').style.opacity = '1';
        document.getElementById('wall-text').style.transform = 'translateY(0)';
        document.getElementById('btn-1').style.display = 'block';
    }, 600);

    // Crazy confetti explosion
    confetti({ particleCount: 150, spread: 100, origin: { y: 0.5 }, colors: ['#8a2be2', '#00ffaa', '#ff4444'] });
  }"""

content = content.replace(old_logic, new_logic)

with open('index.html', 'w') as f:
    f.write(content)

print("Fixed screen 1.")
