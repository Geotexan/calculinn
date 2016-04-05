#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Prototipo de cálculo y recomendación para la aplicación de muros.
"""

from __future__ import print_function
import sys
import argparse
import csv
import re


def main():
    """
    Abre los ficheros fuente de cálculo de parámetros y de recomendación de
    producto para la aplicación en muros.
    Lee los seis parámetros de entrada desde la línea de comandos y recorre
    todas las filas de los ficheros fuente determinando si algún valor
    cumple con las entradas. En caso contrario, muestra error.
    """
    # NOTE: Solo acepta enteros como entrada para los valores. De momento nada
    # de cadenas (en carreteras se usa) ni floats (algunos valores son float
    # en realidad, incluso aquí en muros).
    parser = argparse.ArgumentParser(description="Prototipo cálculo muros.")
    parser.add_argument("-e", "--espesor", "--tongada", dest="e",
                        help="Espesor tongada de relleno (cm) t",
                        default=None, type=int)
    parser.add_argument("-a", "--angulo", "--rozamiento", dest="a",
                        help="Ángulo de rozamiento de relleno (grados) φ",
                        default=None, type=int)
    parser.add_argument("-l", "--altura", dest="h",
                        help="Altura de muro (m) H",
                        default=None, type=int)
    parser.add_argument("-i", "--inclinacion", dest="i",
                        help="Inclinación de muro (grados) α",
                        default=None, type=int)
    parser.add_argument("-d", "--densidad", dest="d",
                        help="Densidad relleno (t/m³) Υ",
                        default=None, type=int)
    parser.add_argument("-s", "--sobrecarga", dest="s",
                        help="Sobrecarga (kN/m²) P",
                        default=None, type=int)
    if len(sys.argv) < 7:
        parser.print_help()
        sys.exit(1)
    else:
        args = parser.parse_args()
        calculo, header_calculo = parse_calculo()
        catalogo, header_recomendacion = parse_recomendacion()
        out_calculo = calcular(args.e, args.a, args.h, args.i, args.d, args.s,
                               calculo)
        out_recomendacion = recomendar(args.e, args.a, args.h, args.i, args.d,
                                       args.s, catalogo)
        entradas = (args.e, args.a, args.h, args.i, args.d, args.s)
        if out_calculo:
            dump(entradas, out_calculo, header_calculo,
                 nombre_calculo="Cálculo Geotexan")
        else:
            print("Combinación de parámetros incorrecta para cálculo.",
                  file=sys.stderr)
            sys.exit(2)
        if out_recomendacion:
            dump(entradas, out_recomendacion, header_recomendacion,
                 nombre_calculo="Geocompuesto recomendado")
        else:
            print("Combinación de parámetros incorrecta para recomendación.",
                  file=sys.stderr)
            sys.exit(3)
        sys.exit(0)


def parse_calculo(nomfichero="400 muro_Geotexan (muro-contencion.html).csv"):
    """
    Abre el fichero de la tabla de cálculo y lee todas las líneas para
    devolver una lista de tuplas de la siguiente forma:
    [
     (50, "[25..35)", "[0..5)", "[50..60)", ...),
     (50, "[25..35)", ...),
    ...
    ]
    Cada valor de esas listas contiene un número o un rango (como cadena) para
    comparar con los valores de entrada recibidos (e, a, h, i, d, s), que
    están en el mismo orden en el fichero de entrada. El resto de valores (del
    séptimo en adelante) se consideran valores de salida.
    También devuelve una tupla con los nombres de los parámetros en el mismo
    orden.
    """
    res = []
    cabecera = ()
    try:
        file_in = open(nomfichero)
    except IOError:
        print("El fichero {} no existe.".format(nomfichero))
        sys.exit(4)
    reader = csv.reader(file_in)
    for fila in reader:
        if es_cabecera(fila):
            # La segunda cabecera, la de verdad, machacará a la de (In, Out).
            cabecera = fila
            continue
        res.append(tuple(fila))
    return res, cabecera


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


def parse_recomendacion(nomfi="401 muro_geomalla (muro-contencion.html).csv"):
    """
    "Parsea" y devuelve una lista de tuplas similar a la de parse_calculo.
    """
    return parse_calculo(nomfi)


# pylint: disable=invalid-name, too-many-arguments, too-many-locals
def calcular(e, a, h, i, d, s, tabla):
    """
    Compara la combinación de los seis valores de entrada (e, a, h, i, d, s)
    con cada una de las listas del array bidimensional «tabla». Devuelve la
    primer lista con la que coincida o None si no hay coincidencia.
    Las listas pueden contener números enteros, un valor de cadena o un
    rango de valores como string (por ejemplo: "[25..35)"). En este último
    caso se parsea la cadena y se obtiene el rango correspondiente con el que
    se compara el valor.
    El orden de los parámetros recibidos y el de la lista con los rangos a
    comparar **debe ser el mismo**.
    El cálculo se hace por fuerza bruta y es O(n). Podría hacerse O(log_n) si
    se implementara como árbol de decisión, PERO NO HAY TIEMPO Y ESTO ES SÓLO
    UN PROTOTIPO que acabará en JavaScript.
    """
    res = None
    for fila in tabla:
        aciertos = []
        espesor, angulo, altura, inclinacion, densidad, sobrecarga = fila[:6]
        for valor, referencia in ((e, espesor),
                                  (a, angulo),
                                  (h, altura),
                                  (i, inclinacion),
                                  (d, densidad),
                                  (s, sobrecarga)):
            if referencia.isdigit():    # OJO: Solo vale para enteros.
                referencia = int(referencia)
            resultado = comparar(valor, referencia)
            aciertos.append(resultado)
        if check_aciertos(aciertos):
            res = fila
            break
    return res


def comparar(valor, referencia):
    """
    Aquí está el meollo de la cuestión. Se trata de interpretar el valor de
    referencia. Si es un número, directamente hace la comparación de
    igualdad.
    Si es una cadena:
        - Si es interpretable como rango --conteiene extremos abiertos o
          cerrados en la forma "[|]|(|)"-- determina si el valor está dentro
          del rango.
        - En otro caso hace una comaración como cadena (para los casos como el
          de carretera, aunque no se den en aquí en muros).
    """
    if isinstance(referencia, str):
        # NOTE: Esto en Javascript seguramente haya que hacerlo de otra forma.
        if ".." in referencia:  # Es un rango.
            res = valor in parse_rango(referencia)
        else:   # Es cadena.
            res = valor == referencia
    else:   # Es númerico.
        res = valor == referencia
    return res


def parse_rango(str_rango):
    """
    Devuelve un rango numérico correspondiente al rango recibido como cadena.
    La cadena siempre tiene la forma "[(x..y)]" donde el primer y el último
    carácter indican si es un intervalo abierto «()» o cerrado «[]» en cada
    extremo.
    `x` es el extermo inferior.
    `y` es el extremo superior (puede ser infinito: ∞)
    """
    regex = re.compile(r"[\[\(]([0-9]+)\.\.([0-9]+|∞)[\]\)]")
    matcheds = regex.findall(str_rango)  # Tupla de listas coincidentes. Cada
    # lista "interna" tiene un valor por cada grupo de la expresión regular.
    x, y = matcheds[0]
    if str_rango[0] == "(":
        x = int(x) + 1  # Como todos los valores son enteros, me vale así.
        # Si fueran floats habría que montar los ifs con > y >=. Nada de rangos
    elif str_rango[0] == "[":
        x = int(x)
    if str_rango[-1] == ")":
        if y.isdigit():
            y = int(y)
        else:   # Infinito. Me da igual si el extermo es abierto o cerrado:
            y = sys.maxint  # El máximo entero permitido por la máquina.
    elif str_rango[-1] == "]":
        y = int(y) + 1
    res = range(x, y)
    return res


def check_aciertos(aciertos):
    """
    Comprueba si todos los valores comparados recibidos en la tupla de
    booleanos «aciertos» son True (coinciden todos los valores de entrada
    con los valores de la tabla).
    """
    res = True  # Si alguno es False, res acabará a False.
    for resultado in aciertos:
        res = res and resultado
    return res


def recomendar(e, a, h, i, d, s, tabla):
    """
    De manera análiga a `calcular`, realiza las comapraciones y devuelve
    la fila que satisface todos los valores de entrada o None si no se
    encuentra ninguna.
    """
    return calcular(e, a, h, i, d, s, tabla)


def dump(entradas, fila, cabecera, num_params_entrada=6, nombre_calculo=""):
    """
    Muestra por pantalla el resultado del cálculo o la recomendación.
    Recibe la fila que satisface todos los valores de entrada y una lista
    con los nombres de los parámetros --cabeceras de la tabla--.
    Como parámetro opcional recibe el índice hasta el que los parámetros
    de la fila resultante eran de entrada (-1). El resto se consideran de
    salida.
    «entradas» son los parámetros de entrada que recogió el script para
    hacer los cálculos y determinar los valores de aplicación.
    """
    print(nombre_calculo)
    print("=" * len(nombre_calculo))
    print("Entrada:")
    for i, nombre_parametro in enumerate(cabecera[:num_params_entrada]):
        print("\t{}: {} ({})".format(nombre_parametro,
                                     entradas[i],
                                     fila[i]))
    print("Salida:")
    for i, nombre_parametro in enumerate(cabecera[num_params_entrada:]):
        print("\t{}: {}".format(nombre_parametro,
                                fila[num_params_entrada + i]))
    print()


if __name__ == "__main__":
    main()
