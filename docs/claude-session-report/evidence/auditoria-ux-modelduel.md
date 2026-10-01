
**1. Cinco problemas**
1. `site/index.html:115-119` `.duel-bars`: barras casi idénticas (97/94/94 de 100) que no comunican nada, cifras sin letra y `aria-hidden`, cuando AGENTS.md exige «la letra siempre acompaña al color»; además son datos fijos que se desincronizarán de `demo/` y `leaderboard/`. → Cada fila con su letra («A 31/32»), escala real del marcador o retirarlas.
2. `site/index.html:120-124` `.cta`: tres botones con el mismo peso, el primario lleva al informe **estático** y nada invita a probar la app; el nav (`site/index.html:97-109`) apila 8 enlaces monoespaciados sin jerarquía. → Primario «Probar la demo en vivo», resto secundario, y sección `#demo` propia.
3. `src/modelduel/report/style.css:24` el subrayado de los enlaces del informe usa `--line` (#2a2a2f), invisible sobre el fondo (el index usa `--muted`, `site/index.html:27`), y falta la regla `a:focus-visible` que sí existe en `site/index.html:29`; los informes solo enlazan a GitHub (`template.html:67-71`, `league.html:57-61`), así que `/demo/` es un callejón sin salida. → Subrayado `--muted`, foco global y enlace «modelduel · web» en el pie.
4. `site/index.html:188` (tabla de proveedores) es desplazable pero sin `tabindex="0" role="region" aria-label` ni `:focus-visible`, mientras `template.html:50` y `league.html:24,46` sí lo hacen: el foco de teclado se pierde en el scroll horizontal. → Repetir atributos y regla de foco en el CSS del index.
5. `src/modelduel/report/style.css:75-76,167` el «perdedor» de cada métrica se marca solo con `opacity:.8` (información por color que recorta contraste) y `.mark`/`th`/`.hint` están a 9-11 px. → Marcar con glifo+texto (▲ «mejor»), sin opacidad, y tipografía mínima 11 px.

**2. Modo demo en tiempo real (sin servidor ni claves)**
- **Datos:** ya generados por el CI en `site/demo/results.json` (enunciado, `code`, `latency_s`, `input/output_tokens`, `passed/total`, `cost` por tarea y contendiente). Se incrustan como `<script type="application/json">` o se traen con un `fetch` diferido tras el clic. Cero backend, cero claves, cero ejecución real (Pyodide queda descartado por «nada de librerías nuevas») y queda explícito «resultado pregrabado».
- **Dónde:** sección `#demo` en `site/index.html` reutilizando el CSS existente (`.duel-bars`, `.metric`, `.board`), sin dependencias nuevas.
- **Segundo a segundo (~25 s, contador `00:07` en monoespaciada):** 0-3 s aparece el enunciado de `slugify`; 3-12 s tres paneles A/B/C escriben su `code` grabado a ritmo proporcional a `latency_s` mientras suben los contadores de tokens; 12-20 s caen los tests uno a uno con ✓/✗ (`passed/total`) y crecen las barras; 20-25 s marcador, coste (ficticios, ya marcado) y enlace «Ver informe completo» a `demo/`.
- **Activación:** botón «Iniciar demo», sin auto-arranque (carga perezosa del script). **Parada:** botón «Pausa/Detener» siempre visible (`clearTimeout`/`AbortController`), fin automático al completarse y con `visibilitychange`; con `prefers-reduced-motion` no hay tipeo, sino pasos manuales «Siguiente».
- **Sin JS:** la sección degrada a un párrafo con enlace al informe estático.

**3. Riesgos**
- WCAG 2.2.2 (contenido en movimiento >5 s): exige pausa visible y no auto-arrancar; ya cubierto, pero hay que probarlo con teclado.
- Contadores con `aria-live` = ruido para lectores de pantalla: anunciar solo cambios de fase (`polite`), números en `aria-hidden` con resumen final estático.
- No robar foco ni scroll al iniciar; el foco permanece en el botón.
- Estados ✓/✗ por color solo → siempre glifo + texto, como las letras de la liga.
- Rendimiento: el tipeo carácter a carácter provoca reflow → escribir en un `<pre>` con `overflow:auto` a ~10 fps, no incrustar JSON gigante en la portada (fetch diferido) y detener todo al terminar; la sección engorda el HTML inicial de GitHub Pages.
