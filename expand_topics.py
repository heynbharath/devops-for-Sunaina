import re

expanded_topics = [
    ["Introduction to DevOps", "DevOps (Development + Operations) is a mindset, culture, and set of technical practices. It aims to bridge the gap between software developers (who want to ship features fast) and IT operations (who want stability and no crashes). By uniting these teams, organizations can build, test, and release software faster, more frequently, and more reliably."],
    ["Need and Benefits of DevOps", "Traditionally, Dev and Ops worked in silos, leading to slow deployments, finger-pointing when things broke, and manual errors. DevOps solves this by introducing automation and shared responsibility. Benefits include faster time-to-market, lower failure rates of new releases, shortened lead time for fixes, and faster recovery times (MTTR)."],
    ["DevOps Culture and Collaboration", "A successful DevOps transition is 80% culture and 20% tools. It requires shared ownership (Devs care about how code runs in production, Ops care about the code itself), transparent communication, and blameless post-mortems (learning from failures instead of punishing people)."],
    ["DevOps Principles", "The core principles can be summarized by CAMS: Culture, Automation, Measurement, and Sharing. It emphasizes continuous improvement, small batch sizes (releasing tiny changes often rather than huge updates once a year), automated testing, and constant feedback loops."],
    ["DevOps Lifecycle", "The lifecycle is an infinite loop that represents continuous delivery. The phases generally include: Plan, Code, Build, Test, Release, Deploy, Operate, and Monitor. The 'infinite loop' shape shows that monitoring feedback directly informs the planning of the next code change."],
    ["DevOps Lifecycle Stages", "Each stage relies on the previous one. <b>Plan/Code</b>: Developers write code and commit. <b>Build/Test</b>: CI servers compile code and run automated tests. <b>Release/Deploy</b>: CD tools push the validated code to staging/production. <b>Operate/Monitor</b>: Infrastructure runs the app while monitoring tools watch for errors."],
    ["Continuous Integration (CI)", "Continuous Integration is the practice where developers frequently merge their code changes into a central repository (like GitHub). Every merge automatically triggers a build and automated testing sequence. This ensures that new code doesn't break the existing application. Memory Hook: Integrate code + Validate it automatically."],
    ["Continuous Delivery (CD)", "Continuous Delivery takes CI one step further. After code is built and tested, it is automatically prepared for a release to a production environment. The code is kept in a 'ready to release' state at all times. However, the final push to production still requires a human to click 'Approve' or 'Deploy'."],
    ["Continuous Deployment", "Continuous Deployment is the ultimate level of automation. Every code change that passes all the automated CI tests and quality gates is automatically deployed directly to production, with zero human intervention. Memory Hook: Code goes from developer's laptop to production completely automatically."],
    ["CI vs CD vs Continuous Deployment", "<b>CI (Integration)</b>: Developers merge code; automated tests run.<br><b>CD (Delivery)</b>: Code is validated and sits in a staging area, completely ready to go live whenever a human decides.<br><b>Continuous Deployment</b>: The code automatically goes live to customers without any human clicking 'deploy'."],
    ["Automation in DevOps", "Automation removes human error and speeds up repeatable tasks. In DevOps, you automate everything you can: code compilation, unit testing, security scanning, infrastructure provisioning (Infrastructure as Code), and server configuration. The goal is consistency and speed."],
    ["DevOps Metrics and DORA Metrics", "DORA (DevOps Research and Assessment) defined 4 key metrics to measure DevOps success:<br>1. <b>Deployment Frequency</b> (How often you release)<br>2. <b>Lead Time for Changes</b> (Time from commit to production)<br>3. <b>Change Failure Rate</b> (Percentage of releases that break things)<br>4. <b>Time to Restore Service</b> (How fast you recover from crashes)."],
    ["Quality Gates", "A predefined pass/fail checkpoint in a CI/CD pipeline. For example, a quality gate might say 'Do not allow deployment if code coverage is below 80%' or 'Fail the build if critical security vulnerabilities are found.' They act as automated bouncers protecting production."],
    ["DevOps Tools and Their Purpose", "Tools belong to categories. Source Control: Git. Code Hosting: GitHub/GitLab. CI/CD: Jenkins, GitHub Actions. Containers: Docker. Container Orchestration: Kubernetes. Infrastructure as Code: Terraform. Monitoring: Prometheus, Grafana. Learn the category, not just the tool name!"],
    ["Monitoring and Feedback", "Deploying code isn't the end; it's the beginning. Monitoring (using logs, metrics, and traces) watches application health in production. If a bug happens, monitoring alerts the team. This feedback loop allows developers to fix issues quickly in the next cycle."],
    ["Introduction to Git", "Git is a distributed version control system (VCS) created by Linus Torvalds. It tracks changes made to files over time, allowing multiple developers to collaborate, revert to previous versions, and work in isolated branches without overwriting each other's work."],
    ["Version Control System (VCS)", "A system that records changes to a file or set of files over time so that you can recall specific versions later. It prevents the 'final_v2_really_final.txt' problem. Git is a 'distributed' VCS, meaning every developer has a full copy of the entire history on their local machine."],
    ["Git vs GitHub vs GitLab", "<b>Git</b> is the actual underlying software/command-line tool that tracks changes on your local computer.<br><b>GitHub and GitLab</b> are remote, cloud-based hosting platforms where you can upload (push) your Git repositories to share them with other developers and manage CI/CD."],
    ["Git Repository", "A Git repository (repo) is essentially a database where Git stores all the history, commits, branches, and metadata for a project. It lives in a hidden folder called `.git` inside your project directory. If you delete the `.git` folder, the files remain, but the history is gone."],
    ["Working Directory, Staging Area and Repository", "Git has 3 main areas. <b>1. Working Directory</b>: Where you actually edit files. <b>2. Staging Area (Index)</b>: A waiting room where you select which modified files will go into the next commit. <b>3. Local Repository</b>: Where Git permanently saves the committed snapshots."],
    ["Basic Git Workflow", "The holy grail sequence:<br>1. <code>git status</code> (check what you changed)<br>2. <code>git add .</code> (move changes to the staging area)<br>3. <code>git commit -m \"message\"</code> (record the staged changes permanently locally)<br>4. <code>git push</code> (upload your local commits to GitHub)."],
    ["Git Configuration", "Before using Git, you must tell it who you are, because every commit is stamped with an author. You set this using: <code>git config --global user.name \"Sunaina\"</code> and <code>git config --global user.email \"email@domain.com\"</code>."],
    ["git init", "The command used to transform a normal, empty directory on your computer into a brand new Git repository. It creates the hidden `.git` folder that starts tracking your project."],
    ["git status", "The most frequently used Git command. It tells you the current state of your working directory and staging area. It shows which files are modified, which are staged for the next commit, and which are untracked."],
    ["git add", "Moves changes from the Working Directory to the Staging Area. <code>git add file.txt</code> stages a specific file. <code>git add .</code> stages all current modifications. It tells Git, 'I want these changes to be included in my next commit snapshot.'"],
    ["git commit", "Takes everything in the staging area and permanently records it as a snapshot in the local repository's history. Every commit requires a message explaining what changed. Example: <code>git commit -m \"Fix login button bug\"</code>."],
    ["git log", "Displays the chronological history of all commits in the repository. It shows the commit hash (the unique ID), the author, the date, and the commit message. Useful for seeing what happened in the past."],
    ["git clone", "Downloads a complete copy of a remote repository (like from GitHub) onto your local machine. It downloads all the files, all the branches, and the entire history, automatically linking your local repo to the remote one."],
    ["git push", "Uploads all your local commits to a remote repository (e.g., GitHub). This is how you share your recorded work with the rest of your team. You cannot push if someone else has pushed changes that you haven't downloaded yet."],
    ["git pull", "Downloads new commits from the remote repository and immediately integrates (merges) them into your current local working branch. It is a shortcut for running <code>git fetch</code> followed by <code>git merge</code>."],
    ["git fetch", "Downloads new data/commits from the remote repository to your local machine, BUT it does NOT automatically merge or change your working files. It lets you safely inspect what colleagues have done before you integrate their work."],
    ["Git Branches", "A branch is an independent, parallel timeline of development. Developers create branches to work on new features or bug fixes without breaking the main, stable codebase (usually called 'main' or 'master')."],
    ["Branch Creation and Switching", "Use <code>git branch [name]</code> to create a new branch. Use <code>git checkout [name]</code> or <code>git switch [name]</code> to jump into that branch. <code>git checkout -b [name]</code> does both: creates it and switches to it immediately."],
    ["Git Merge", "The process of combining the history and changes from one branch into another. For example, once a feature is finished on the `feature/login` branch, you merge it into the `main` branch so it becomes part of the final product."],
    ["Merge Conflicts", "Occurs when two developers edit the exact same line of the same file, or one edits a file while the other deletes it. Git pauses the merge because it doesn't know which change to keep. A human must manually open the file, resolve the conflict, and commit the final decision."],
    [".gitignore", "A text file placed in the repository that tells Git exactly which files or folders it should completely ignore. Usually used for passwords, API keys, large compiled binaries, and system files (like `.DS_Store` or `node_modules`)."],
    ["git diff", "Shows the exact line-by-line differences between files. It can show the difference between your working directory and the staging area, or between two different commits. Very useful for reviewing your code before you `git add` it."],
    ["git reset vs git revert", "<b>git reset</b> moves the history pointer backwards, essentially erasing local history (dangerous if shared).<br><b>git revert</b> creates a brand NEW commit that perfectly undoes the changes of a previous bad commit (very safe, preserves history)."],
    ["Fork and Pull Request", "<b>Forking</b> creates a personal copy of someone else's GitHub repository under your own account.<br>A <b>Pull Request (PR)</b> is a formal request asking the original project owner to 'pull' your finished changes from your fork/branch into their main repository."],
    ["GitHub/GitLab Collaboration Workflow", "The industry standard way teams work:<br>1. Clone/Fork the repo.<br>2. Create a new branch.<br>3. Make edits, stage, and commit.<br>4. Push the branch to GitHub.<br>5. Open a Pull Request.<br>6. Team reviews the code.<br>7. CI runs automated tests.<br>8. Merge into main."]
]

with open('index.html', 'r') as f:
    content = f.read()

# Generate the new JS array string
import json
new_topics_js = "const topics = " + json.dumps(expanded_topics, indent=2) + ";"

# Replace the old topics array
# Find the start of const topics=[ and the end of ];
start_idx = content.find('const topics=[')
if start_idx != -1:
    end_idx = content.find('];', start_idx) + 2
    old_topics_str = content[start_idx:end_idx]
    
    # Replace it
    content = content.replace(old_topics_str, new_topics_js)
    
    with open('index.html', 'w') as f:
        f.write(content)
    print("Topics expanded successfully.")
else:
    print("Could not find topics array.")
