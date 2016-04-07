#!/bin/bash
set -eu
set -o pipefail
IFS=$'\n\t'
# http://redsymbol.net/articles/unofficial-bash-strict-mode/

## "Compila" todas las tablas de cálculo para generar en el directorio
## actual todas las páginas html y módulos correspondientes.
## LICENSE: [Do What the Fuck You Want to Public License](http://www.wtfpl.net)

RUTA_DEFAULT='/home/queen/Geotexan/doc/Programación/calculinn: Programa cálculo pendrive/tablas/normalizadas'
OPEN=false
RUTA_BASE=$(dirname $0)
RUTA_DEST="$RUTA_BASE/../calculos"

clean () {
    rm $RUTA_DEST/[^s][^k][^e][^l]*.html &>/dev/null || true
    # Caso especial. Drenaje me entra en el glob de arriba:
    rm $RUTA_DEST/drenaje.html $RUTA_DEST/drenaje_normativa.html &>/dev/null || true
    rm $RUTA_DEST/*_calculo.py &>/dev/null || true
    rm $RUTA_DEST/*_recomendador.py &>/dev/null || true
}

abrir_ficheros_en_navegador () {
    # Ojo porque abrirá todos los *.html del directorioque no sean el skel.
    for HTML in $RUTA_DEST/*.html; do
        if [ "$(basename $HTML)" == "skel.html" ]; then
            :
        else
            echo "Abriendo $HTML..."
            xdg-open "$HTML"
        fi
    done
}

print_usage () {
    echo "$0 [clean|open|path]"
    echo "path : Ruta donde buscará todos los pares de ficheros fuente ODS o "
    echo "       CSV para generar los ficheros .html y .py correspondientes en"
    echo "       el directorio $RUTA_DEST"
    echo
    echo "clean: Limpia todos los ficheros .html y .py generados."
    echo
    echo "open : Genera todos los ficheros correspondientes a cada par de "
    echo "       tablas fuente del directorio por defecto:"
    echo "       $RUTA_DEFAULT"
    echo
    echo -n "Si no se especifca parámetro, genera todos los .html y .py de la "
    echo "ruta por defecto."
}

if [ $# -eq 0 ]; then
    RUTA_TABLAS=$RUTA_DEFAULT
else
    if [ "$1" == "-h" ] || [ "$1" == "--help" ]; then
        print_usage
        exit
    elif [ "$1" == "clean" ]; then
        clean
        exit $?
    elif [ "$1" == "open" ]; then
        RUTA_TABLAS=$RUTA_DEFAULT
        OPEN=true
    else
        RUTA_TABLAS=$1
    fi
fi

# Solo necesito uno de cada par de tablas. La de cálculo, por ejemplo.
for FICH_CALCULO in $RUTA_TABLAS/??0*; do
    $RUTA_BASE/build_html.py -d $RUTA_DEST "$FICH_CALCULO"
done

if [ "$OPEN" = true ]; then
    abrir_ficheros_en_navegador
fi
