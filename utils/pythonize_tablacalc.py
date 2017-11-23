#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Script para generar un fichero python equivalente al ODS o CSV de modo que
para usar los datos solo hay que importarlo en lugar de parsear el fichero
fuente, que da problemas a causa del "same origin policy" de JavaScript.
"""


from __future__ import print_function
import sys
import csv
import argparse
from collections import defaultdict
from odf.table import TableRow, TableCell, Table
from odf.text import P
from odf.opendocument import load


def es_cabecera(lista):
    """
    Devuelve por heurística si es una lista correspondiente a la cabecera de
    la hoja de cálculo (True).
    """
    # Podría hacerse simplemente mirando si es la fila 0 o la 1, pero no me
    # fío de que no cambien las tablas y soy así de rebuscado.
    # NOTE: Si alguna cabecera de columna tiene un número entre el texto,
    # **no** se considerará cabecera.
    es_fila_numerica = False  # es_fila_numerica es True si hay algún valor numérico, = NO cabecera.
    for valor in lista:
        hay_al_menos_un_valor_numerico = False
        for caracter in valor:
            if caracter.isdigit():
                hay_al_menos_un_valor_numerico = (
                    hay_al_menos_un_valor_numerico or True)
        es_fila_numerica = es_fila_numerica or hay_al_menos_un_valor_numerico
        if es_fila_numerica:     # OPTIMIZACIÓN: Si he encontrado uno, me salgo.
            break
    if not lista:   # Si es una fila vacía, no quiero que se considere cabecera.
        es_fila_numerica = True
    return not es_fila_numerica


def parse(fin):
    """
    Con el fichero «fin» **ya abierto** crea un "reader" de csv y lee todos
    los valores. Devuelve una lista con los campos cabecera y otra lista
    de listas con los valores de referencia de cálculo (filas de celdas).
    """
    res = []
    cabecera = ()
    cabecera_superior = ()
    reader = csv.reader(fin)
    for fila in reader:
        if es_cabecera(fila):
            # La segunda cabecera, la de verdad, machacará a la de (In, Out).
            cabecera = fila
            if "In" in cabecera or "Out" in cabecera:
                # Ojo, es la fila que me dice cuántas entradas y salidas
                # tiene la tabla de cálculo.
                numentradas, numsalidas = find_ins_outs(cabecera)
                cabecera_superior = cabecera
            continue
        if fila:    # Si la fila está vacía, paso de ella.
            res.append(tuple(fila))
    return cabecera, res, numentradas, numsalidas, cabecera_superior


def find_ins_outs(fila):
    """
    Devuelve el número de entradas y salidas que indica la primera cabecera.
    """
    ins = outs = 0
    # Todo hasta encontrar Out son entradas.
    ins = fila.index("Out")
    # A partir de ahí son salidas.
    outs = len(fila[ins:])
    if "FICHA" in fila[-1].upper():
        # **Salvo** en las tablas de cálculo, que tengo anotados los productos
        # pero solo como referencia. No son salidas.
        outs -= 1
    return ins, outs


def es_fichero_recomendador(cabecera):
    """
    Devuelve True si es un fichero recomendador y no uno de cálculo.
    La diferencia está en que el de cálculo lleva **siempre** una última
    columna que dice «Ficha técnica».
    """
    # Es una chapuza, lo sé. Pero hay que habilitar Chrome urgentemente.
    if cabecera[-1].lower().strip() == u"ficha técnica":
        res = False
    else:
        res = True
    return res


# pylint: disable=too-many-arguments
def generate(nombre_fout, cabecera, datos, numentradas, numsalidas, rangos,
             cabecera_superior):
    """
    Crea un fichero python muy sencillo (si existe, lo sobreescribe) que
    instancia la cabecera y filas de datos al ser importado.
    cabecera_superior es la fila que contiene el In, Out y Ficha técnica si
    es un fichero de cálculo y no recomendador.
    """
    skel = ["#!/usr/bin/env python\n"]
    skel.append("# -*- coding: utf-8 -*-\n\n")
    skel.append("NUMENTRADAS = {}\n".format(numentradas))
    skel.append("NUMSALIDAS = {}\n".format(numsalidas))
    skel.append("CABECERA = {}\n".format(cabecera))
    if es_fichero_recomendador(cabecera_superior):
        skel.append("TABLA = {}\n".format(datos))
    else:   # Es fichero de cálculo. Evito conflictos de nombre.
        skel.append("CALCULO = {}\n".format(datos))
    skel.append("RANGOS = {}".format(rangos))
    fout = open(nombre_fout, "w")
    fout.writelines(skel)
    fout.close()


def esta_en(cad, lista):
    """
    Devuelve True si la cadena «cad» está en alguna de las cadenas de «lista».
    """
    res = False
    for item in lista:
        if cad in item:
            # NOTE: Caso especial. "Inclinación de muro" no debe activar la
            # detección de "In" en la cabecera.
            if "Inclinaci" in item:
                continue
            res = True
            break
    return res


def parse_opendocument(fin):
    """
    Con el fichero «fin» **ya abierto** lee todos los valores de las filas.
    Devuelve una lista con los campos cabecera y otra lista
    de listas con los valores de referencia de cálculo (filas de celdas).
    """
    res = []
    cabecera = ()
    cabecera_superior = ()
    doc = load(fin)
    tables = doc.spreadsheet.getElementsByType(Table)
    table = tables[0]   # Sólo tienen 1 hoja
    rows = table.getElementsByType(TableRow)
    numentradas = numsalidas = 0    # Por si no tuviera filas
    for row in rows:
        fila = convert_odrow(row)
        if es_cabecera(fila):
            # La segunda cabecera, la de verdad, machacará a la de (In, Out)
            # en la segunda iteración. La primera nos dará el # de ins y outs.
            cabecera = fila
            if esta_en("In", cabecera) or esta_en("Out", cabecera):  # Ojo, es
                # la fila que me dice cuántas entradas y salidas tiene la
                # tabla de cálculo.
                numentradas, numsalidas = find_ins_outs(cabecera)
                cabecera_superior = cabecera
            continue
        if fila:    # Si la fila está vacía, paso de ella.
            res.append(fila)
    return cabecera, res, numentradas, numsalidas, cabecera_superior


def get_numcolumns(cell):
    """
    Devuelve el número de columnas del ODS que ocupa la celda.
    Una celda puede estar unida con otras, ocupando varias columnas.
    """
    res = 1
    for attribute in cell.attributes:
        # pylint: disable=unused-variable
        namespace, name = attribute
        if "columns-spanned" in name:
            res = int(cell.attributes[attribute])
    return res


def convert_odrow(row):
    """
    Convierte una fila TableRow de OpenDocument en una lista de valores
    de sus celdas.
    """
    res = []
    for cell in row.getElementsByType(TableCell):
        columnas_unidas = get_numcolumns(cell)
        textos = cell.getElementsByType(P)
        for texto in textos:
            for nodo in texto.childNodes:
                try:
                    valor = nodo.data
                except AttributeError:  # Nodo comentario, no contiene datos.
                    pass
                else:
                    res.append(valor)
        # Si lleva columnas unidas, agrego valores vacíos para saberlo.
        # pylint: disable=unused-variable
        for i in range(1, columnas_unidas):
            res.append("")
    ret = tuple(res)
    return ret


def sanitize(nombre):
    """
    Devuelve el nombre recibido pero sin espacios ni tildes que impidan
    su uso como módulo Python.
    """
    simbolos = ((" ", "_"), ("(", "_"), (")", "_"),
                ("á", "a"), ("é", "e"), ("í", "i"),
                ("ó", "o"), ("ú", "u"), ("-", "_"),
                ("#", "_"), (".htm", "_htm"))
    res = nombre
    for wrong, good in simbolos:
        res = res.replace(wrong, good)
    return res


def main():
    """
    Abre el fichero CSV de entrada y genera un fichero python que carga
    automáticamente al ser importado como módulo la cabecera y las filas
    de cálculo.
    """
    parser = argparse.ArgumentParser(description="Conversor de ODS a py.")
    parser.add_argument("fichero_entrada", help="Fichero de entrada")
    parser.add_argument("-o", help="Fichero de salida", dest="nombre_fout")
    args = parser.parse_args()
    nombre_fin = args.fichero_entrada
    nombre_fout = args.nombre_fout
    if not nombre_fout:
        # Me da igual si era un csv o un ods:
        nombre_fout = nombre_fin.replace(".csv", ".py")
        nombre_fout = nombre_fout.replace(".ods", ".py")
    nombre_fout = sanitize(nombre_fout)
    try:
        if nombre_fin.endswith(".csv"):
            fin = open(nombre_fin)
        else:
            fin = open(nombre_fin, "rb")  # En binario o peta el odfpy
    except IOError:
        print("El fichero {} no existe.".format(nombre_fin), file=sys.stderr)
        sys.exit(1)
    if nombre_fin.endswith(".csv"):
        (cabecera, datos, numentradas, numsalidas,
         cabecera_superior) = parse(fin)
    else:   # Es un OpenDocument (.ods).
        (cabecera, datos, numentradas, numsalidas,
         cabecera_superior) = parse_opendocument(fin)
    rangos = determinar_rangos(cabecera[:numentradas], datos)
    generate(nombre_fout, cabecera, datos, numentradas, numsalidas, rangos,
             cabecera_superior)
    fin.close()
    sys.exit(0)


def determinar_rangos(columnas, tabla):
    """
    Crea y devuelve un diccionario cuyas claves son los nombres de las
    columnas de entrada recibidas.
    Los valores son:
        - Si es una columna numérica, el menor y el mayor valor admitido.
          Pueden ser el mismo. Como tupla de 2 elementos. Salvo si son valores
          únicos, que entonces también sería un desplegable y no un rango.
        - Si es una columna de texto, una tupla con los diferentes valores que
          puede tomar. En el HTML se convertirá en un desplegable.
    """
    minimos = defaultdict(lambda: None)
    maximos = defaultdict(lambda: None)
    cadenas = defaultdict(lambda: None)
    res = {}
    for fila in tabla:
        for indice, columna in enumerate(columnas):
            valor = fila[indice]
            if es_numero(valor):    # Entero o flotante, pero uno solo.
                # numero = parse_numero(valor)
                # update_minimos(minimos, columna, numero)
                # update_maximos(maximos, columna, numero)
                update_cadenas(cadenas, columna, valor)
            elif es_rango_numerico(valor):
                ini, fin = parse_rango(valor)
                update_minimos(minimos, columna, ini)
                update_maximos(maximos, columna, fin)
            elif valor.upper().strip() == "Z":
                # Alta impedancia. Esta variable no importa para ese caso.
                pass
            else:   # Es texto
                update_cadenas(cadenas, columna, valor)
    for columna in columnas:
        if minimos[columna] is not None:
            res[columna] = (minimos[columna], maximos[columna])
        else:   # No está en la columna de mínimos, está en la de cadenas.
            res[columna] = tuple(cadenas[columna])
    return res


def parse_rango(valor):
    """
    Analiza el rango y devuelve el valor inferior y superior.
    Como el último valor de la unión de todos los rangos para la columna
    siempre es cerrado, da igual si el extremo del que estamos tratando ahora
    es abierto o cerrado.
    Si el máximo valor es infinito, devuelve el máximo entero permitido por
    la máquina. ¿Podría dar problemas en ordenadores con otro máximo definido
    cuando interprete el Javascript? Haré una cosa, infinito lo equipararé
    al mínimo máximo garantizado que devuelve python para sys.maxint.
    """
    valor = valor.replace(
        "[", "").replace("(", "").replace("]", "").replace(")", "")
    # pylint: disable=invalid-name
    x, y = valor.split("..")
    infinito = 2**31 - 1
    try:
        ini = parse_numero(x)
    except (TypeError, ValueError):
        ini = -infinito - 1     # -1 por la simetría.
    try:
        fin = parse_numero(y)
    except (TypeError, ValueError):
        fin = infinito
    return ini, fin


def es_rango_numerico(valor):
    """
    Devuelve True si el valor recibido es un rango numérico.
    """
    res = ".." in valor
    return res


def parse_numero(valor):
    """
    Convierte el valor recibido en un entero o en un float, dependiendo de
    si lleva o no decimales.
    """
    try:
        valor = valor.replace(",", ".")
        res = float(valor)
    except AttributeError:  # No es una cadena. ¿?
        if isinstance(valor, (int, float)):
            res = valor
        else:
            raise ValueError("El valor recibido «{}» no se puede parsear"
                             " como número".format(valor))
    if res % 1 == 0:
        # pylint: disable=redefined-variable-type
        res = int(res)
    return res


def es_numero(valor):
    """
    Determina si un número es interpretable como entero o floante.
    """
    try:
        parse_numero(valor)
        res = True
    except (TypeError, ValueError):
        res = False
    return res


def update_cadenas(cadenas, columna, valor):
    """
    Si la cadena no está ya en la lista de valores para esa columna según
    el diccionario, la agrega y vuelve a ordenar.
    """
    if cadenas[columna] is None:
        cadenas[columna] = [valor]
    elif valor not in cadenas[columna]:
        cadenas[columna].append(valor)
        cadenas[columna].sort()


def update_minimos(minimos, columna, numero):
    """
    Actualiza el diccionario de mínimos con el valor recibido para la columna
    indicada.
    """
    if minimos[columna] is None:
        minimos[columna] = numero
    elif minimos[columna] > numero:
        minimos[columna] = numero


def update_maximos(maximos, columna, numero):
    """
    Actualiza el diccionario de máximos con el valor recibido para la columna
    indicada.
    """
    if maximos[columna] is None:
        maximos[columna] = numero
    elif maximos[columna] < numero:
        maximos[columna] = numero


if __name__ == "__main__":
    main()
