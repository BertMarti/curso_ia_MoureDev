import subprocess


def gh(*a, inp=None):
    r = subprocess.run(["gh", *a], input=inp, capture_output=True, text=True, encoding="utf-8")
    if r.returncode:
        print("ERR", a[:4], r.stderr.strip()[:200])
    return r.stdout.strip()


def body(ctx, crit):
    return (ctx + "\n\n## Criterios de aceptación\n" + "\n".join(f"- [ ] {c}" for c in crit)
            + "\n\n_Hito v0.3.0 · creada por el lead (Claude Code)._")


ISSUES = {
    "printquote": [
        ("PDF con fuente incrustada para cualquier alfabeto", body(
            "El PDF solo admite WinAnsi: cirílico, griego y otros caracteres salen como «?». Incrustar una fuente libre (licencia OFL) con buena cobertura usando `@pdf-lib/fontkit`, cargada bajo demanda junto con pdf-lib para no aumentar el JS inicial.",
            ["Texto en español, cirílico y griego se ve correctamente en el PDF",
             "Fuente con licencia libre, incluida en el repositorio con su licencia",
             "El JS inicial no crece (la fuente y fontkit solo se descargan al pulsar «Descargar PDF»)",
             "Test que genera un PDF con texto no latino y comprueba que no hay «?»"])),
        ("Metadatos Open Graph y Twitter en inglés", body(
            "Las metaetiquetas de la página siguen en español cuando la interfaz está en inglés. Deben actualizarse al cambiar de idioma y usar los textos del diccionario.",
            ["og:title, og:description, twitter:* y description cambian con el idioma",
             "Test que comprueba los metadatos en ambos idiomas"])),
        ("Aviso en OBJ con polígonos cóncavos muy grandes", body(
            "Los polígonos OBJ de más de 200 vértices se triangulan en abanico sin aviso, lo que puede falsear superficie y visor si son cóncavos.",
            ["Aviso visible y accesible si hay polígonos de más de 200 vértices",
             "Traducido en es/en", "Test del aviso"])),
        ("Tope de triángulos en 3MF", body(
            "Un 3MF con muchas instancias puede superar la memoria y acabar en un RangeError genérico.",
            ["Límite de triángulos totales documentado", "Error claro y traducido al superarlo",
             "Test con un 3MF sintético que lo supera"])),
        ("Zoom con teclado en el visor", body(
            "El visor se puede girar y desplazar con el teclado, pero no acercar ni alejar.",
            ["Teclas + y − (y equivalentes) acercan y alejan con el visor enfocado",
             "Indicado en la pista de controles", "Respeta prefers-reduced-motion"])),
        ("Captura del README con la interfaz de v0.2", body(
            "`docs/captura.png` muestra la interfaz de v0.1.0, sin perfiles de impresora ni datos del negocio.",
            ["Captura nueva generada con la pieza de ejemplo", "README y og.png coherentes con la interfaz actual"])),
    ],
    "commitling": [
        ("Conservar el último SVG válido ante caídas largas de la API", body(
            "Tras 3 reintentos (unos 7 s) el cliente se rinde y la ejecución diaria falla. En la Action conviene no romper el perfil: si la API no responde, conservar el SVG anterior y terminar con un aviso, no con error.",
            ["Opción `--keep-on-error` en la CLI y entrada `keep-on-error` en la Action (por defecto activada en la Action)",
             "Si falla la API y existe el archivo de salida, se conserva intacto y el paso termina con un aviso",
             "Si no existe archivo previo, el error se mantiene",
             "Tests de ambos casos y documentación en README y docs/USO.md"])),
    ],
}

for repo, issues in ISSUES.items():
    R = f"BertMarti/{repo}"
    gh("api", f"repos/{R}/milestones", "-f", "title=v0.3.0", "-f", "description=Tercera fase", "--silent")
    for title, b in issues:
        print(repo, gh("issue", "create", "-R", R, "--title", title, "--label", "agent:builder",
                       "--label", "enhancement", "--milestone", "v0.3.0", "--body-file", "-", inp=b), title)
