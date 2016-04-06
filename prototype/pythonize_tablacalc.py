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
    res = False  # res es True si hay algún valor numérico, = NO cabecera.
    for valor in lista:
        hay_al_menos_un_valor_numerico = False
        for caracter in valor:
            if caracter.isdigit():
                hay_al_menos_un_valor_numerico = (
                    hay_al_menos_un_valor_numerico or True)
        res = res or hay_al_menos_un_valor_numerico
        if res:     # OPTIMIZACIÓN: Si he encontrado uno, me salgo.
            break
    return not res


def parse(fin):
    """
    Con el fichero «fin» **ya abierto** crea un "reader" de csv y lee todos
    los valores. Devuelve una lista con los campos cabecera y otra lista
    de listas con los valores de referencia de cálculo (filas de celdas).
    """
    res = []
    cabecera = ()
    reader = csv.reader(fin)
    for fila in reader:
        if es_cabecera(fila):
            # La segunda cabecera, la de verdad, machacará a la de (In, Out).
            cabecera = fila
            if "In" in cabecera:    # Ojo, es la fila que me dice cuántas
                # entradas y salidas tiene la tabla de cálculo.
                numentradas, numsalidas = find_ins_outs(cabecera)
            continue
        res.append(tuple(fila))
    return cabecera, res, numentradas, numsalidas


def find_ins_outs(fila):
    """
    Devuelve el número de entradas y salidas que indica la primera cabecera.
    """
    # NOTE: Quedaría el caso de las constantes, que siempre van antes de los
    # In. También está el caso de los desplegables, indicado en el nombre
    # de la variable de entrada, pero eso es otra historia.
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


def generate(nombre_fout, cabecera, datos, numentradas, numsalidas):
    """
    Crea un fichero python muy sencillo (si existe, lo sobreescribe) que
    instancia la cabecera y filas de datos al ser importado.
    """
    skel = ["#!/usr/bin/env python\n"]
    skel.append("# -*- coding: utf-8 -*-\n\n")
    skel.append("NUMENTRADAS = {}\n".format(numentradas))
    skel.append("NUMSALIDAS = {}\n".format(numsalidas))
    skel.append("CABECERA = {}\n".format(cabecera))
    skel.append("TABLA = {}\n".format(datos))
    fout = open(nombre_fout, "w")
    fout.writelines(skel)
    fout.close()


def parse_opendocument(fin):
    """
    Con el fichero «fin» **ya abierto** lee todos los valores de las filas.
    Devuelve una lista con los campos cabecera y otra lista
    de listas con los valores de referencia de cálculo (filas de celdas).
    """
    res = []
    cabecera = ()
    doc = load(fin)
    tables = doc.spreadsheet.getElementsByType(Table)
    table = tables[0]   # Sólo tienen 1 hoja
    rows = table.getElementsByType(TableRow)
    for row in rows:
        fila = convert_odrow(row)
        if es_cabecera(fila):
            # La segunda cabecera, la de verdad, machacará a la de (In, Out).
            cabecera = fila
            if "In" in cabecera:    # Ojo, es la fila que me dice cuántas
                # entradas y salidas tiene la tabla de cálculo.
                numentradas, numsalidas = find_ins_outs(cabecera)
            continue
        res.append(fila)
    return cabecera, res, numentradas, numsalidas


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
        cabecera, datos, numentradas, numsalidas = parse(fin)
    else:   # Es un OpenDocument (.ods).
        cabecera, datos, numentradas, numsalidas = parse_opendocument(fin)
    generate(nombre_fout, cabecera, datos, numentradas, numsalidas)
    fin.close()
    sys.exit(0)

if __name__ == "__main__":
    main()
