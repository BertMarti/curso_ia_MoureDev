# Herramientas del equipo (léelo al empezar)

Esta sesión se abrió antes de sincronizar los plugins, así que sus skills no aparecen en la herramienta `Skill`. Están instaladas en disco: **úsalas leyendo su `SKILL.md` y siguiéndolo** (es exactamente lo que hace la herramienta `Skill`). Lee solo las que apliquen a tu tarea.

Rutas base (Git Bash):
- `SP=~/.claude/plugins/synced/*/6ba53849-2ee0-4cf0-957e-31c122ea1dd1/skills` (Superpowers)
- `FD=~/.claude/plugins/synced/*/2ca4e30e-2482-4c94-8644-6c26adf27391/skills/frontend-design/SKILL.md` (Frontend Design)
- `AS=~/.claude/plugins/cache/addy-agent-skills/agent-skills/0.6.11/skills` (Agent Skills)
- `PT=~/.claude/plugins/cache/ponytail/ponytail/4.10.0/skills` (Ponytail)
- `GF=~/.claude/skills/graphify/SKILL.md` (Graphify)

## Cuándo usar cada una

| Situación | Skill (`<ruta>/<nombre>/SKILL.md`) |
|---|---|
| Antes de diseñar una funcionalidad | `$SP/brainstorming`, luego `$SP/writing-plans` |
| Implementar | `$SP/test-driven-development` (test que falla → código → verde) |
| Un fallo que no entiendes | `$SP/systematic-debugging` |
| Antes de decir «terminado» | `$SP/verification-before-completion` |
| Cerrar la rama y abrir el PR | `$SP/finishing-a-development-branch` |
| Revisar código (agent-review) | `$SP/requesting-code-review`, `$AS/code-review-and-quality/SKILL.md`, `$PT/ponytail-review/SKILL.md` |
| Recibir revisión | `$SP/receiving-code-review` |
| Interfaz, estilos, UX, responsive | `$FD` y `$AS/frontend-ui-engineering/SKILL.md` |
| CI/CD y publicación | `$AS/ci-cd-and-automation/SKILL.md`, `$AS/shipping-and-launch/SKILL.md` |
| Seguridad | `$AS/security-and-hardening/SKILL.md` |
| Simplicidad (siempre) | `$PT/ponytail/SKILL.md` |

## Graphify (primera opción para entender el repo)

Cada proyecto tiene su grafo en `graphify-out/` (ya construido). CLI: `G=/c/Users/Alberto-PC/AppData/Roaming/Python/Python312/Scripts/graphify.exe`.
- Lee primero `graphify-out/GRAPH_REPORT.md` (comunidades, nodos centrales).
- `"$G" explain "<símbolo>"` y `"$G" path "<A>" "<B>"` para relaciones e impacto.
- Tras cambios estructurales: `"$G" update .`
- `graphify-out/` no se sube al repositorio: añádelo al `.gitignore` en tu primer PR si no está.

## Context7 (documentación actual de librerías)

Antes de decidir según el comportamiento de una librería, framework, API o herramienta:
```bash
MSYS_NO_PATHCONV=1 python /d/Desarrollos/_equipo/c7.py resolve "<librería>" "<qué necesitas>"
MSYS_NO_PATHCONV=1 python /d/Desarrollos/_equipo/c7.py docs "</org/proyecto>" "<pregunta concreta>"
```
(`MSYS_NO_PATHCONV=1` es obligatorio en Git Bash para que no convierta `/org/proyecto` en una ruta.)

## Ralph Loop

No se usa en esta fase: funciona con un hook de parada de la sesión principal y no debe anidarse en subagentes. El ciclo implementar → ejecutar → comprobar → corregir lo hace cada agente con TDD.

## Reglas comunes

- Trabajas **solo** en tu proyecto. Si algo afecta a otro, dilo en tu informe final: el lead lo coordina.
- Una rama y un PR por issue contra `main`, `Closes #n`, commits convencionales en español con `Agente: <rol> (Claude Code · Sonnet)` y `Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>`.
- `MEMORY.md` actualizado en cada PR. Nunca fusiones, ni borres ramas remotas, ni crees etiquetas o releases.
- Empuja tras cada commit en verde (hay límites de uso: que nada se pierda si hay un corte).
- Cierra los procesos que arranques (servidores de desarrollo, `http.server`) antes de terminar.

## Go en este PC (importante)

El Control de aplicaciones de Windows (Smart App Control) bloquea y notifica cada binario de test de Go sin firmar (`*.test.exe`). **No ejecutes `go test` ni `go run` en local.** Verifica en local solo con `gofmt -l .`, `go vet ./...` y `go build ./...` (compilar no dispara el aviso), y deja la ejecución de tests al CI de GitHub (`gh pr checks --watch`, `gh run view --log-failed`). Los tests del wasm pueden ejecutarse con `node`.
