import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace the previous terrible mobile CSS with an App-like mobile CSS
old_mobile_css = r'@media\(max-width:600px\)\{.*?\n\}'

# The previous script did a replacement like this:
# .replace("</style>", mobile_css + "\n</style>")
# Let's just find everything from @media(max-width:600px) down to the end of style, 
# but there are two 600px media queries. I will just replace ALL @media(max-width:600px) blocks.
# Better to do it via regex, but let's be careful.

# Actually, I'll just write a script to re-do the 600px and 900px queries cleanly.
new_css = """
@media(max-width: 900px) {
  .sidebar { width: 80px; padding: 20px 10px; }
  .logo { font-size: 0; } .logo span { font-size: 20px; }
  .tag, .nav button span, .progress { display: none; }
  .nav button { font-size: 0; text-align: center; padding: 14px 0; }
  .nav button:first-letter { font-size: 22px; }
  .main { margin-left: 80px; width: calc(100% - 80px); padding: 30px 24px; }
  .grid, .grid2, .compare, .topic-list { grid-template-columns: 1fr; }
}

@media(max-width: 700px) {
  /* Completely redesign for phones */
  .sidebar { 
      width: 100% !important; 
      height: auto !important; 
      bottom: auto !important; 
      padding: 12px 10px 5px 10px !important; 
      display: flex !important; 
      flex-direction: column !important; 
      gap: 10px !important;
      border-right: none !important;
      border-bottom: 1px solid rgba(255,126,179,0.3) !important;
      background: rgba(15,5,12,0.98) !important; /* solid enough to hide content scrolling under it */
  }
  .logo { font-size: 18px !important; text-align: center; margin: 0 !important; }
  .logo br { display: none; }
  .logo span:last-child { display: none; } /* hide the "BY N BHARATH" text on mobile to save space */
  
  .nav { 
      display: flex !important; 
      flex-direction: row !important; 
      overflow-x: auto !important; 
      gap: 8px !important; 
      padding-bottom: 10px !important;
  }
  .nav::-webkit-scrollbar { display: none; } /* hide scrollbar for nav */
  
  .nav button { 
      padding: 8px 16px !important; 
      flex-shrink: 0 !important; 
      font-size: 14px !important; 
      background: rgba(255,126,179,0.1) !important; 
      border-radius: 20px !important; 
      border: 1px solid rgba(255,126,179,0.2) !important;
  }
  .nav button span { display: inline !important; font-size: 14px !important; }
  
  .main { 
      margin-left: 0 !important; 
      width: 100% !important; 
      padding: 130px 15px 30px !important; /* pad top to avoid header */
  } 
  
  .top { display: none !important; } /* Hide giant badges and reset button */
  
  .hero-content { padding: 25px 15px !important; }
  h1 { font-size: 32px !important; line-height: 1.1 !important; margin-bottom: 10px !important;}
  .lead { font-size: 16px !important; line-height: 1.5 !important; margin-bottom: 20px !important;}
  .hero { border-radius: 20px !important; }
  
  .card { padding: 16px !important; border-radius: 16px !important; }
  
  .connect-step { flex-direction: column !important; align-items: flex-start !important; gap: 10px !important; }
  .connect-step > div:first-child { width: 30px !important; height: 30px !important; font-size: 14px !important; }
  
  .modalbox { padding: 20px !important; border-radius: 16px !important; width: 95% !important; }
}
"""

# Let's remove the previous 900px and 600px media queries to prevent clashes
content = re.sub(r'@media\(max-width:900px\)\{.*?\}', '', content, flags=re.DOTALL)
content = re.sub(r'@media\(max-width:600px\)\{.*?\}', '', content, flags=re.DOTALL)

# Insert the new ones before </style>
content = content.replace("</style>", new_css + "\n</style>")

with open('index.html', 'w') as f:
    f.write(content)

print("Mobile fixed")
