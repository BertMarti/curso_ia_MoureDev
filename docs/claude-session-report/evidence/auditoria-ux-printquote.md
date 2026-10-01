
Auditoría visual en curso: reviso la identidad y la interfaz actual sin tocar nada.
1. `index.html` cabecera `#open-button` + `#sample-button`: dos botones iguales compiten; el primario naranja pierde jerarquía. Dejar solo «Abrir» como `button--primary` y la muestra como `link-button` secundario.
2. `src/styles.css` `.summary` solo `sticky` en móvil (línea 1288): en escritorio el total 40px se pierde tras 7 bloques de `src/ui/app.ts` `render()`. Hacerlo `sticky bottom:0` también en escritorio.
3. `index.html` `.stage-meta` + `.notice` + `.empty#empty-state`: aviso `top:64px` tapa nombre de pieza y texto vacío centrado; jerarquía confusa al cargar. Reservar banda superior solo para aviso/error y atenuar `empty-text`.
4. `src/styles.css` `.field input` 30px, `.range` 22px, `.bed-inputs input` 3.6em: dianas <44px y cama X/Y/Z apretada en 400px de `.panel`. Subir a 40-44px y apilar cama en móvil sin romper retícula recta.
5. `index.html` `#stage-hint[aria-hidden=true]` + `#stage-dims[aria-hidden=true]`: ayuda de órbita/zoom y medidas solo visual; lector de pantalla y teclado (OrbitControls en `src/ui/app.ts:167`) quedan sin instrucciones. Duplicar ayuda en `aria-label` del `#viewer` y no ocultar dims.
Demo en vivo (solo local, sin servidor/claves):
6. Activación: tercer botón `index.html#tb-actions` «Ver demo» junto a muestra; `aria-pressed`, respeta `prefers-reduced-motion` (no autoarranca si reduce movimiento).
7. s0-2: carga `public/samples/soporte-movil.stl` ya precacheado, `stage-loading` visible y órbita lenta; s2-5: rellena PLA→PETG, relleno 20→40% con `NumberField.set`; s5-8: rota cámara, recalcula `computeQuote`, total en `aria-live`; fin: pausa y deja estado editable.
8. Parada: cualquier `pointerdown/keydown` en visor o panel, segundo clic o `Esc` detiene (`clearInterval`, devuelve foco al botón); nunca pisa `localStorage`.
9. Datos: solo STL local + `DEFAULT_SETTINGS` y `PRINTERS`; three.js ya diferido en `src/ui/app.ts:162`, sin fetch ni Worker extra.
Riesgos:
10. Accesibilidad AA: movimiento automático, parpadeo `pq-blink`, verborrea de `live-status`/`warnings[aria-live]`; mitigar con pausa visible, `aria-live=off` durante demo y un solo anuncio final.
11. Rendimiento: three.js ~500kB + órbita continua sube CPU/batería en móvil; limitar a 1 ciclo, `requestAnimationFrame` con visibilidad y `matchMedia`, reutilizar malla ya analizada.
