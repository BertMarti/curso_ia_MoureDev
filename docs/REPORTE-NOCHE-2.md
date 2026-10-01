# Reporte y auditoría · noche del 30/09 al 01/10/2026

Lo que ha hecho el equipo de agentes desde las 22:03 hasta las 08:00, cómo funciona cada aplicación, qué ha mejorado, cómo comprobarlo y qué queda pendiente.

## 1. Resumen

| Proyecto | Versión publicada | Web | Estado de la v0.4.0 «Pro» |
|---|---|---|---|
| **printquote** | [v0.4.0](https://github.com/BertMarti/printquote/releases/tag/v0.4.0) (y v0.3.0 esta noche) | https://bertmarti.github.io/printquote/ | **Publicada y probada en la web**: app instalable sin conexión, historial de presupuestos con CSV, enlace para compartir |
| **modelduel** | v0.4.0 (etiqueta; release de GitHub pendiente de PyPI) | https://bertmarti.github.io/modelduel/ · [clasificación](https://bertmarti.github.io/modelduel/leaderboard/) | **Publicada**: proveedor `omniroute:` y clasificación pública de modelos |
| **commitling** | [v0.4.0](https://github.com/BertMarti/commitling/releases/tag/v0.4.0) + `v1` | https://bertmarti.github.io/commitling/ · [generador](https://bertmarti.github.io/commitling/#generador) | **Publicada y probada en la web**: generador en vivo con WebAssembly |

- **Webs:** las cinco URLs comprobadas a las 07:15 responden 200: printquote, modelduel, la demo de modelduel, commitling y su imagen para redes. El CI y los despliegues de `main` están en verde en los tres repos.
- **Volumen de la noche:** más de 25 PR fusionados en total, entre los tres proyectos, tu perfil y el repositorio del curso. Cada PR de funcionalidad pasó por un agente revisor antes de fusionarse.
- **Tu perfil:** usa `BertMarti/commitling@v1` y su workflow se ejecutó con éxito.

## 2. Cómo ha trabajado el equipo

| Agente | Herramienta | Cometido |
|---|---|---|
| lead | Claude Code (Opus) | Plan, reparto, revisión de informes, fusiones, releases, integración entre repos y este reporte |
| agent-project-1 | Claude Code (Sonnet) | Dueño exclusivo de printquote |
| agent-project-2 | Claude Code (Sonnet) | Dueño exclusivo de modelduel |
| agent-project-3 | Claude Code (Sonnet) | Dueño exclusivo de commitling |
| agent-review | Agente `agent-skills:code-reviewer` (Sonnet) | Revisión de cada lote de PR en cinco ejes: corrección, legibilidad, arquitectura, seguridad y rendimiento. Más Ponytail. Solo lectura |
| docs | OpenCode + GPT-5.6 Terra | Guía `docs/COMO-PROBAR.md` del repositorio del curso |

**Flujo:**
1. Issues con criterios de aceptación en un hito.
2. Una rama y un PR por issue contra `main`, con `Closes #n`.
3. CI en Ubuntu y Windows.
4. Revisión por agent-review.
5. Correcciones del dueño.
6. Fusión por el lead.
7. PR de preparación de release (versión y CHANGELOG), release y despliegue en Pages.

**Herramientas usadas de verdad:**
- **Agent Skills:** `spec` y `plan` para las especificaciones v0.4 y sus issues, y el agente `code-reviewer`.
- **Superpowers:** TDD (tests en rojo antes de implementar), verificación antes de completar y brainstorming.
- **Frontend Design:** en la UI del generador de commitling, la clasificación de modelduel y los avisos de printquote. Además, `dataviz` en la clasificación.
- **Graphify:** un grafo por proyecto en `graphify-out/`, ignorado en git, para orientarse y medir el impacto de los cambios.
- **Context7:** pdf-lib y fontkit, Actions compuestas, `syscall/js` y wasm. Se usó con `equipo/c7.py`, porque el MCP del plugin pide autorización OAuth.
- **Ponytail:** criterio permanente; la revisión busca también sobreingeniería.

**Incidencias:**
- **Límites de uso:** la noche se cortó hacia las 22:45 y las 02:50. El trabajo se reanudó desde el contexto de cada agente sin perder nada.
- **Ralph Loop:** no se usó. Funciona con el hook de parada de la sesión principal y no debe anidarse en subagentes.
- **OmniRoute:** no pudo usarse con modelos reales. No hay claves de proveedor, y su proveedor gratuito por defecto (OpenCode Free) rechaza el uso fuera de OpenCode con un 403.

## 3. Cronología

- **22:03.** Fusionados en el curso #1 (reporte anterior) y #2 (plan de la fase 3 y herramientas del equipo).
- **22:10-22:45 · commitling.** La revisión del #17 (conservar la criatura si cae la API) detecta que también se conservaba ante errores permanentes. Se corrige para que solo cuente lo transitorio (5xx, 429, red). Después se fusionan #17 y #18 (versión 0.3.0), se publica la **release v0.3.0** y se mueve `v1`.
- **22:10-22:45 · perfil.** El workflow se fija a `@v1`, se fusiona su PR y se ejecuta con éxito.
- **22:10-22:45 · modelduel.** Se revisan #20 y #21. El ajuste del coste redondeado queda pedido a su dueño.
- **02:01-02:35 · modelduel.** Se fusionan #20 (veredicto y clasificación con el mismo criterio) y #21 (aviso de reintento en formato español), después de resolver el conflicto entre ambos. Luego #22 (versión 0.3.0) y las etiquetas `v0.2.0` y `v0.3.0`.
- **02:01-02:35 · printquote.** Revisión de #23 a #28 sin nada bloqueante, fusión en orden y PR de pulido #29. **Release v0.3.0** desplegada.
- **02:01-02:35 · curso.** Se fusiona el #3, la guía de pruebas escrita por OpenCode.
- **02:20-02:50 · fase Pro.**
  - commitling: especificación, issues #19 a #22 y PR #23 a #26. Revisados con la seguridad verificada en navegador y fusionados. Queda encargado el PR de pulido.
  - modelduel: especificación, issues #23 a #25 y PR #26 a #28, que pasan a revisión.
  - printquote: empieza su v0.4 con los PR #33 y #34.
- **07:13.** Reanudación tras el segundo límite y cierre (§6).

## 4. Auditoría por aplicación

### 4.1 printquote: presupuestos de impresión 3D en el navegador

**Cómo funciona:**
1. Arrastras un STL, OBJ o 3MF. El archivo se lee en el navegador, dentro de un Web Worker, y **nunca se sube a ningún servidor**.
2. Calcula volumen, superficie, dimensiones y triángulos, y avisa si la malla está abierta, si tiene polígonos grandes o si no cabe en la cama.
3. Muestra la pieza en un visor three.js.
4. Con el material, el relleno, los perímetros, el caudal, la energía, el margen y las copias, saca el peso, el tiempo **estimado** y el precio, con un desglose que suma exacto, como una factura.
5. Desde ahí copias el presupuesto, lo imprimes o lo **descargas en PDF** con los datos de tu negocio e IVA.

**Mejoras de esta noche (v0.3.0):**
- **PDF que admite latín extendido, griego y cirílico.** Usa Noto Sans y JetBrains Mono, de licencia OFL, recortadas a 224 kB y cargadas solo al pulsar «Descargar PDF». La carga inicial no crece: sigue en unos 78 kB de JavaScript.
- **Metadatos para redes en inglés** cuando la interfaz está en inglés.
- **Aviso en OBJ** con polígonos de más de 200 vértices.
- **Tope de 6 millones de triángulos en 3MF**, comprobado antes de reservar memoria y con un error claro en los dos idiomas.
- **Zoom con las teclas + y −.** No interfiere con los campos numéricos ni con los atajos del navegador.
- **Capturas nuevas** del README y de la imagen para redes.
- **Pulido tras la revisión:**
  - las licencias OFL se sirven en la web (obligatorio);
  - aviso específico si falla la descarga de la fuente;
  - la fuente no se descarga dos veces;
  - el zoom no actúa sin pieza;
  - test del límite exacto del 3MF.

**Calidad:**
- **Tests:** 308 en verde.
- **CI:** lint, typecheck, tests y build en Ubuntu y Windows.
- **Dependencias:** `npm audit --omit=dev` sin vulnerabilidades. `@pdf-lib/fontkit` tiene licencia MIT y no trae dependencias.
- **Revisión:** los 6 PR aprobados.

**Cómo probarlo:**
1. Abre https://bertmarti.github.io/printquote/#ejemplo. Con los valores por defecto, el total es **1,59 €**.
2. Cambia a **EN** y comprueba que la interfaz y los formatos cambian.
3. Elige un perfil de impresora y comprueba que cambian el caudal, la potencia y la cama.
4. Abre «Datos del negocio», escribe un nombre con letras griegas o cirílicas y pulsa **Descargar PDF**. Deben verse bien.
5. Pulsa en el visor y prueba **+** y **−**.

### 4.2 modelduel: enfrenta modelos de IA con tus tests

**Cómo funciona:**
1. Le das una carpeta de tareas: cada una tiene un enunciado y tests de pytest.
2. Pide el código a 2 o más modelos (`replay` grabado, `gemini`, `openai` compatible y, en la v0.4, `omniroute`).
3. Ejecuta los tests de cada respuesta en un directorio temporal: subproceso con límite de tiempo, árbol de procesos acotado y entorno sin variables secretas.
4. Genera un informe HTML sin JavaScript, con el marcador, el veredicto, el coste y el detalle de cada tarea.

**Mejoras de esta noche (v0.3.0):**
- **El veredicto de dos y la clasificación usan una sola función de ordenación**: tareas resueltas, luego tests y luego coste. El texto dice qué criterio decide, por ejemplo «gana A por tests superados (31 frente a 30, con las mismas tareas resueltas)».
- **Los costes se comparan redondeados**, así que dos costes que se muestran iguales empatan.
- **Aviso de reintento en formato español** («1,2 s»).

**Calidad:**
- **Tests:** 270 con la cobertura por encima del 90 %, que exige el CI.
- **CI:** ruff, formato, tests, demo y paquete (sdist y wheel) en Ubuntu y Windows.
- **Revisión:** la del veredicto comprobó 324 combinaciones a fuerza bruta sin encontrar ninguna discrepancia.

**Cómo probarlo:**
1. Abre https://bertmarti.github.io/modelduel/demo/: el informe muestra 31/32 frente a 30/32 y el veredicto con su criterio.
2. En local:

   ```bash
   git clone https://github.com/BertMarti/modelduel && cd modelduel
   python -m venv .venv && .venv/Scripts/activate
   pip install -e ".[dev]"
   modelduel run examples/tasks --a replay:alfa --b replay:beta --model replay:gamma --out runs/liga
   ```

### 4.3 commitling: mascota pixel-art original para tu perfil de GitHub

**Cómo funciona:**
1. Una GitHub Action lee tus eventos públicos.
2. Calcula experiencia, racha, días activos y repositorios.
3. Dibuja una tarjeta SVG animada con CSS, que GitHub muestra en el README. Hay dos especies de diseño propio, el brote de musgo y el hongo, cada una con 5 fases, 4 ánimos y 3 accesorios.
4. Con los mismos datos sale siempre el mismo SVG.

**Mejoras de esta noche:**
- **v0.3.0:** si la API de GitHub cae, la Action **conserva la última criatura en vez de fallar**, pero solo ante errores transitorios (5xx, 429 y red). Con un token caducado o un usuario inexistente sigue fallando, a propósito.
- **v0.4.0, fusionada en `main`:** **generador en vivo**. En la galería escribes cualquier usuario y su criatura se genera en tu navegador con el mismo código Go compilado a WebAssembly, que se descarga solo al usar el generador.
  - El SVG sale idéntico byte a byte al de la CLI.
  - Tiene botón de descarga y el workflow relleno con tu usuario.
  - Seguridad verificada en navegador: el usuario se valida antes de llamar a la API y la criatura se inserta como imagen, así que no puede ejecutar código. Eventos con `<script>` no ejecutan nada.

**Calidad:**
- **CI:** gofmt, vet, tests y build del wasm en Ubuntu y Windows, más la prueba de la propia Action.
- **Versión publicada:** release v0.3.0, con `v1` apuntando a ella.

**Cómo probarlo:**
1. Abre https://bertmarti.github.io/commitling/ y mira las dos especies.
2. Si la v0.4 ya está desplegada (§6), ve a **#generador**, escribe `BertMarti` y cambia de especie y de tema.
3. Mira tu perfil: https://github.com/BertMarti

## 5. Lo que no se ha comprobado (honestidad)

- **OmniRoute** no se ha llamado con modelos reales: no hay claves de proveedor.
- **Gemini y OpenAI** en modelduel solo se han probado con respuestas simuladas.
- **printquote:** no se ha probado con un lector de pantalla real (NVDA o VoiceOver), ni la impresión en Firefox o Safari, ni con archivos OBJ y 3MF reales de laminadores.
- **El PDF con fuentes** se verificó renderizándolo en local, pero no descargándolo desde la web publicada.

## 6. Cierre de la v0.4.0 «Pro» (07:13-07:30)

Las tres v0.4.0 se cerraron, revisadas y probadas, antes de las 07:30.

### printquote v0.4.0: herramienta para talleres
- **Especificación:** `docs/specs/v0.4.md`, con las issues #30, #31 y #32.
- **PR:** [#33](https://github.com/BertMarti/printquote/pull/33) app instalable (PWA), [#34](https://github.com/BertMarti/printquote/pull/34) historial de presupuestos y [#35](https://github.com/BertMarti/printquote/pull/35) enlace para compartir, incluida la versión 0.4.0.
- **Revisión:** sin bloqueantes. Ningún cambio necesario. Lo que comprobó:
  - el service worker usa caché versionada por hash, borra las cachés viejas y pide el HTML primero a la red, así que no puede atrapar la web en una versión antigua;
  - su ámbito es `/printquote/`;
  - el enlace valida tipos y rangos de todo lo que lee de la URL y no guarda nada sin querer;
  - el CSV neutraliza la inyección de fórmulas (`= + - @`) y las filas del historial se pintan como texto.
- **Comprobado en la web publicada:** total de 1,59 €, bloque «Presupuestos», botón «Copiar enlace», service worker registrado en `/printquote/` y manifiesto servido.
- **Coste:** el JavaScript inicial pasa de 80 a 93 kB (de 28 a 32 kB comprimido). El precaché de la app (~0,76 MB) se descarga después de cargar la página.

### commitling v0.4.0: generador en vivo
- **Especificación:** `docs/specs/v0.4.md`, con las issues #19 a #22.
- **PR:** [#23](https://github.com/BertMarti/commitling/pull/23) a [#26](https://github.com/BertMarti/commitling/pull/26) y el pulido [#27](https://github.com/BertMarti/commitling/pull/27).
- **Revisión:** sin bloqueantes, con la seguridad verificada en navegador. El pulido aplicó todo lo recomendado:
  - el usuario va entre comillas en el workflow (logins como `007` o `true` no se malinterpretan en YAML);
  - las regiones accesibles están siempre presentes;
  - `ValidLogin` sin `regexp`, que deja el WebAssembly en 4,6 MB (1,26 MB comprimido);
  - tiempo límite en las peticiones y reutilización de los eventos;
  - la descarga del WebAssembly solo empieza al escribir o enviar.
- **Publicación:** release v0.4.0, con `v1` movida a ella. Tu perfil la usa sin cambios.
- **Comprobado en la web publicada:** el generador dibuja a @BertMarti en el navegador (la criatura se inserta como imagen *blob*) y el workflow sale con `user: "BertMarti"`.

### modelduel v0.4.0: benchmark con OmniRoute y clasificación pública
- **Especificación:** `docs/specs/v0.4.md`, con las issues #23 a #25.
- **PR:** [#26](https://github.com/BertMarti/modelduel/pull/26) proveedor `omniroute:`, [#27](https://github.com/BertMarti/modelduel/pull/27) clasificación y comando `modelduel leaderboard`, [#28](https://github.com/BertMarti/modelduel/pull/28) publicación en CI y web, y [#29](https://github.com/BertMarti/modelduel/pull/29) versión 0.4.0.
- **La revisión bloqueó el #27 por dos fallos de seguridad (XSS) reales.** Con un `results.json` manipulado se podía inyectar código en los informes publicados, a través de la moneda en el veredicto y del contador de tests fallidos. Detectó también que el coste por tarea se calculaba mal con `--runs` > 1.
- **Corrección:** se arregló con un test de regresión que analiza todo el HTML generado. El CI busca ahora scripts en toda la clasificación. Además, lo comprobé yo con un modelo llamado `<script>alert(1)</script>`: **0 scripts sin escapar**.
- **Publicación:** etiqueta `v0.4.0`. La release de GitHub queda pendiente porque dispara la publicación en PyPI.
- **Comprobado en la web publicada:** `/modelduel/leaderboard/` responde con los resultados de ejemplo (contendientes grabados con precios ficticios).

### PDF
Los tres PDF de [`proyectos/`](proyectos/) se han regenerado con el código final de `main` y una sección nueva, «Novedades de la noche del 30/09 al 01/10».

## 7. Acciones para ti, Alberto

1. **PyPI (modelduel).** Crea el *pending publisher* en pypi.org y el environment `pypi` en GitHub. Después crea la release `v0.3.0` o la siguiente, y eso desbloquea las issues #18 y #19.
2. **OmniRoute (opcional).** Conecta al menos un proveedor gratuito con `omniroute keys add <proveedor> <clave>` (Gemini, Groq u OpenRouter) para hacer duelos reales con `omniroute:<modelo>`.
3. **Context7.** Si quieres el MCP nativo, autorízalo con `/mcp` en un terminal `claude`.
4. **Pruebas manuales:**
   - el PDF con letras griegas o cirílicas desde la web;
   - una pasada con lector de pantalla;
   - un OBJ o 3MF de tu laminador.
5. **Marketplace (opcional).** Publica la Action de commitling desde la release (requiere aceptar el acuerdo de GitHub).
