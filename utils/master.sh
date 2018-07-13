#!/bin/bash
set -eu
set -o pipefail
IFS=$'\n\t'

## Crea una imagen VFAT con el contenido del pendrive para ser grabada en 
## varios dispositivos a la vez con MultiWriter o Etcher.
## LICENSE: [GLWT(Good Luck With That)](https://github.com/me-shaon/GLWTPL/blob/master/LICENSE)

RUTA_BASE=$(dirname $0)/..
RUTA_DEST="$RUTA_BASE/master"
MNT_IMG=/tmp/mntgtx

clean () {
    rm -rf  ${RUTA_DEST}/* &>/dev/null || true
}

print_usage () {
    echo "$0 [clean] [path]"
    echo "path : Ruta donde creará la imagen del pendrive."
    echo
    echo "clean: Limpia todos los ficheros."
    echo
    echo -n "Si no se especifca parámetro, genera la estructura en la " 
    echo "ruta por defecto `./master`."
}

if [ $# -gt 0 ]; then
    if [ "$1" == "-h" ] || [ "$1" == "--help" ]; then
        print_usage
        exit
    elif [ "$1" == "clean" ]; then
        if [ $# -eq 2 ]; then
            RUTA_DEST=$2
        fi
        clean
        exit $?
    else
        RUTA_DEST=$1
    fi
fi

# Ficheros a incluir en el máster:
declare -a FILES=("autorun.inf" "calculo" "calculos" "conds" "COPYING.txt" "css" "favicon.ico" \
    "fonts" "geosinteticos" "geotextiles" "images" "index.html" "introduccion" "js" "just" \
    "libs" "pdf" "autorun")

# No se pueden ocultar hasta no estar en el pendrive formateado como FAT/NTFS
declare -a HIDDEN=("calculo" "calculos" "conds" "css" "fonts" "geosinteticos" "geotextiles" \
    "images" "introduccion" "js" "just" "libs" "pdf" "autorun")

# Creo directorio destino si no existe
mkdir -p $RUTA_DEST

# Creo la imagen
if [[ -f $RUTA_DEST/geotexan.img ]]; then 
    rm $RUTA_DEST/geotexan.img
fi
dd if=/dev/zero of=$RUTA_DEST/geotexan.img bs=512 count=1958400

# Creo el sistema de ficheros
echo "Vamos a crear el sistema de ficheros. Ejecutando sudo..."
sudo mkfs -t fat -F 16 -n GEOTEXAN $RUTA_DEST/geotexan.img

# Monto la imagen
echo "Vamos a montar la imagen. Ejecutando sudo..."
mkdir -p $MNT_IMG && sudo mount -o loop,rw,sync $RUTA_DEST/geotexan.img $MNT_IMG
echo "Permisos de escritura. Ejecutando sudo..."
sudo chmod -R 777 $MNT_IMG

# Copio los ficheros
for FILE in "${FILES[@]}"; do
    echo "Copiando ${FILE} a ${MNT_IMG}/${FILE}..."
    sudo cp -R "$RUTA_BASE/$FILE" "$MNT_IMG"
    sudo fatattr +r "$MNT_IMG/$FILE"
done

# Copio las instrucciones al raíz
sudo cp "$RUTA_BASE/doc/instrucciones.pdf" "$MNT_IMG/INSTRUCCIONES.pdf"
sudo fatattr +r "$MNT_IMG/INSTRUCCIONES.pdf"

# Permisos y tal
sudo chmod a+x $MNT_IMG/autorun.inf
sudo chmod a+x $MNT_IMG/autorun
for FILE in  "${HIDDEN[@]}"; do
    echo "Estableciendo permisos de ${MNT_IMG}/${FILE}..."
    sudo fatattr +h "$MNT_IMG/$FILE"
done

# Desmonto la imagen
echo "Vamos a desmontar la imagen. Ejecutando sudo..."
sudo umount $MNT_IMG

echo -e "\033[0;32m >>> Finalizado <<< \033[0m"
