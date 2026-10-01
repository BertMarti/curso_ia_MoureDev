# Cómo probar las aplicaciones publicadas

| Aplicación | Qué es | Web | Prueba local |
| --- | --- | --- | --- |
| [printquote](#1-printquote) | Presupuestos de impresión 3D en el navegador. | https://bertmarti.github.io/printquote/ | Node.js / npm |
| [modelduel](#2-modelduel) | Enfrenta modelos de IA con la misma tarea y los mismos tests y genera un informe HTML. | https://bertmarti.github.io/modelduel/ | Python |
| [commitling](#3-commitling) | Mascota pixel-art original para un perfil de GitHub que crece con la actividad. | https://bertmarti.github.io/commitling/ | Go |

## 1. printquote

**Qué es:** una aplicación de presupuestos de impresión 3D que funciona en el navegador.

**Web:** https://bertmarti.github.io/printquote/

### Qué hacer

1. Abre la [pieza de ejemplo](https://bertmarti.github.io/printquote/#ejemplo).
2. Mantén los valores por defecto.
3. Comprueba el total del presupuesto.
4. Prueba abrir un archivo STL, OBJ o 3MF.
5. Selecciona un perfil de impresora.
6. Cambia el selector de idioma entre **ES** y **EN**.
7. Genera el presupuesto en PDF e introduce, si procede, los datos del negocio y el IVA.

### Resultado esperado

- Con la pieza de ejemplo y los valores por defecto, el total es **1,59 €**.
- Se pueden abrir archivos STL, OBJ y 3MF.
- Hay perfiles de impresora disponibles.
- El presupuesto se puede generar en PDF con datos del negocio e IVA.
- La interfaz está disponible en español e inglés mediante el selector ES/EN.

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

**Qué es:** una herramienta que enfrenta modelos de IA con la misma tarea y los mismos tests, y genera un informe HTML.

**Web:** https://bertmarti.github.io/modelduel/

**Demo:** https://bertmarti.github.io/modelduel/demo/

### Qué hacer

1. Abre la web o la demo.
2. Ejecuta la demo local sin claves usando los modelos de repetición `alfa` y `beta`.
3. Abre el informe HTML generado.
4. Para incluir un tercer participante en la liga, añade el modelo `gamma`.

### Resultado esperado

- Los modelos se enfrentan usando la misma tarea y los mismos tests.
- Se genera un informe HTML en la carpeta de salida indicada.
- La demo se puede ejecutar sin claves con los modelos de repetición.

### Probar en local

```bash
git clone https://github.com/BertMarti/modelduel
cd modelduel
python -m venv .venv
# Activa el entorno virtual
pip install -e ".[dev]"
modelduel run examples/tasks --a replay:alfa --b replay:beta --out runs/demo
```

Abre `runs/demo/index.html`.

Para una liga con un modelo adicional:

```bash
modelduel run examples/tasks --a replay:alfa --b replay:beta --model replay:gamma --out runs/demo
```

Para ejecutar los tests:

```bash
pytest
```

## 3. commitling

**Qué es:** una mascota pixel-art original para el perfil de GitHub que crece con la actividad.

**Web:** https://bertmarti.github.io/commitling/

### Qué hacer

1. Abre la web.
2. Revisa la galería.
3. Identifica las dos especies disponibles: **brote de musgo** y **hongo**.
4. Para usarlo en un perfil de GitHub, configura la GitHub Action `BertMarti/commitling@v1` en el repositorio de perfil.

### Resultado esperado

- La galería muestra las especies brote de musgo y hongo.
- La mascota está pensada para crecer con la actividad del perfil de GitHub.
- La integración se realiza mediante la GitHub Action `BertMarti/commitling@v1`.

### Probar en local

```bash
git clone https://github.com/BertMarti/commitling
cd commitling
go test ./...
go run ./cmd/commitling render --fixture testdata/events.json --out out/demo.svg
```

Abre `out/demo.svg`.
