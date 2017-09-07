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

