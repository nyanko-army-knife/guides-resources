# %%
from operator import ne
from pathlib import Path
basetext = Path("content/guides/others/index.md").read_text()
for section in basetext.split("\n## ")[1:-1]:
  header_end = section.find('\n')
  header, maintext = section[:header_end], section[header_end+1:].lstrip("\n")
  maintext = f"---\ntitle: {header}\n---\n" + maintext

  header_slug = header.lower().replace(" ", "-")

  p = Path(f"content/guides/advents/{header_slug}/index.md")
  p.parent.mkdir(parents=True, exist_ok=True)
  p.write_text(maintext)
# %%
