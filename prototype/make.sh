#!/bin/bash
set -eu
set -o pipefail
IFS=$'\n\t'
# http://redsymbol.net/articles/unofficial-bash-strict-mode/

## "Compila" todas las tablas de cálculo para generar en el directorio
## actual todas las páginas html y módulos correspondientes.
## LICENSE: [Do What the Fuck You Want to Public License](http://www.wtfpl.net)

clean () {
    rm [^s][^k][^e][^l]*.html
    rm *_calculo.py
    rm *_recomendador.py
}

if [ $# -eq 0 ]; then
    RUTA_TABLAS='/home/queen/Geotexan/doc/Programación/calculinn: Programa cálculo pendrive/tablas/normalizadas'
else
    if [ "$1" == "clean" ]; then
        clean
        exit $?
    else
        RUTA_TABLAS=$1
    fi
fi

# Solo necesito uno de cada par de tablas. La de cálculo, por ejemplo.
for FICH_CALCULO in $RUTA_TABLAS/??0*; do
    echo ./build_html.py "$FICH_CALCULO"
done
