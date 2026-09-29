# Reporte nocturno · 29-30 de septiembre de 2026

Diario de todo lo que ha hecho el equipo de agentes mientras dormías. Empieza por el **Resumen**; el detalle cronológico está debajo.

## Resumen

**Las 3 aplicaciones están terminadas, revisadas y documentadas, con los 9 pull requests en verde. Falta solo publicarlas, y eso tienes que hacerlo tú:** el sistema de permisos de Claude Code no me deja fusionar en `main`, y el despliegue a GitHub Pages se lanza al fusionar.

| Proyecto | Stack | PRs (todos con CI en verde) | Tests | Web (tras fusionar) | PDF |
|---|---|---|---|---|---|
| **printquote** | TypeScript + Vite + three.js | [#1 builder](https://github.com/BertMarti/printquote/pull/1) → [#2 qa](https://github.com/BertMarti/printquote/pull/2) → [#3 docs](https://github.com/BertMarti/printquote/pull/3) | 132 | https://bertmarti.github.io/printquote/#ejemplo | [printquote.pdf](proyectos/printquote.pdf) |
| **modelduel** | Python 3.12 | [#1 builder](https://github.com/BertMarti/modelduel/pull/1) → [#2 qa](https://github.com/BertMarti/modelduel/pull/2) → [#3 docs](https://github.com/BertMarti/modelduel/pull/3) | 132 (94 % cobertura) | https://bertmarti.github.io/modelduel/ (demo en `/demo/`) | [modelduel.pdf](proyectos/modelduel.pdf) |
| **commitling** | Go 1.27 + GitHub Action | [#1 builder](https://github.com/BertMarti/commitling/pull/1) → [#2 qa](https://github.com/BertMarti/commitling/pull/2) → [#3 docs](https://github.com/BertMarti/commitling/pull/3) | ✓ (Ubuntu, Windows y prueba de la Action) | https://bertmarti.github.io/commitling/ | [commitling.pdf](proyectos/commitling.pdf) |

Capturas de las tres en [`capturas/`](capturas/). Trabajo terminado sobre la **01:00**, muy antes de las 8:00.

### Qué tienes que hacer tú (en este orden)

**1. Fusionar y publicar.** En cada repositorio, fusiona los PR en orden. Con `--delete-branch`, al borrar la rama base GitHub reorienta solo el siguiente PR a `main`:

```bash
for r in printquote modelduel commitling; do for n in 1 2 3; do gh pr merge $n -R BertMarti/$r --merge --delete-branch; done; done
```

Si algún PR no se ha reorientado a `main` (lo verás porque falla el merge), cámbialo con `gh pr edit <n> -R BertMarti/<repo> --base main` y repite. Al terminar, cada fusión lanza su despliegue en Pages. Revisa la pestaña **Actions** de cada repo y abre las tres URLs de la tabla.

**2. Comprobar.** printquote con `#ejemplo`; modelduel y su `/demo/`; commitling con la criatura en vivo de tu usuario (hasta el primer despliegue, la imagen del README sale rota).

**3. Opcionales:**
- **commitling en tu perfil:** crear `BertMarti/BertMarti` (si no existe) y añadir el workflow de `docs/USO.md`. No lo he tocado porque es tu perfil público.
- **Etiqueta `v1` de commitling** y cambiar `@main` por `@v1` en README, galería y `docs/USO.md`.
- **modelduel con APIs reales:** probarlo una vez con tus claves (Gemini, OpenAI…). Solo se ha probado con respuestas simuladas.
- **printquote:** comparar peso y tiempo con tu laminador para ajustar el caudal por defecto; revisar la impresión en Firefox o Safari y probar con un lector de pantalla.
- **Permisos de Claude Code**, si quieres más autonomía la próxima vez:
  - fusionar PRs (`gh pr merge`);
  - lanzar OpenCode en modo autónomo (`opencode run --auto`).

  Ambas cosas las bloqueó el sistema esta noche.

### Lo que no salió como estaba previsto
- **No pude fusionar ni, por tanto, desplegar**: el sistema de permisos bloquea `gh pr merge` hacia `main`.
- **OpenCode y ChatGPT no participaron**: lanzar OpenCode en modo autónomo también fue bloqueado («agentes sin supervisión»). La documentación la hizo Claude **Sonnet**, y el QA de commitling también (más barato que Opus). Los README ya lo cuentan así.
- **Límite de uso** entre ~23:45 y 00:30: los 3 QA se cortaron a medias. Se reanudaron sin perder trabajo.
- He instalado **Go 1.27** en tu PC (con `winget`, paquete oficial).

## Equipo

| Agente | Herramienta | Rama | Cometido |
|---|---|---|---|
| lead | Claude Code (sesión principal, Opus 5.5) | `main` (solo merges) | Plan, repositorios, revisión, integración, despliegue, PDFs y este reporte |
| builder ×3 | Claude Code (subagentes, uno por proyecto) | `agent/builder` | MVP, tests, CI y despliegue |
| qa ×3 | Claude Code (Opus en printquote y modelduel; Sonnet en commitling) | `agent/qa` | Revisión, tests de casos límite, fallos y accesibilidad |
| docs ×3 | Claude Code (Sonnet). Previsto: OpenCode, bloqueado | `agent/docs` | Guía de uso `docs/USO.md` y `CONTRIBUTING.md` |

## Proyectos

| Proyecto | Stack | Repositorio | Web |
|---|---|---|---|
| printquote | TypeScript + Vite + three.js | https://github.com/BertMarti/printquote | https://bertmarti.github.io/printquote/ |
| modelduel | Python 3.12 (stdlib) | https://github.com/BertMarti/modelduel | https://bertmarti.github.io/modelduel/ |
| commitling | Go 1.27 (stdlib) + GitHub Action | https://github.com/BertMarti/commitling | https://bertmarti.github.io/commitling/ |

## Diario

### Preparación (lead)
- Instalado **Go 1.27** con `winget` (paquete oficial `GoLang.Go`) porque no estaba en el PC y commitling usa Go.
- Creados los 3 repositorios locales en `D:\Desarrollos\` con: `README.md`, `AGENTS.md` (stack, estructura, diseño y reglas del equipo), `CLAUDE.md` (importa `AGENTS.md` y `MEMORY.md`), `MEMORY.md`, `opencode.json` (hace que OpenCode cargue `MEMORY.md`), licencia MIT, plantilla de PR y `.gitattributes` (finales de línea LF).
- Regla en todos los `AGENTS.md`: **cada agente actualiza `MEMORY.md` al terminar**; si no, la sesión no cuenta como terminada.
- Publicados en GitHub como **públicos**, con descripción, topics y web.
- **GitHub Pages** activado en modo «GitHub Actions» en los tres.
- **`main` protegida** con un ruleset: no se puede borrar ni forzar, y todo entra por pull request.
- Lanzados los 3 agentes **builder** en paralelo, cada uno en su rama `agent/builder`.
- Comprobado que **OpenCode** trabaja sin supervisión (`opencode run --auto`) con el modelo gratuito `opencode/muse-spark-1.3-contributor-free`: crea y edita archivos en la carpeta donde se lanza. Será el agente **docs**.
- Preparado el generador de PDFs por proyecto (reportlab): uso, técnica, flujo con diagrama, funcionalidades, monetización, acciones para Alberto y anexo con el código.

### modelduel · builder terminado
- PR [BertMarti/modelduel#1](https://github.com/BertMarti/modelduel/pull/1) «feat: MVP de modelduel»: 13 commits convencionales, 68 tests, CI en verde en Ubuntu y Windows.
- Revisión del lead: el runner ejecuta el código generado en un directorio temporal, en subproceso con timeout, sin stdin y quitando del entorno las variables que parecen secretos. Aprobado.
- **Bloqueo:** el sistema de permisos de Claude Code **no me deja fusionar en `main`** (repositorio público y protegido). No lo he forzado. Consecuencia: **las webs no se publican hasta que fusiones los PR tú** (el despliegue se lanza al actualizar `main`).
- Solución adoptada: los agentes siguientes trabajan **en cadena** (qa parte de `agent/builder`, docs parte de `agent/qa`) y sus PR apuntan a la rama anterior. Por la mañana fusionas en orden y se despliega todo.
- Lanzado el agente **qa** de modelduel en `agent/qa` (parte de `agent/builder`): runner en Windows, `--runs`, errores de proveedores, escapado y accesibilidad del informe.
- Borrador del PDF de modelduel generado (40 páginas); se regenerará con el código final.

### printquote · builder terminado
- PR [BertMarti/printquote#1](https://github.com/BertMarti/printquote/pull/1) «feat: MVP de printquote»: 14 commits, 57 tests, CI en verde en Ubuntu y Windows.
- Revisión del lead: parser STL propio (binario y ASCII), volumen, área, caja, avisos de malla abierta y de cama, presupuesto completo, visor three.js, «copiar» e «imprimir», pieza de ejemplo original (soporte de móvil low-poly). Diseño «hoja técnica suiza» conseguido (captura en `docs/capturas/printquote.png`). Aprobado.
- Lanzado el agente **qa** de printquote en `agent/qa`: parseo en Web Worker, soldado de vértices con tolerancia, valores extremos, accesibilidad, metadatos y móvil.
- Borrador del PDF de printquote generado; se regenerará con el código final.

### commitling · builder terminado
- PR [BertMarti/commitling#1](https://github.com/BertMarti/commitling/pull/1) «feat: MVP de commitling»: CI en verde (tests en Ubuntu y Windows + prueba de la propia Action con el fixture y con tu usuario real).
- Revisión del lead: generé la galería en local y revisé las 48 variantes. La criatura es un **diseño original** (un brote de musgo que crece hasta árbol ancestral) con 5 fases, 4 ánimos y 3 accesorios. Capturas en `docs/capturas/commitling-*.png`. Hoy tu criatura real sería **Brote, contento, ~170 XP**. Aprobado.
- Lanzado el agente **qa** de commitling en `agent/qa`: versiones de acciones (Node 20 obsoleto), tipografía y desbordes del SVG, casos límite de estadísticas y de la API, accesibilidad de la galería y entradas de la Action.
- Borrador del PDF de commitling generado; los PDF incluyen ya capturas de las apps.

### Incidencia: límite de uso (≈ 23:45 → 00:30)
- Los 3 agentes **qa** se cortaron a medias al agotarse el uso de la sesión. Se restableció a las 00:30.
- Estado al cortarse: printquote con cambios sin confirmar en el parser; modelduel con 2 commits locales (matar el árbol de procesos y acotar la salida; BOM y tests rotos); commitling sin empezar.
- 00:32 · Reanudados los qa de printquote y modelduel desde su contexto (mismo agente), con hora límite 07:30 y orden de empujar a menudo.

### Incidencia: OpenCode autónomo bloqueado
- Intenté que el qa de commitling lo hiciera **ChatGPT (GPT-5.6 Terra) mediante OpenCode** en modo `--auto`, para repartir el gasto como pediste. El sistema de permisos de Claude Code lo **bloqueó** («crear agentes sin supervisión»). No lo he forzado ni buscado otra vía.
- Consecuencia: esta noche **OpenCode/ChatGPT no participa**. El qa de commitling lo hace un subagente de **Claude Sonnet** (más barato que Opus) y la guía de uso (`docs/USO.md`) la hará también un subagente de Claude.
- Si quieres que OpenCode trabaje solo en futuras noches, tendrás que permitirlo tú en la configuración de permisos de Claude Code, o lanzar tú OpenCode.

### commitling · qa terminado
- PR [BertMarti/commitling#2](https://github.com/BertMarti/commitling/pull/2) «test: revisión QA de commitling» (base `agent/builder`): 7 commits, CI en verde (Ubuntu, Windows y prueba de la Action). Hecho por Claude **Sonnet**.
- Hallazgos corregidos:
  - acciones actualizadas a las últimas versiones (checkout v7, setup-go v7, Pages v5/v6) porque Node 20 está obsoleto;
  - el texto del SVG se desbordaba con usuarios largos o XP grandes; ahora se ajusta de forma determinista;
  - un gris con contraste insuficiente (3,3:1) pasa a 4,8:1;
  - cliente HTTP con `User-Agent` correcto y timeout también en clientes construidos a mano;
  - **eventos duplicados al paginar** que contaban XP dos veces;
  - galería con Open Graph completo y botón de copiar accesible con alternativa.
- Revisión visual del lead: tarjetas clara y oscura correctas tras los ajustes; la criatura no cambia. Aprobado.
- Lanzado el agente **docs** de commitling (Claude Sonnet) en `agent/docs` (parte de `agent/qa`): `docs/USO.md`, `CONTRIBUTING.md` y enlaces en el README.

### modelduel · qa terminado
- PR [BertMarti/modelduel#2](https://github.com/BertMarti/modelduel/pull/2) «test: revisión QA de modelduel» (base `agent/builder`): CI en verde en Ubuntu y Windows; **132 tests (antes 68), cobertura 94 %** con mínimo del 90 % exigido en el CI.
- Hallazgos corregidos:
  - **procesos nietos que colgaban el runner en Windows** y sobrevivían; ahora se mata el árbol completo con un Job Object en Windows o un grupo de procesos en Linux/macOS;
  - salida enorme acotada;
  - tareas con BOM;
  - tests rotos que culpaban a los modelos;
  - cortes de red que tumbaban el duelo;
  - **HTML sin escapar en el informe** (inyección con un results.json manipulado);
  - el marcador usaba el total de A para los dos;
  - contraste insuficiente del perdedor;
  - CLI en español con códigos de salida coherentes.
- Lanzado el agente **docs** de modelduel (Claude Sonnet) en `agent/docs` (parte de `agent/qa`).

### commitling · docs terminado
- PR [BertMarti/commitling#3](https://github.com/BertMarti/commitling/pull/3) «docs: guía de uso y guía de contribución» (base `agent/qa`): `docs/USO.md` (instalación en 4 pasos, reglas con ejemplos, FAQ y solución de problemas), `CONTRIBUTING.md`, enlaces en el README y fila del agente docs actualizada en AGENTS.md. CI en verde. Hecho por Claude Sonnet.
- El agente verificó cada regla contra el código y señaló matices: «Contento» son hoy, ayer o anteayer en UTC; la XP puede bajar porque solo cuentan 90 días. Los explica la guía.
- Lead: corregida la sección «Cómo se ha hecho» del README para no atribuir a OpenCode un trabajo que no ha hecho.

### printquote · qa terminado
- PR [BertMarti/printquote#2](https://github.com/BertMarti/printquote/pull/2) «test: revisión QA de printquote» (base `agent/builder`): **132 tests (antes 57)**, CI en verde en Ubuntu y Windows.
- Hallazgos corregidos:
  - STL con BOM;
  - nombres de sólido con palabras clave;
  - números fuera de float32;
  - binario con recuento 0;
  - **ASCII grandes que ocupaban ~800 MB** (ahora tokenizador byte a byte);
  - falsos avisos de malla abierta (soldado con tolerancia);
  - **parseo en Web Worker** (720.000 triángulos en 0,8 s sin bloquear);
  - **visor cargado bajo demanda** (JS inicial de 580 kB a 26 kB);
  - **el desglose no sumaba el total** (ahora se redondea por líneas, como en una factura);
  - avisos accesibles con regiones vivas;
  - Open Graph;
  - aviso de pieza en metros o pulgadas.
- Lanzado el agente **docs** de printquote (Claude Sonnet) en `agent/docs`.

### modelduel · captura
- Captura del informe de demostración generada con Chrome sin interfaz: `docs/capturas/modelduel.png`.
- PDF final de commitling generado desde `agent/docs` (código final de la cadena): `docs/proyectos/commitling.pdf`.

### modelduel · docs terminado
- PR [BertMarti/modelduel#3](https://github.com/BertMarti/modelduel/pull/3) (base `agent/qa`): `docs/USO.md` (instalación en PowerShell y Linux/macOS, duelos con Gemini, OpenAI, OpenRouter y Ollama, tarea nueva `es_palindromo` paso a paso, FAQ y solución de problemas), `CONTRIBUTING.md`, enlaces en el README y en la web. CI en verde. Hecho por Claude Sonnet, que comprobó todos los mensajes citados ejecutando la herramienta.
- Nota: los enlaces a `docs/USO.md` desde la web apuntan a `main`, así que darán 404 hasta que fusiones.
- Lead: corregido el crédito del equipo en README y web (no atribuir a OpenCode).

### printquote · docs terminado
- PR [BertMarti/printquote#3](https://github.com/BertMarti/printquote/pull/3) (base `agent/qa`): `docs/USO.md` de 14 secciones con cifras comprobadas en la app con la pieza de ejemplo (123,83 cm³, 59,3 g, 1 h 45 min, 1,59 €) y guía de calibración con el laminador; `CONTRIBUTING.md`; README con el equipo real. CI en verde. Hecho por Claude Sonnet.

### Cierre (lead)
- Plantilla de PR corregida en los 3 repos (`opencode-docs` → `docs`). CI de los 3 PR de docs en verde tras el cambio.
- PDF finales regenerados desde el código final (`agent/docs`) con capturas: printquote (44 págs.), modelduel (46) y commitling (46), en `docs/proyectos/`.
- Todo este material (reporte, PDFs, capturas y la guía general `Guia-Proyectos-con-IA.pdf`) se sube a `curso_ia_MoureDev` en la rama `docs/reporte-nocturno` con su PR.
