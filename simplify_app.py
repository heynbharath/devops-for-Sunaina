import re

with open('index.html', 'r') as f:
    content = f.read()

# Swap Screen 2 (Git) with Screens 3 and 4
screen2 = re.search(r'<!-- Screen 2: Git Simulator -->.*?</div>\s*</div>\s*<!-- Screen 3: CI/CD -->', content, re.DOTALL).group(0).replace('<!-- Screen 3: CI/CD -->', '')
screen3 = re.search(r'<!-- Screen 3: CI/CD -->.*?</div>\s*</div>\s*<!-- Screen 4: Quality Gates & DORA -->', content, re.DOTALL).group(0).replace('<!-- Screen 4: Quality Gates & DORA -->', '')
screen4 = re.search(r'<!-- Screen 4: Quality Gates & DORA -->.*?</div>\s*</div>\s*<!-- Screen 5: Final -->', content, re.DOTALL).group(0).replace('<!-- Screen 5: Final -->', '')

# Replace the IDs to match the new order
new_screen2 = screen3.replace('id="screen-3"', 'id="screen-2"').replace('id="btn-3"', 'id="btn-2"')
new_screen2 = new_screen2.replace('<h2>3.', '<h2>2.')

new_screen3 = screen4.replace('id="screen-4"', 'id="screen-3"').replace('id="btn-4"', 'id="btn-3"')
new_screen3 = new_screen3.replace('<h2>4.', '<h2>3.')

new_screen4 = screen2.replace('id="screen-2"', 'id="screen-4"').replace('id="btn-2"', 'id="btn-4"')
new_screen4 = new_screen4.replace('<h2>2.', '<h2>4.')

# Update the Git logic to have easier hints and highlight the correct button if wrong
new_js_logic = """  function tryGitCommand(cmd) {
    const btns = document.getElementById('cmd-btns');
    
    // Clear old highlights
    Array.from(btns.children).forEach(b => b.style.boxShadow = 'none');

    if(gitState === 0 && cmd === 'git add') {
      moveFile('gb-work', 'gb-stage');
      gitState++;
      gitHint.innerText = "Awesome! Stage 1 complete. Next: Record it with 'commit'.";
      gitHint.style.color = "var(--primary)";
    } 
    else if(gitState === 1 && cmd === 'git commit') {
      moveFile('gb-stage', 'gb-local');
      gitState++;
      gitHint.innerText = "Awesome! Stage 2 complete. Finally: Share it with 'push'.";
      gitHint.style.color = "var(--primary)";
    }
    else if(gitState === 2 && cmd === 'git push') {
      moveFile('gb-local', 'gb-remote');
      gitState++;
      gitHint.innerText = "You did it! That's the whole workflow.";
      gitHint.style.color = "var(--primary)";
      document.getElementById('btn-4').style.display = 'block';
      confetti({ particleCount: 100, spread: 70, origin: { y: 0.6 } });
    }
    else {
      // Highlight the correct button as a massive hint
      let correctBtn = "";
      if (gitState === 0) {
          gitHint.innerText = "Hint: You always 'add' files before doing anything else.";
          correctBtn = "git add";
      }
      else if (gitState === 1) {
          gitHint.innerText = "Hint: Now you need to 'commit' your changes.";
          correctBtn = "git commit";
      }
      else if (gitState === 2) {
          gitHint.innerText = "Hint: The last step is to 'push' to GitHub.";
          correctBtn = "git push";
      }
      
      gitHint.style.color = "var(--danger)";
      
      // Flash the correct button
      Array.from(btns.children).forEach(b => {
          if(b.innerText === correctBtn) {
              b.style.boxShadow = "0 0 20px var(--primary)";
          }
      });

      btns.style.animation = 'none';
      setTimeout(() => btns.style.animation = 'shake 0.4s', 10);
    }
  }"""

# Reconstruct the HTML
new_content = content.replace(screen2 + screen3 + screen4, new_screen2 + new_screen3 + new_screen4)

# Replace the tryGitCommand logic
pattern = re.compile(r'function tryGitCommand\(cmd\).*?setTimeout\(\(\) => btns.style.animation = \'shake 0.4s\', 10\);\n    }\n  }', re.DOTALL)
new_content = re.sub(pattern, new_js_logic.strip(), new_content)

with open('index.html', 'w') as f:
    f.write(new_content)

print("Simplified and reordered app.")
