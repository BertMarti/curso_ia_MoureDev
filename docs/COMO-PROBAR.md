# Cómo probar las aplicaciones publicadas

Actualizado para la **v0.6.0** de las tres aplicaciones (1 de octubre de 2026).

| Aplicación | Qué es | Web | Prueba local |
| --- | --- | --- | --- |
| [printquote](#1-printquote) | Presupuestos de impresión 3D en el navegador. | https://bertmarti.github.io/printquote/ | Node.js / npm |
| [modelduel](#2-modelduel) | Enfrenta modelos de IA con la misma tarea y los mismos tests y genera un informe HTML o Markdown. | https://bertmarti.github.io/modelduel/ | Python |
| [commitling](#3-commitling) | Mascota pixel-art original para un perfil de GitHub que crece con la actividad. | https://bertmarti.github.io/commitling/ | Go |

## 1. printquote

**Qué es:** una aplicación de presupuestos de impresión 3D que funciona en el navegador.

**Web:** https://bertmarti.github.io/printquote/

### Qué hacer

1. Pulsa **«Ver demo»** en la cabecera: carga la pieza de ejemplo, gira la cámara y cambia material y relleno mientras el total se recalcula. Se para con un segundo clic, Esc o cualquier interacción, y al terminar devuelve tus ajustes.
2. Abre la [pieza de ejemplo](https://bertmarti.github.io/printquote/#ejemplo) y mantén los valores por defecto.
3. Comprueba el total del presupuesto.
4. Prueba abrir un archivo STL, OBJ o 3MF y selecciona un perfil de impresora.
5. Cambia el selector de idioma entre **ES** y **EN**.
6. Genera el presupuesto en PDF e introduce, si procede, los datos del negocio y el IVA.
7. **Lote (v0.6):** en el bloque **06 Lote**, pulsa «Añadir esta pieza», cambia material o copias y vuelve a añadirla. Prueba «Quitar», «Copiar lote» y «PDF del lote».
8. En el bloque **08 Historial**, pulsa «Guardar lote» y después «Exportar CSV».

### Resultado esperado

- Con la pieza de ejemplo y los valores por defecto, el total es **1,59 €**.
- La demo termina sola en unos 13 segundos y no guarda nada.
- El lote suma cada pieza con los ajustes con los que se añadió, aplica el IVA una sola vez y admite hasta 50 piezas.
- El total del lote coincide en el panel, el texto copiado, el PDF y el CSV.
- El PDF del lote puede ocupar varias páginas, numeradas «Página n de N».
- «Copiar enlace» comparte solo los parámetros de la pieza, no el lote.

### Probar en local

```bash
git clone https://github.com/BertMarti/printquote
cd printquote
npm ci
npm run dev
```

Abre http://localhost:5173/printquote/.

Para ejecutar los tests:

```bash
npm test
```

## 2. modelduel

**Qué es:** una herramienta que enfrenta modelos de IA con la misma tarea y los mismos tests, y genera un informe HTML o Markdown.

**Web:** https://bertmarti.github.io/modelduel/ · **Duelo en directo:** https://bertmarti.github.io/modelduel/#demo · **Informe de demostración:** https://bertmarti.github.io/modelduel/demo/ · **Clasificación:** https://bertmarti.github.io/modelduel/leaderboard/

### Qué hacer

1. En la web, pulsa **«Ver un duelo en directo»**: reproduce un duelo grabado, sin claves, con el reloj y los tests avanzando.
2. Abre el informe de demostración y la clasificación pública.
3. En local, ejecuta la demo sin claves con los modelos de repetición `alfa`, `beta` y `gamma`.
4. **Informe en Markdown (v0.6):** genera `informe.md` y pégalo en un issue o un PR de GitHub.

### Resultado esperado

- El duelo en directo marca al primero con «▲ primero» y avisa de que el informe completo agrega todas las tareas.
- Se genera un informe HTML en la carpeta de salida.
- Con `--format md` se genera `informe.md` con el marcador, el veredicto, una tabla por tarea y el coste.
- Al pegar `informe.md` en GitHub, los textos de los resultados no generan enlaces, menciones ni referencias a issues o commits.

### Probar en local

```bash
git clone https://github.com/BertMarti/modelduel
cd modelduel
python -m venv .venv
# Activa el entorno virtual
pip install -e ".[dev]"
modelduel run examples/tasks --model replay:alfa --model replay:beta --model replay:gamma --format html,md --out runs/demo
```

Abre `runs/demo/index.html` y `runs/demo/informe.md`.

Para generar el Markdown de un resultado que ya tienes:

```bash
modelduel report runs/demo/results.json --format md --out runs/demo
```

Para ejecutar los tests:

```bash
pytest
```

## 3. commitling

**Qué es:** una mascota pixel-art original para el perfil de GitHub que crece con la actividad.

**Web:** https://bertmarti.github.io/commitling/

### Qué hacer

1. Abre la web y pulsa **«Ver demo: míralo crecer»**: es un timelapse de unos 15 segundos sin pedir nada a GitHub, con Pausa, Detener y un control deslizante.
2. Revisa la galería e identifica las dos especies: **brote de musgo** y **hongo**.
3. **Tarjeta compacta (v0.6):** baja a la sección «Tarjeta compacta» y, en el generador, elige «Tamaño: Compacta».
4. Escribe un usuario de GitHub en el generador y copia el workflow relleno.
5. En el móvil (o a 320 px de ancho), comprueba que la página no se desplaza hacia los lados.
6. Para usarlo en un perfil, configura la GitHub Action `BertMarti/commitling@v1` en el repositorio de perfil, con `size: compact` si quieres la insignia pequeña.

### Resultado esperado

- La demo recorre las cinco fases y los cuatro ánimos.
- La compacta es una insignia de 200x60 con la criatura, la fase, el ánimo y una barra de progreso.
- Sin `size` (o con `size: full`), la tarjeta es exactamente la de siempre: las configuraciones existentes no cambian.
- El generador solo descarga el WebAssembly al tocar el formulario o pulsar «Ver demo».

### Probar en local

```bash
git clone https://github.com/BertMarti/commitling
cd commitling
go test ./...
go run ./cmd/commitling render --fixture testdata/events.json --size compact --out out/demo.svg
```

Abre `out/demo.svg`.

> En el PC de Alberto, el Control de aplicaciones de Windows bloquea los binarios de test de Go sin firmar. Ahí, compila con `go build ./...` y deja los tests al CI de GitHub.
