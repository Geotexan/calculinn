#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Prototipo de cálculo y recomendación para la aplicación de muros.
"""

# import sys
# import re     # NS_ERROR_DOM_BAD_URI: No puedo importar nada.


# pylint: disable=invalid-name, too-many-arguments, too-many-locals
def calcular(tabla, e, a, h, i, d, s):
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
# TODO: Recibir parámetros como opcionales para que valga para todas las tablas
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
            # Sanitize:
            try:
                valor = valor.strip().upper()
            except AttributeError:
                pass
            # Si no es rango ni cadena, lo convierto ya a entero para comparar
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
        if ".." in referencia:  # Es un rango.
            res = valor_in_rango(valor, referencia)
        else:   # Es cadena. Las entradas se pasaron a upper también arriba.
            res = valor == referencia.strip().upper()
    else:   # Es númerico.
        res = valor == referencia
    return res


def valor_in_rango(valor, rango):
    """
    Recibe el valor, que puede ser float, y un rango como cadena. Devuelve
    True si el valor está dentro del rango.
    """
    # Había una manera más "pythónica" de hacerlo, pero no valía para floats.
    ini = rango[0]
    fin = rango[-1]
    strx, stry = rango.split("..")
    strx = strx.replace("(", "").replace("[", "").replace(",", ".")
    stry = stry.replace(")", "").replace("]", "").replace(",", ".")
    x = float(strx)
    y = float(stry)
    evals = []  # Almacenaré los resultados de cada una de las evaluaciones
    # Evalúo el extremo inferior:
    if ini == "(":      # Abierto
        condicion_ini = valor > x
    elif ini == "[":    # Cerrado
        condicion_ini = valor >= x
    else:
        raise ValueError("El inicio del intervalo debe ser ( o [.")
    evals.append(condicion_ini)
    if fin == ")":      # Abierto
        condicion_fin = valor < y
    elif fin == "]":    # Cerrado
        condicion_fin = valor <= y
    else:
        raise ValueError("El fin del intervalo debe ser ) o ].")
    evals.append(condicion_fin)
    # Y al final evaluaré si todas son True o no.
    res = check_aciertos(evals)
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


def recomendar(tabla, *args):
    """
    De manera análiga a `calcular`, realiza las comapraciones y devuelve
    la fila que satisface todos los valores de entrada o None si no se
    encuentra ninguna.
    """
    return calcular(tabla, *args)
