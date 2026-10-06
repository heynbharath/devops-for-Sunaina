import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace the terminal input with buttons
old_terminal = """<div class="terminal">
          <span class="terminal-prefix">~</span>
          <input type="text" class="terminal-input" id="git-input" placeholder="type 'git add .' and press Enter" autocomplete="off" spellcheck="false">
        </div>"""

new_terminal = """<div class="command-buttons" id="cmd-btns" style="display: flex; gap: 10px; margin-top: 15px; flex-wrap: wrap;">
          <button class="btn" style="background: rgba(255,255,255,0.1); color: var(--primary); padding: 12px 24px; font-family: monospace; border: 1px solid rgba(0,255,170,0.3);" onclick="tryGitCommand('git push')">git push</button>
          <button class="btn" style="background: rgba(255,255,255,0.1); color: var(--primary); padding: 12px 24px; font-family: monospace; border: 1px solid rgba(0,255,170,0.3);" onclick="tryGitCommand('git add')">git add</button>
          <button class="btn" style="background: rgba(255,255,255,0.1); color: var(--primary); padding: 12px 24px; font-family: monospace; border: 1px solid rgba(0,255,170,0.3);" onclick="tryGitCommand('git pull')">git pull</button>
          <button class="btn" style="background: rgba(255,255,255,0.1); color: var(--primary); padding: 12px 24px; font-family: monospace; border: 1px solid rgba(0,255,170,0.3);" onclick="tryGitCommand('git commit')">git commit</button>
        </div>"""
content = content.replace(old_terminal, new_terminal)

# Update the instructions text
content = content.replace("Type the command to move the file forward.", "Click the correct Git command to move your code through the pipeline.")

# Replace the JS logic for the git input
old_js_start = "const gitInput = document.getElementById('git-input');"
old_js_end = "    }\n  });"
pattern = re.compile(re.escape(old_js_start) + r".*?" + re.escape(old_js_end), re.DOTALL)

new_js = """  function tryGitCommand(cmd) {
    const btns = document.getElementById('cmd-btns');
    if(gitState === 0 && cmd === 'git add') {
      moveFile('gb-work', 'gb-stage');
      gitState++;
      gitHint.innerText = "Awesome! It's staged. Now 'record' it to the local repo.";
      gitHint.style.color = "var(--primary)";
    } 
    else if(gitState === 1 && cmd === 'git commit') {
      moveFile('gb-stage', 'gb-local');
      gitState++;
      gitHint.innerText = "Committed! Now share it with the team on GitHub.";
      gitHint.style.color = "var(--primary)";
    }
    else if(gitState === 2 && cmd === 'git push') {
      moveFile('gb-local', 'gb-remote');
      gitState++;
      gitHint.innerText = "Pushed! You've mastered the flow.";
      gitHint.style.color = "var(--primary)";
      document.getElementById('btn-2').style.display = 'block';
      confetti({ particleCount: 100, spread: 70, origin: { y: 0.6 } });
    }
    else {
      if (gitState === 0) gitHint.innerText = "Not quite! To move code out of the Working Directory, you must stage it first.";
      else if (gitState === 1) gitHint.innerText = "Not quite! It's staged, but you need to record it locally before sharing.";
      else if (gitState === 2) gitHint.innerText = "Not quite! It's saved locally. Now send it to the remote server.";
      gitHint.style.color = "var(--danger)";
      btns.style.animation = 'none';
      setTimeout(() => btns.style.animation = 'shake 0.4s', 10);
    }
  }"""

content = re.sub(pattern, new_js, content)

# Remove the focus logic in nextScreen
content = content.replace("    if(currentScreen === 2) {\n      document.getElementById('git-input').focus();\n    }", "")

with open('index.html', 'w') as f:
    f.write(content)

print("Replaced terminal with interactive buttons.")
