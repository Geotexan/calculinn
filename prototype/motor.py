#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Prototipo de cálculo y recomendación para la aplicación de muros.
"""

# import sys
# import re     # NS_ERROR_DOM_BAD_URI: No puedo importar nada.


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
    _x, _y = str_rango.split("..")
    _x = "".join([i for i in _x if i.isdigit()])
    _y = "".join([i for i in _y if i.isdigit()])
    if str_rango[0] == "(":
        x = int(_x) + 1  # Como todos los valores son enteros, me vale así.
        # Si fueran floats habría que montar los ifs con > y >=. Nada de rangos
    elif str_rango[0] == "[":
        x = int(_x)
    if str_rango[-1] == ")":
        if _y.isdigit():
            y = int(_y)
        else:   # Infinito. Me da igual si el extermo es abierto o cerrado:
            # y = sys.maxint  # El máximo entero permitido por la máquina.
            y = 99999  # No puedo sys.maxint, así que número grande arbitrario.
    elif str_rango[-1] == "]":
        y = int(_y) + 1
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
