# Auditoría de rendimiento web · v0.6 · 01/10/2026

Agente: `agent-skills:web-performance-auditor` (Sonnet), solo lectura. Medición: curl (gzip) + Chrome headless por CDP, móvil 390×844 Slow-4G (1,6 Mbps, 150 ms RTT, CPU ×4) y escritorio sin límites. No medido: CrUX, INP real, Lighthouse oficial. GitHub Pages fija `max-age=600` y solo gzip.

| | Carga inicial (gz) | FCP / LCP móvil | FCP / LCP escritorio | CLS | Bloqueante |
|---|---|---|---|---|---|
| printquote | 185,9 KB (7 recursos; visor three.js 139 KB diferido) | 748-824 ms | 300 ms | 0 | solo CSS (5,1 KB) |
| modelduel | 13,0 KB (2 recursos) | 904 ms | 364 ms | 0 | solo HTML |
| commitling | 17,6 KB (5 recursos; wasm 1,3 MB gz solo con interacción) | 588 / 736 ms | 364 ms | 0 | solo HTML |

## Hallazgos accionables
1. **printquote · `src/sw.js`**: el `install` precachea con `cache: 'reload'` y vuelve a descargar los `assets/*` con hash que la página acaba de pedir (net-log: index, css y viewer pedidos 2 veces). Usar `'default'` para `/assets/`: −≈177 KB gz en la primera visita (medido).
2. **commitling · `generator.js`**: empezar a bajar el wasm con `pointerdown` en el formulario (intención), no solo con la primera tecla. Gana el tiempo entre tocar y teclear (no medido) sobre una descarga de 6,4 s en Slow-4G.
3. **commitling · `generator.js`**: pedir `commitling.wasm` en paralelo con `wasm_exec.js` (hoy en serie): −≈176 ms en Slow-4G.
4. **modelduel**: sin mejoras de rendimiento medibles. Fuera de rendimiento: faltan `og:image` y `twitter:card` en `site/index.html`.

## Descartado
- printquote: `modulepreload` del visor (compite con el CSS crítico), aplazar el visor (se pierde el estado vacío), comprimir og.png (no lo carga la página), precalentar el PDF (≈620 KB gz a quien quizá nunca lo pida; decisión de producto, no se aplica).
- commitling: `fetchpriority` en el hero (LCP a 148 ms del FCP), reducir el wasm (no cuantificable sin compilar; TinyGo es herramienta nueva).

## Ya está bien
Sin fuentes web en los tres, sin scripts síncronos en `<head>`, CLS 0, imágenes con `width/height`, carga perezosa del visor/PDF/wasm, `<picture>` por esquema de color, animaciones solo de `transform`/`opacity` con `prefers-reduced-motion`.
