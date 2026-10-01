
**1. Los 5 problemas estéticos/UX más importantes**

| # | Archivo / elemento | Problema | Mejora propuesta |
|---|---|---|---|
| 1 | `index.html.tmpl` · hero `header img` (línea 43) | Imagen estática 112×112 sin animación; la criatura "viva" solo aparece tras rellenar formulario. El visitante no ve la promesa del producto al aterrizar. | Cambiar `img` por `picture` con SVG animado de ejemplo (moss ancient radiant) que respire/parpadee al cargar; usa `prefers-reduced-motion`. |
| 2 | `index.html.tmpl` · generador `#gen-stage` (líneas 68-73) | Contenedor con `min-height:226px` y borde `dashed` rompe la estética "papel y píxel"; el SVG resultante (480×200) queda centrado en caja mayor, generando espacio muerto vertical. | Igualar alto del contenedor a 200px, quitar borde `dashed`, usar `background:var(--paper)` y sombra sutil `box-shadow:0 1px 0 var(--line)` para mantener papel. |
| 3 | `generator.js` · `ensureWasm()` (líneas 87-99) | Carga perezosa solo al `input` en el formulario; si el usuario hace clic directo en "Dibujar" sin teclear, espera descarga completa (4.6 MB) con spinner genérico "Cargando el generador…". | Precargar `wasm` en `IntersectionObserver` cuando `#generador` entra en viewport; mostrar progreso real (`fetch` `progress` event) y permitir cancelar. |
| 4 | `render.go` · animaciones CSS (líneas 286-315) | Saltos (`hop`) y respiración (`breathe`) usan `transform:translateY` en el grupo `.bob` completo; en tema oscuro el outline (papel) se mueve con el cuerpo, rompiendo la ilusión de "sticker". | Separar capa outline (`.o`) de cuerpo/ojos; animar solo `.body+.eyes`; mantener outline fijo para efecto pegatina. |
| 5 | `index.html.tmpl` · galería `#galeria` (líneas 213-223) | Grid de 2 columnas fijo; en móvil (`max-width:720px`) pasa a 1 columna pero las imágenes 480×200 requieren scroll horizontal si el viewport < 500px por `width="480"`. | Quitar `width/height` en `img` de galería; usar `max-width:100%;height:auto` y `aspect-ratio:12/5` en CSS; `object-fit:contain`. |

---

**2. Propuesta concreta: «Modo demo en tiempo real»**

**Qué ve el visitante (segundo a segundo):**
- **0–1 s**: Al entrar en `#generador`, la hero muestra ya un SVG animado (ej. `@demo` moss ancient radiant) respirando y con destellos.
- **1–2 s**: Aparece un banner superior no intrusivo: «Prueba en vivo sin escribir tu usuario →» (botón secundario).
- **Al clic**: El formulario se autollenna con `demo-octocat` (usuario ficticio predefinido), especie `moss`, tema `light`; el botón cambia a «Generando…» y se desactiva.
- **2–4 s**: Se descarga WASM si no está en caché (con barra de progreso real); se usan eventos **fixture locales** (`testdata/events.json` servidos como `/demo/events.json`, sin red).
- **4–5 s**: SVG aparece en `#gen-stage` con animación completa; caption: «Demo: @demo-octocat · 2 500 XP · racha 12 días · accesorios: gorro, bufanda, flor».
- **5 s en adelante**: Botones radio especie/tema **reactivos** (redibujan al instante sin red); botón «Descargar SVG» y workflow prellenado funcionan.
- **Detener**: Banner muestra «Volver a mi usuario» (restaura formulario vacío) o el usuario escribe otro nombre y pulsa Enter (cancela demo, pide a GitHub).

**Activación:** Un clic en el banner o check `?demo=1` en URL. **Datos:** Fixture estático `testdata/events.json` (usuario `octoexample`) servido desde `/demo/events.json`; sin token, sin petición a GitHub, determinista.

---

**3. Riesgos de accesibilidad/rendimiento de la demo**

- **Rendimiento**: WASM (4.6 MB / 1.3 MB gzip) se descarga aunque el usuario no la use si precargas en `IntersectionObserver`; solución: `link rel="preload" as="fetch" crossorigin` solo tras interacción real (hover/focus en formulario) y `Cache-Control: immutable, max-age=31536000` en CDN.
- **Accesibilidad (AA)**: 
  - Animaciones automáticas en hero y demo violan `prefers-reduced-motion: reduce` si no se respetan en el SVG de ejemplo; el CSS del `render.go` ya lo hace (`@media (prefers-reduced-motion:reduce){*{animation:none!important}}`), pero el hero `img` estático no lo hereda → usar `picture` con `source[media="(prefers-reduced-motion:reduce)"]` apuntando a SVG estático.
  - Cambio de especie/tema por radio buttons debe anunciar cambio vía `aria-live="polite"` en `#gen-caption` (ya existe) y mantener foco en el control accionado.
  - Contraste del banner demo: fondo `--paper` / texto `--ink` cumple 7:1; botón secundario debe tener `border:2px solid var(--ink)` y `:focus-visible` visible.
- **Memoria**: `URL.createObjectURL` en `show()` revoca el anterior, pero si el usuario alterna especie/tema rápido se crean blob URLs huérfanas; solución: `revokeObjectURL` inmediato tras `img.src = nuevo` (ya está en línea 135).
