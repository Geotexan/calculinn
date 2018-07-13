Instrucciones para generar los ficheros `html`
==============================================

En el directorio `utils` reside un _script_ `make.sh` que genera todos los 
ficheros `.html` con el código python que ejecutará _Brython_ adaptado a cada 
una de las tablas de referencia.

* `motor.py` contiene el código que realiza el cálculo efectivo en función de
  las entradas. Es común para todos los `html`.
* `pythonize_tablacalc.py` toma como entrada el fichero `ods` o `csv` con las
  tablas de cálculo originales y genera un fichero _python_ equivalente.
* `build_html.py` construye el `.html` final basándose en la tabla de cálculo,
  la tabla de recomendación de producto y la aplicación. También genera las 
  tablas "pythonizadas" llamando a `pythonize_tablacalc.py`.
* `skel.html` es el fichero base para construir el resto de ficheros HTML. 
  **Todos los cambios deben hacerse aquí** y ejecutar el `make.sh` para 
  actualizar los ficheros del directorio `calculos`.


# Estructura del proyecto

* `autorun.inf` debería hacer que se autoejecutara `index.html` en el navegador
   del usuario al conectar un _pendrive_ que contiene todos los ficheros de la
   aplicación.
* `autorun` sirve a algunos escritorios GNU/Linux a autoarrancar el USB.
* `calculo` contiene los submenús de la parte de cálculo.
* `calculos` contiene las páginas específicas de cada cálculo (balsas, 
  carreteras...). Se generan automáticamente a partir de una plantilla.
* `conds` contiene los pliegos de condiciones asociados a cada cálculo. Reciben
  los valores a mostrar a través de parámetros _GET_ de la _url_.
* `COPYING.txt`: Fichero de licencia GPLv3.
* `css` contiene todos los ficheros de estilos de todas las páginas.
* `doc`: Documentación adicional.
* `favicon.ico`: Icono para mostrar en el navegador.
* `fonts`: Tipografías usadas.
* `geosinteticos`: Ficheros _html_ del submenú de geosintéticos.
* `geotextiles` contiene los ficheros del submenú de geotextiles. Se divide a
  su vez en dos submenús más: `tejidos` y `no-tejidos`. Cada uno de ellos es
  un subdirectorio con las páginas de cada apartado.
* `images`: Todas las imágenes usadas en el proyecto. Contiene un subdirectorio
  `calculos` con los diagramas usados en los cálculos y sus páginas de
  justificaciones.
* `index.html` es el "menú principal".
* `introduccion` contiene las páginas del apartado Introducción.
* `js`: Ficheros JavaScript:
    * `fichas_tecnicas.js`: Código para abrir el _pdf_ de la ficha técnica de
      cada uno de los productos.
    * `help.js`: Busca el diagrama (fichero _png_) de ayuda correspondiente al 
      cálculo actual y lo muestra en una ventana emergente.
    * `justificacion.js`: Código que extrae los valores calculados y los pasa
      por `GET` al `.html` de justificación del cálculo.
    * `pliego_condiciones.js`: Funciona igual que `justificacion.js`, pero solo
      envía los valores calculados. No se necesitan valores de referencia, 
      entradas ni producto recomendado. En lugar de abrir el _html_ de 
      justificación, abre el de pliego de condiciones de cada cálculo.
    * `replace_params.js`: Usado en las justificaciones y pliego de condiciones.
      Inserta en las etiquetas `span` cuyo `id` sea igual a los valores de los 
      parámetros de entrada (`in*`), referencia (`ref_*`) o calculados (`gtx_*`)
      el valor recibido por `GET` en la `url` de los parámetros que se llamen 
      igual.
* `just` contiene los _html_ de justificación de cada tipo de cálculo.
* `libs`: Bibliotecas de terceros: **Brython** y **jQuery**.
* `pdf`: Fichas técnicas de cada producto.
* `plantillas`: Diseños de referencia.
* `prototype`: Pruebas de concepto y prototipos.
* `README.md`: Fichero de introducción y resumen del proyecto.
* `utils` contiene un par de programas de ayuda para el desarrollo:
    * `build_html.py` se encarga de leer los datos de la tabla de cálculo y de
      la tabla de recomendación (_ods_ o _csv_) y reemplaza en la plantilla 
      `skel.html` las etiquetas clave (título, "motor de inferencia", etc.) por 
      los valores o el código definitivo.
    * `make.sh`: _Script_ para generar automáticamente todos los _html_ en su
      lugar correspondiente.
    * `motor.py`: Es el código que realmente realiza los cálculos y determina
      el producto recomendado en función de las entradas apoyándose en las 
      tablas de cálculo procedentes de las hojas de cálculo _ods_ o _csv_.
    * `pythonize_tablacalc.py` recibe una hoja de cálculo con las "reglas" que
      determinan producto recomendado y valores calculados en función de las
      entradas y genera el código python equivalente que alimentará a 
      `motor.py`.
    * `skel.html`: Fichero base para todos los _html_ de cálculo. Si es
      necesario cambiar algo, **debe hacerse aquí** y propagarse al resto de
      ficheros volviéndolos a generar con `make.sh`.

