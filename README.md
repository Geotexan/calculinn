# calculinn

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Cálculo de los valores de referencia y recomendación de productos de [Geotexan, S. A](http://www.geotexan.com) en diferentes aplicaciones.

Se puede [usar directamente desde el repositorio](http://geotexan.github.io/calculinn/).

## Desarrollo

`calculinn` es una aplicación _serverless_ puramente HTML+JavaScript que se ejecuta por entero en el navegador del cliente.

Se apoya en código Python interpretado por [Brython](http://brython.info), que es una implementación de un subconjunto de Python en JavaScript.

[Planificación, incidencias y peticiones](https://tree.taiga.io/project/pacoqueen-calculinn/issues) alojadas en Taiga.

## Actualizaciones

### Cambios en orígenes de datos

Si es necesario cambiar algún valor o agregar nuevos productos se debe modificar el fichero _ods_ del directorio `tablas/normalizadas` y volver a generar los ficheros `.html`.
```bash
cd utils
./make.sh
```

Es importante conservar el formato de los nombres de los ficheros, pues determinan el tipo de cálculo (carreteras, vertederos, etc.) y el nombre del fichero `.html` --entre paréntesis-- que generará.

### Cambios en páginas

Si es necesario modificar el aspecto de una página se debe acudir primero al _CSS_. En caso de ser un cambio más profundo (atributo `id`, nuevas etiquetas, etc.) se debe modificar `utils/skel.html` y propagar el cambio con:
```bash
cd utils
./make.sh
```
