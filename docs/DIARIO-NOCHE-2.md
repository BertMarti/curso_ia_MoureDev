# Diario · noche del 30/09 al 01/10/2026

Registro de trabajo del lead para el reporte final de las 8:00.

## 22:03 · Arranque
- Alberto autoriza: fusionar sin pedir permiso, usar OpenCode con ChatGPT, trabajar hasta las 8:00.
- Mantener el PC despierto activado.
- Fusionados curso_ia_MoureDev #1 (reporte nocturno y PDF v0.1) y #2 (plan fase 3 y herramientas del equipo).
- En curso (v0.3.0): commitling #17 aplicando cambios de revisión; modelduel #20 y #21 en revisión; printquote con agent-project-1 trabajando en #17-#22.
- OmniRoute: servidor arrancado en localhost:20128. Sin claves de proveedor: el proveedor gratuito por defecto (OpenCode Free) rechaza el uso fuera de OpenCode (403). Se integrará en modelduel con pruebas simuladas.

## 22:10-22:45
- OpenCode + GPT-5.6 Terra lanzado (esta vez permitido) para `docs/COMO-PROBAR.md` en curso_ia_MoureDev (rama docs/guia-pruebas-opencode); en segundo plano.
- commitling: revisión de #17 → cambios (solo errores transitorios conservan el SVG) → aplicados → CI verde → fusionado. PR #18 prepara 0.3.0 → fusionado. Release v0.3.0 publicada y `v1` movida a ella.
- Perfil BertMarti: workflow fijado a `@v1`, PR #1 fusionado, workflow ejecutado con éxito (commit 997cf3b «chore: actualiza commitling»).
- modelduel: revisión de #20 y #21 aprobada; enviado ajuste de coste redondeado y nits a agent-project-2.
- printquote: agent-project-1 trabajando en #17-#22.
- 22:45 límite de uso alcanzado.

## Tras el límite
- printquote: agent-project-1 terminó v0.3.0: PRs #23-#28 (cierran #17-#22), CI verde, 304 tests. PDF con Noto Sans y JetBrains Mono (OFL) recortadas y cargadas bajo demanda; metadatos en inglés; aviso OBJ >200 vértices; tope 6M triángulos en 3MF; zoom con +/−; capturas nuevas. Pendiente: revisión (agent-review) y fusión en orden 23→28, release v0.3.0.
- modelduel: pendiente informe de agent-project-2 con el ajuste de coste redondeado; luego fusión #20→#21 y release v0.3.0.
- Nuevo límite de uso alcanzado.

## 02:01 · Reanudación (proceso nuevo: Superpowers, Frontend Design y Ralph Loop ya cargan como skills nativas; Context7 como MCP del plugin pide autorización OAuth, `c7.py` sigue funcionando sin ella)
- modelduel: #20 (con el ajuste de coste redondeado de la revisión) fusionado; #21 tenía conflicto con #20 → `main` fusionado en su rama (sin rebase), ruff + 270 tests en verde, CI verde → fusionado. #22 prepara 0.3.0 → fusionado. Etiquetas `v0.2.0` y `v0.3.0` creadas; **sin release de GitHub** porque dispararía la publicación en PyPI (pendiente de configurar por Alberto).
- printquote: revisión de #23-#28 (agent-review, code-reviewer): todo aprobado, nada bloqueante; recomendada la licencia OFL en el despliegue. Fusionados #23→#28 en orden con CI verde. Encargado PR de pulido v0.3 (licencias OFL en public/, memoización de fuentes, aviso de red, guarda de zoom sin pieza, test de frontera 3MF, comentarios, versión 0.3.0).
- curso_ia_MoureDev #3: `docs/COMO-PROBAR.md` escrito por OpenCode + GPT-5.6 Terra, revisado y fusionado.

