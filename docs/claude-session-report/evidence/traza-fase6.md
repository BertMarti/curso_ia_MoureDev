# Traza · fase v0.6 · 01/10/2026

Formato: HORA · AGENTE → PROYECTO → TAREA → HERRAMIENTA/SKILL → ACCIÓN → RESULTADO

## Punto de partida
- Las tres apps en v0.5.0, `main` en verde, desplegadas.
- Deuda conocida (REPORT.md §15-16): commitling desborda a 320 px; capturas del duelo en directo de modelduel obsoletas; og.png/captura de printquote sin regenerar; tests de commitling que comparan cadenas exactas de CSS.

## Plan v0.6.0
- printquote: presupuesto por lotes (varias piezas en un mismo presupuesto, con copias por pieza) + og.png y captura actualizadas.
- modelduel: exportar el resultado de un duelo a Markdown (`modelduel report --format md`) para pegarlo en PRs/issues + capturas del duelo en directo actualizadas.
- commitling: tarjeta compacta opcional (`size: compact`, entrada nueva retrocompatible) + desborde a 320 px + tests de CSS menos frágiles.
- Transversal: auditoría de rendimiento de las 3 webs publicadas (agente `agent-skills:web-performance-auditor`) como entrada para el pulido.

## Registro
- lead → los 3 → lanzar v0.6.0 → Agent (general-purpose, Sonnet) ×3 con spec/plan/TDD/frontend-design/graphify/verification → en curso.
- lead → las 3 webs → auditoría de rendimiento → Agent `agent-skills:web-performance-auditor` (solo lectura, mide con curl/Chrome) → en curso.
- agent-project-3 → commitling → v0.6.0 → spec, plan, TDD, verification, graphify → PR #41-#44 (tarjeta compacta 200×60 con huellas SHA-256 de las 96 tarjetas v0.5.0; desborde 320 px: causa real `<code>` sin cortes 338→320 px + rejillas sin minmax + td nowrap; lector de CSS para tests de intención) → CI verde. Tests Go ejecutados como wasm bajo Node, sin `go test` nativo.
- agent-review → commitling #41-#44 → revisión → en curso.
- web-performance-auditor → las 3 webs → auditoría → OK, guardada en evidence/auditoria-rendimiento-v06.md. Accionables: printquote SW descarga doble (−177 KB gz medido); commitling wasm con `pointerdown` y en paralelo con wasm_exec.js (−176 ms Slow-4G); modelduel nada de rendimiento (falta og:image). Descartado precalentar el PDF (620 KB gz por adelantado).
- opencode → curso_ia_MoureDev → revisión de COMO-PROBAR.md → `opencode/nemotron-3-ultra-free` → FALLO: tiempo agotado (exit 124) sin salida. Hipótesis: lectura de carpetas fuera del proyecto pide permiso y se cuelga en modo no interactivo → reintento lanzado desde D:/Desarrollos con `opencode/mimo-v2.6-flash-free`.
- agent-review → commitling #41-#44 → #42, #43 APROBADOS; #41 CAMBIOS NECESARIOS: B1 campos `hop/breathe/rest` del layout muertos → la compacta radiante salta 8 px (puede recortar la cabeza en 60 px) aunque spec/MEMORY dicen 3 px; #44 condicionado. Action retrocompatible verificada (CL_SIZE por env, validación única en Options.Check). Opcionales O1 (action-test con size), O2 (lector CSS).
- ~16:50 · límite de uso de Claude: se cortan agent-project-1, agent-project-2 y agent-review (este ya había entregado). Reanudación 17:11.
- opencode → COMO-PROBAR → reintento desde D:/Desarrollos con `opencode/mimo-v2.6-flash-free` → FALLO: exit 124 sin salida.
- 17:12 · lead → diagnóstico OpenCode → humo «Responde OK» OK; «lee docs/COMO-PROBAR.md» dentro del proyecto OK → causa: leer fuera del directorio de trabajo cuelga `opencode run` no interactivo (permiso de directorio externo) → solución: copiar los archivos a una carpeta de trabajo y lanzarlo allí → relanzado.
- 17:12 · lead → reanudados agent-project-1 y agent-project-2; agent-project-3 recibe B1 + O1 + O2 + mejoras de rendimiento del wasm.
- agent-project-3 → commitling → corrección B1 + O1 + O2 + rendimiento → `8b90112` (Fprintf con l.hop/breathe/rest; test del salto de 3 px y de la cabeza dentro de la tarjeta; comprobación visual a 4x), action-test con size compact/grande, lector CSS robusto, PR #46 (wasm en paralelo + pointerdown + lazy) → CI verde.
- lead → commitling → verificación propia del diff de B1 y de `instantiate()` (res.ok y clone en el fallback) → OK → fusionados #41, #42, #43, #44, #46 → CI/Action/Pages de main en verde → release v0.6.0 → `v1` movida (action.yml retrocompatible: solo se añade `size` con valor por defecto `full`).
- agent-project-1 → printquote → v0.6.0 → spec, TDD, verification, graphify → PR #44, #45, #47 (SW), #48, #49 → CI verde, 454 tests.
- agent-review → printquote #44-#49 → TODOS APROBADOS sin bloqueantes (dinero coherente en texto/PDF/CSV, CSV contra inyección de fórmulas, XSS por nombre de archivo probado, historial corrupto, SW offline en Chrome real). Opcionales: retoques de docs (CHANGELOG dice que og.png muestra el lote y no lo muestra; README «una página A4»), anuncio de «Lote lleno», comentario de tamaño del historial, aria-label de lote.
- lead → printquote → envío de los opcionales a agent-project-1 → BLOQUEADO por el clasificador del modo automático (sin motivo) → no se busca otra vía; queda para Alberto.
- lead → printquote → fusionados #44, #45, #47, #48, #49 → CI y Pages en verde → release v0.6.0.
- agent-project-2 → modelduel → v0.6.0 → spec, security-and-hardening, TDD, graphify → PR #42, #43, #45 (og:image), #46 → CI verde, cobertura 96,33 %. Hallazgo propio: GitHub enlaza @menciones/#refs aunque estén escapadas → U+200B tras @ y #. Capturas del duelo en directo regeneradas.
- agent-review → modelduel #42-#46 → en curso.
- opencode → COMO-PROBAR (carpeta temporal sin git) → FALLO exit 124; prueba mínima en esa carpeta también se cuelga → causa real: `opencode run` se cuelga fuera de un repositorio git → relanzado desde el repo del curso con copias en `.oc-tmp/` (excluida solo en local).
- lead → web publicada → commitling a 320 px: scrollWidth 320 (antes 338), SVG compactos 200, generator.js con pointerdown; printquote a 320 px: scrollWidth 320, bloque del lote presente.
- agent-review → modelduel #42-#46 → #43 y #45 APROBADOS; #42 CAMBIOS: B1 `GH-N` y SHA de commit siguen enlazándose en GitHub (verificado con `gh api markdown`), B2 `write_markdown` trunca informe.md antes de renderizar (0 bytes si falla); #46 docs prometen de más + `_interrupted` escribe siempre index.html → devuelto a agent-project-2 con O2/O3.
- incidencia: el revisor de modelduel borró con globs temporales del scratchpad que no eran suyos (`pdf_project.py`, entre otros). Sin impacto en repos; `pdf_project.py` se puede reconstruir desde la transcripción. Lección para próximos encargos: cada agente usa su propia subcarpeta del scratchpad y no borra con globs.
- opencode → COMO-PROBAR (desde el repo del curso, archivos en `.oc-tmp/` excluida de git) → `opencode/mimo-v2.6-flash-free` → FALLO exit 124 (4.º intento). Conclusión: en esta instalación `opencode run` no interactivo solo es fiable para tareas cortas de un archivo dentro de un repo git; con varios archivos o fuera de git se cuelga sin salida. Se abandona; la actualización de COMO-PROBAR.md la hace el lead al cerrar la fase. `.oc-tmp/` borrada.
