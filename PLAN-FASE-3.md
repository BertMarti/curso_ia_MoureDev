# Plan de la fase 3 (v0.3.0) · equipo multiagente

Estado de partida (30/09/2026): v0.2.0 fusionada y desplegada en los tres proyectos; releases v0.2.0 en printquote y commitling; etiqueta `v1` de commitling creada; release de modelduel pendiente de configurar PyPI.

## Proyectos

| Id | Ruta | Stack | Tamaño (sin tests) | Web |
|---|---|---|---|---|
| P1 printquote | `D:\Desarrollos\printquote` | TypeScript + Vite + three.js + pdf-lib | ~6.200 líneas (stl 1.570, ui 1.100, i18n 730, quote 680, pdf 510, viewer 250) | https://bertmarti.github.io/printquote/ |
| P2 modelduel | `D:\Desarrollos\modelduel` | Python 3.12, solo stdlib | ~3.300 líneas (report 1.150, providers 580) | https://bertmarti.github.io/modelduel/ |
| P3 commitling | `D:\Desarrollos\commitling` | Go 1.27, solo stdlib + Action compuesta | ~3.000 líneas (creature 750, gallery 540, render 520, github 500, og 310) | https://bertmarti.github.io/commitling/ |

Repos relacionados que no son proyectos, pero que el lead integra:
- `BertMarti/BertMarti` (perfil): consume la Action de P3. Tiene el PR #1 abierto.
- `D:\Desarrollos\curso_ia_MoureDev`: reporte, guía y PDF de los tres. Tiene el PR #1 abierto.

## Dependencias entre proyectos

No hay dependencias de código entre P1, P2 y P3. Las que existen son de integración:

1. **P3 → perfil.** El workflow del perfil usa `BertMarti/commitling@main`; ya existe `v1` y debe fijarse a `@v1`. Cualquier cambio en las entradas de `action.yml` de P3 obliga a revisar el perfil. Orden: primero P3 publica, después se actualiza el perfil.
2. **P2 #18 y #19 → publicación en PyPI** (acción de Alberto). Se bloquean hasta que exista https://pypi.org/project/modelduel/.
3. **P1, P2, P3 → curso_ia_MoureDev.** Los PDF se generan leyendo el código de `main` de cada repo; se regeneran al final de la fase.
4. **Convenciones compartidas:** `AGENTS.md` (equipo y flujo), plantilla de PR y patrón de CI y Pages. Un cambio de convención lo decide el lead y se replica en los tres a la vez.

## Equipo

| Agente | Ámbito (exclusivo) | Cometido |
|---|---|---|
| lead (sesión principal) | integración, perfil y curso | Dividir, delegar, revisar, dependencias, PDF y reporte |
| agent-project-1 | solo P1 | Issues de v0.3.0 de printquote |
| agent-project-2 | solo P2 | Issues de v0.3.0 de modelduel |
| agent-project-3 | solo P3 | Issues de v0.3.0 de commitling |
| agent-review | lectura de P1, P2 y P3 | Revisión de cada PR (corrección y sobreingeniería); no escribe código |

Reglas: una rama y un PR por issue contra `main` con `Closes #n`; commits convencionales; `MEMORY.md` en cada PR; Alberto fusiona. Los subagentes se lanzan como `general-purpose` (todas las herramientas, incluidas Skill y MCP), sin listas de herramientas restringidas. Modelo Sonnet por defecto, por el límite semanal.

## Disponibilidad comprobada (30/09/2026, CLI Claude Code 2.1.286)

| Componente | Estado |
|---|---|
| Ponytail | Instalado (`ponytail@ponytail` 4.10.0) y cargado |
| Superpowers | Sincronizado desde claude.ai (`superpowers@synced` 6.4.1), cargado en sesiones nuevas |
| Frontend Design | Sincronizado (`frontend-design@synced`), cargado en sesiones nuevas |
| Ralph Loop | Sincronizado (`ralph-loop@synced` 1.0.0), cargado en sesiones nuevas |
| Context7 | Sincronizado (`context7@synced`); MCP `plugin:context7:context7` conectado |
| Agent Skills | Instalado (`agent-skills@addy-agent-skills` 0.6.11) |
| Graphify | Instalado (`graphifyy` 0.9.72, skill en `~/.claude/skills/graphify`); grafo construido en cada proyecto |

La sesión que ejecuta la fase se abrió antes de la sincronización, así que los agentes usan las skills leyendo su `SKILL.md` y Context7 con `_equipo/c7.py` (ver `D:\Desarrollos\_equipo\HERRAMIENTAS.md`). Ralph Loop no se usa: depende del hook de parada de la sesión principal.

## Uso de herramientas

- **Graphify:** grafo propio por proyecto (`graphify-out/` en cada repo) antes de analizar la arquitectura. No está instalado.
- **Superpowers:** brainstorming y plan por issue, TDD, debugging sistemático y cierre de rama.
- **Context7:** antes de tocar three.js, Vite, pdf-lib (P1), la acción de PyPI y el empaquetado (P2) y la sintaxis de Actions y el Marketplace (P3).
- **Frontend Design:** cambios de interfaz de P1, del informe y la web de P2 y de la galería de P3.
- **Ponytail:** criterio permanente; `ponytail-review` en agent-review.
- **Ralph Loop:** solo en P1 para incrustar una fuente en el PDF (cierre objetivo: test con texto no latino + build en verde). Sin bucles anidados.
- **Agent Skills:** especificación, verificación y envío cuando haya una skill aplicable.

## Trabajo propuesto (hito v0.3.0)

**P1 printquote** (issues por crear):
- Incrustar una fuente en el PDF (acentos de otros idiomas, cirílico, griego) sin disparar el peso inicial.
- Metadatos Open Graph y Twitter también en inglés.
- Aviso al usuario en polígonos OBJ cóncavos de más de 200 vértices.
- Tope de triángulos en 3MF con mensaje claro.
- Zoom con teclado en el visor.
- Captura del README con la interfaz v0.2.

**P2 modelduel** (issues existentes):
- #15 unificar veredicto y clasificación.
- #17 formato es-ES en el aviso de reintento.
- #18 y #19 (bloqueadas hasta la publicación en PyPI).

**P3 commitling** (issues por crear):
- Resistencia ante caídas largas de la API (conservar el último SVG válido en vez de fallar).
- Ejemplos y galería con `@v1` verificados.

**Integración (lead):**
- Perfil con `@v1`.
- PDF v0.2 de los tres.
- Cierre del reporte.

## Orden de ejecución

1. Lead: crear las issues de P1 y P3 en el hito v0.3.0.
2. En paralelo: agent-project-1, agent-project-2 (#15, #17) y agent-project-3; cada uno construye su grafo con Graphify al empezar.
3. agent-review revisa cada PR según se abre; los hallazgos vuelven al agente dueño.
4. Lead: perfil a `@v1` (tras confirmar P3), PDF y reporte.
5. Alberto: fusionar en orden y publicar las releases v0.3.0; publicar P2 en PyPI y desbloquear #18 y #19.
