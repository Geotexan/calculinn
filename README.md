![Geotexan, SA](https://geotexan.com/wp-content/uploads/2015/05/geotexan-logo-verde2.png)

# calculinn

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Cálculo de los valores de referencia y recomendación de productos de [Geotexan, S. A.](http://www.geotexan.com) en diferentes aplicaciones.

Se puede [usar directamente desde el repositorio](http://geotexan.github.io/calculinn/).

## Desarrollo

`calculinn` es una aplicación _serverless_ puramente HTML+JavaScript que se ejecuta por entero en el navegador del cliente.

Se apoya en código Python interpretado por [Brython](http://brython.info), que es una implementación de un subconjunto de Python en JavaScript.

Compatible con Safari, Chrome, Firefox, Internet Explorer/Edge e incluso Silk (Kindle) siempre que tengan activado JavaScript. Se ha evitado cualquier práctica que pudiera ser bloqueada por las reglas de seguridad de los diferentes navegadores y sistemas operativos (importar código desde un fichero local en Chrome, por ejemplo).

[Planificación, incidencias y peticiones](https://tree.taiga.io/project/pacoqueen-calculinn/issues) alojadas en Taiga.

### Actualizaciones

#### Cambios en orígenes de datos

Si es necesario cambiar algún valor o agregar nuevos productos se debe modificar el fichero _ods_ del directorio `tablas/normalizadas` (no inlcuido en el repositorio) y volver a generar los ficheros `.html`.
```bash
cd utils
./make.sh
```
> La ruta al directorio de tablas por defecto del _script_ `make.sh` debe apuntar al directorio local donde residan las hojas de cálculo o bien ejecutar `make.sh ruta_ficheros_ods`

Es importante conservar el formato de los nombres de los ficheros, pues determinan el tipo de cálculo (carreteras, vertederos, etc.) y el nombre del fichero `.html` --entre paréntesis-- que generará. Por ejemplo: `310 drenaje_Geotexan_cálculo (drenaje-por-Geotexan.html).ods`.

#### Cambios en páginas

Si es necesario modificar el aspecto de una página se debe acudir primero al _CSS_. En caso de ser un cambio más profundo (atributo `id`, nuevas etiquetas, etc.) se debe modificar `utils/skel.html` y propagar el cambio con:
```bash
cd utils
./make.sh
```
> :warning: Se necesitan las tablas originales para poder regenerar los _html_.

