# %%
from pathlib import Path
import glob

from markdownify import markdownify as md
# %%
flist = glob.glob("data/documents/*.html")
# %%
for fname in flist:
  dest = fname.removesuffix(".html") + ".md"
  fl = Path(fname).read_text()
  flmd = md(fl, wrap=False, wrap_width=120)
  Path(dest).write_text(flmd)
