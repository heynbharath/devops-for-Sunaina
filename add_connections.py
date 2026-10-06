import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Add sidebar nav item
nav_item = """<button onclick="go('connect')">🔗 <span>Connect the Dots</span></button>"""
# Find where practice ends
content = content.replace("<button onclick=\"go('practice')\">🧪 <span>Practice</span></button>", "<button onclick=\"go('practice')\">🧪 <span>Practice</span></button>\n    " + nav_item)

# 2. Update the `map` in the `go` function in JS to include 'connect'
content = content.replace("tools:4,practice:5,quiz:6,topics:7", "tools:4,practice:5,connect:6,quiz:7,topics:8")

# 3. Create the new section HTML
new_section = """
<section id="connect">
<div class="section-head"><div><h2>Connect the Dots (The Master Map)</h2><p>Exams test your ability to connect concepts. Here is how Git, DevOps, and Tools all fit into one single workflow.</p></div></div>

<div style="background: rgba(10,15,30,0.7); backdrop-filter: blur(15px); border: 1px solid rgba(0,240,255,0.3); border-radius: 20px; padding: 30px; margin-top: 10px;">
  
  <div style="display: grid; grid-template-columns: 1fr; gap: 20px;">
    
    <!-- Step 1 -->
    <div style="display: flex; gap: 20px; align-items: stretch;">
      <div style="width: 40px; background: rgba(0,240,255,0.1); color: var(--cyan); border: 1px solid var(--cyan); border-radius: 10px; display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 20px;">1</div>
      <div style="flex: 1; padding: 20px; background: rgba(0,0,0,0.4); border-radius: 12px; border-left: 4px solid var(--cyan);">
        <h3 style="color: var(--cyan); margin-bottom: 5px;">The Developer's Laptop (Git Local)</h3>
        <p style="margin: 0; color: #c4d8eb;">You write code. You run <code style="color:#00ffaa;background:#000;padding:2px 6px;border-radius:4px;">git add</code> (Staging) and <code style="color:#00ffaa;background:#000;padding:2px 6px;border-radius:4px;">git commit</code> (Local Repo). <br><em>Concept:</em> Version Control. <em>Tool:</em> Git.</p>
      </div>
    </div>

    <!-- Step 2 -->
    <div style="display: flex; gap: 20px; align-items: stretch;">
      <div style="width: 40px; background: rgba(98,168,255,0.1); color: var(--blue); border: 1px solid var(--blue); border-radius: 10px; display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 20px;">2</div>
      <div style="flex: 1; padding: 20px; background: rgba(0,0,0,0.4); border-radius: 12px; border-left: 4px solid var(--blue);">
        <h3 style="color: var(--blue); margin-bottom: 5px;">Sharing with the Team (Git Remote)</h3>
        <p style="margin: 0; color: #c4d8eb;">You run <code style="color:#00ffaa;background:#000;padding:2px 6px;border-radius:4px;">git push</code>. Your code leaves your laptop and goes to the cloud.<br><em>Concept:</em> Collaboration. <em>Tool:</em> GitHub / GitLab.</p>
      </div>
    </div>

    <!-- Step 3 -->
    <div style="display: flex; gap: 20px; align-items: stretch;">
      <div style="width: 40px; background: rgba(255,234,0,0.1); color: var(--yellow); border: 1px solid var(--yellow); border-radius: 10px; display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 20px;">3</div>
      <div style="flex: 1; padding: 20px; background: rgba(0,0,0,0.4); border-radius: 12px; border-left: 4px solid var(--yellow);">
        <h3 style="color: var(--yellow); margin-bottom: 5px;">The Pipeline Triggers (Continuous Integration)</h3>
        <p style="margin: 0; color: #c4d8eb;">GitHub tells the CI server about your push. The CI server automatically downloads your code, builds it, and runs automated tests (Quality Gates).<br><em>Concept:</em> CI / Automation. <em>Tools:</em> Jenkins, Maven, JUnit.</p>
      </div>
    </div>

    <!-- Step 4 -->
    <div style="display: flex; gap: 20px; align-items: stretch;">
      <div style="width: 40px; background: rgba(0,255,136,0.1); color: var(--green); border: 1px solid var(--green); border-radius: 10px; display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 20px;">4</div>
      <div style="flex: 1; padding: 20px; background: rgba(0,0,0,0.4); border-radius: 12px; border-left: 4px solid var(--green);">
        <h3 style="color: var(--green); margin-bottom: 5px;">Going to Production (Continuous Deployment)</h3>
        <p style="margin: 0; color: #c4d8eb;">The tests passed! The code is packaged into a container and pushed to the live servers so customers can use it.<br><em>Concept:</em> CD / Orchestration. <em>Tools:</em> Docker, Kubernetes, Terraform.</p>
      </div>
    </div>

    <!-- Step 5 -->
    <div style="display: flex; gap: 20px; align-items: stretch;">
      <div style="width: 40px; background: rgba(255,68,102,0.1); color: var(--red); border: 1px solid var(--red); border-radius: 10px; display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 20px;">5</div>
      <div style="flex: 1; padding: 20px; background: rgba(0,0,0,0.4); border-radius: 12px; border-left: 4px solid var(--red);">
        <h3 style="color: var(--red); margin-bottom: 5px;">Watching it Run (Monitoring & Feedback)</h3>
        <p style="margin: 0; color: #c4d8eb;">The app is live. We watch the servers to make sure they don't crash. If they do, an alert is sent back to the developers at Step 1 to fix it.<br><em>Concept:</em> Feedback Loop / DORA metrics. <em>Tools:</em> Prometheus, Grafana.</p>
      </div>
    </div>

  </div>
</div>
</section>
"""

# Insert right before <section id="quiz">
content = content.replace('<section id="quiz">', new_section + '\n<section id="quiz">')

with open('index.html', 'w') as f:
    f.write(content)

print("Connections section added.")
