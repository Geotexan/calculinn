#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Script para generar un fichero python equivalente al CSV de modo que para
usar los datos solo hay que importarlo en lugar de parsear el CSV, que da
problemas a causa del "same origin policy" de JavaScript.
"""


from __future__ import print_function
import sys
import csv


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
            continue
        res.append(tuple(fila))
    return cabecera, res


def generate(nombre_fout, cabecera, datos):
    """
    Crea un fichero python muy sencillo (si existe, lo sobreescribe) que
    instancia la cabecera y filas de datos al ser importado.
    """
    skel = ["#!/usr/bin/env python\n"]
    skel.append("# -*- coding: utf-8 -*-\n")
    skel.append("CABECERA = {}\n".format(cabecera))
    skel.append("TABLA = {}\n".format(datos))
    fout = open(nombre_fout, "w")
    fout.writelines(skel)
    fout.close()


def main():
    """
    Abre el fichero CSV de entrada y genera un fichero python que carga
    automáticamente al ser importado como módulo la cabecera y las filas
    de cálculo.
    """
    if len(sys.argv) < 2:
        print("Debes especificar el fichero de entrada.", file=sys.stderr)
    else:
        nombre_fin = sys.argv[1]
        try:
            nombre_fout = sys.argv[2]
        except IndexError:
            nombre_fout = nombre_fin.replace(".csv", ".py")
        try:
            fin = open(nombre_fin)
        except IOError:
            # print("El fichero {} no existe.".format(nomfichero))
            sys.exit(1)
        cabecera, datos = parse(fin)
        generate(nombre_fout, cabecera, datos)
        fin.close()
        sys.exit(0)

if __name__ == "__main__":
    main()