## 02:20 · Fase Pro (v0.4.0)
- commitling (agent-project-3): generador en vivo con WebAssembly en la galería (mismo código Go en el navegador), con spec (`agent-skills:spec`), issues (`agent-skills:plan`), TDD y Frontend Design.
- modelduel (agent-project-2): proveedor `omniroute:<modelo>` (preset del proveedor OpenAI, probado con respuestas simuladas) y clasificación pública en la web a partir de resultados versionados.
- printquote (agent-project-1): primero el PR de pulido v0.3; la fase Pro entra después.
- 02:35 printquote: PR #29 de pulido (licencias OFL en public/fonts, memoización de fuentes, aviso de red, guarda de zoom, test de frontera 3MF, versión 0.3.0) fusionado; **release v0.3.0 publicada**; despliegue OK (web, licencia y og.png responden 200).
- 02:36 printquote entra en fase Pro (v0.4.0): PWA instalable sin conexión, historial de presupuestos con exportación CSV y enlace para compartir la configuración.
- modelduel v0.4.0: spec `docs/specs/v0.4.md`, issues #23-#25, PRs #26 (proveedor `omniroute:`), #27 (clasificación agregada y comando `leaderboard`), #28 (publicación en CI y web). CI verde, cobertura 96 %. Skills: spec, plan, TDD, frontend-design, dataviz, verification. En revisión (code-reviewer), con foco en escapado de HTML y rutas de `duelos/<id>`.
- commitling v0.4.0: spec `docs/specs/v0.4.md`, hito y issues #19-#22, PRs #23-#26 (CI verde). Generador en vivo «Pruébalo con tu usuario» en la galería: Go compilado a WebAssembly (≈4,9 MiB, 1,3 MiB gzip, solo se descarga al interactuar), SVG idéntico byte a byte al de la CLI, descarga del SVG y workflow relleno. Refactor `internal/events` para no enlazar `net/http` en el wasm (de 7,1 a 5,1 MB). En revisión con foco en seguridad del formulario y del SVG en el DOM.
- commitling v0.4.0: revisión de #23-#26 aprobada sin bloqueantes (seguridad verificada: login validado antes de la URL, SVG insertado como `<img src=blob:>`, sin innerHTML; eventos hostiles no ejecutan nada). Fusionados #23→#26 con CI verde. Encargado PR de pulido: comillas en `user` del YAML y tema normalizado, regiones accesibles siempre presentes, `ValidLogin` sin regexp (−0,5 MB de wasm), timeout de fetch, `Array.isArray`, reutilización de eventos, descarga del wasm al escribir/enviar, versión 0.4.0.

## 07:13 · Reanudación final
- Reanudados: pulido de commitling v0.4, cierre de printquote v0.4 (PR #33 PWA, #34 historial, enlace para compartir en curso) y revisión de modelduel #26-#28.
- modelduel revisión: #26 aprobado y FUSIONADO (clave de OmniRoute no se filtra, verificado con 8 tipos de fallo). #27 BLOQUEADO por dos XSS reales en `duelos/<id>/index.html` (moneda en el veredicto y contador de fallidos sin escapar) y coste por tarea mal calculado con `--runs` > 1; #28 condicionado. Devuelto al dueño con límite 07:45.
- 07:16 commitling: PR #27 de pulido (comillas en `user`, tema normalizado, regiones accesibles, ValidLogin sin regexp: wasm 4,6 MB / 1,26 MB gzip, timeout y robustez en generator.js, versión 0.4.0) fusionado. **Release v0.4.0** publicada, `v1` movida. Despliegue OK. Probado en la web real: el generador dibuja a @BertMarti y el workflow sale con `user: "BertMarti"`.
- 07:18 printquote: revisión rápida de #33-#35 aprobada sin bloqueantes (service worker con caché versionada y HTML red-primero; enlace con validación de tipos y rangos; CSV con neutralización de fórmulas). Fusionados #33→#35. **Release v0.4.0** publicada. Despliegue OK. Probado en la web real: total 1,59 €, bloque «Presupuestos», botón «Copiar enlace», service worker registrado en /printquote/ y manifiesto servido.
