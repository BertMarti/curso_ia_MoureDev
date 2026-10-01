"""Renderiza los .mmd de esta carpeta a PNG con Mermaid en Chrome sin interfaz.
Uso: python render.py nombre.mmd [ancho alto]"""
import pathlib, subprocess, sys, html
src = pathlib.Path(sys.argv[1]).resolve()
w, h = (sys.argv[2], sys.argv[3]) if len(sys.argv) > 3 else ("1400", "1000")
page = src.with_suffix(".html")
page.write_text(f"""<!doctype html><meta charset="utf-8"><style>body{{margin:0;background:#fff;font-family:Arial}}
#d{{padding:24px}}</style><div id="d"><pre class="mermaid">{html.escape(src.read_text(encoding='utf-8'))}</pre></div>
<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
<script>mermaid.initialize({{startOnLoad:true,theme:'neutral',flowchart:{{htmlLabels:true}}}});</script>""", encoding="utf-8")
chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
subprocess.run([chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--virtual-time-budget=8000",
                f"--window-size={w},{h}", f"--screenshot={src.with_suffix('.png')}", page.as_uri()], check=True,
               capture_output=True)
page.unlink()
print("OK", src.with_suffix(".png"))
