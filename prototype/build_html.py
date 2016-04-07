#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Indicando un par de ficheros de entrada (tabla de cálculo y tabla de
recomendación de producto) y la aplicación (muros, verdereros, etc.) crea
el fichero HTML (basado en skel.html) y las tablas "pythonizadas"
correspondientes que serán cargadas por brython en el navegador.
"""

from __future__ import print_function
import sys
import os
import re
import argparse


def longest_substring_finder(string1, string2):
    """
    http://stackoverflow.com/questions/18715688/find-common-substring-between-two-strings
    """
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        match = ""
        for j in range(len2):
            if i + j < len1 and string1[i + j] == string2[j]:
                match += string2[j]
            else:
                if len(match) > len(answer):
                    answer = match
                match = ""
    return answer


def sanitize(cad):
    """
    Devuelve la cadena recibida sustituyendo los caracteres con tilde,
    guiones, etc.
    """
    cad = cad.lower()
    for bad, good in (('á', 'a'), ('é', 'e'), ('í', 'i'),
                      ('ó', 'o'), ('ú', 'u'), ('-', '_')):
        cad = cad.replace(bad, good)
    return cad


def find_nombre_comun_ficheros(tabla_calculo, tabla_recomendador,
                               sanitizar=True):
    """
    A partir de los nombres de los ficheros, obtiene el nombre común que
    llevarán los ficheros generados. Sin extensión.
    Si sanitizar está a True, elimina los caracteres problemáticos.
    """
    nombre_calculo = os.path.basename(tabla_calculo)
    nombre_recomendador = os.path.basename(tabla_recomendador)
    try:
        nombre_comun = re.findall(r"[^\(]*\.html", nombre_calculo)[0]
        nombre_comun = nombre_comun.replace(".html", "")
    except IndexError:
        nombre_comun = longest_substring_finder(nombre_calculo,
                                                nombre_recomendador)
    if sanitizar:
        nombre_comun = sanitize(nombre_comun)
    if not nombre_comun:    # Algo hay que devolver o creará ficheros ocultos
        nombre_comun = os.path.basename(tabla_calculo).split(".")[0]
    return nombre_comun


def escape_chars(ruta):
    """
    Devuelve la misma ruta pero entrecomillada para que al pasrala como
    parámetro a os.system, no pete.
    """
    ruta = "'" + ruta.replace("'", "'\\''") + "'"
    return ruta


def pythonize_tablas(ruta_calculo, ruta_recomendador):
    """
    ruta_calculo y ruta_recomendador son la ruta a las dos tablas en CSV o ODS.
    Ejecuta un script externo que convierte ambas tablas en sendo módulos
    python conteniendo la base de conocimiento.
    """
    ruta_script = os.path.dirname(os.path.abspath(__file__))
    script = os.path.join(ruta_script, "pythonize_tablacalc.py")
    res = []
    salida = find_nombre_comun_ficheros(ruta_calculo, ruta_recomendador)
    for ruta_tabla, pyout in ((ruta_calculo, salida + "_calculo.py"),
                              (ruta_recomendador,
                               salida + "_recomendador.py")):
        comando = "{} {} -o {}".format(script, escape_chars(ruta_tabla),
                                       escape_chars(pyout))

        retcode = os.system(comando)
        if retcode == 0:
            print("{} generado.".format(pyout))
            res.append(pyout)
        else:
            raise ValueError("Comando `{}` falló.\nSalida {}.".format(comando,
                                                                      retcode))
    return res[0], res[1]


def templatear(linea, calculo, recomendador, aplicacion):
    """
    Devuelve la línea recibida pero realizando las sustituciones pertinentes.
    """
    if "SKEL_" in linea:
        lista_subs = (("SKEL_TITULO", aplicacion.title()),
                      ("SKEL_RECOMENDADOR", recomendador.replace(".py", "")),
                      ("SKEL_CALCULO", calculo.replace(".py", "")),
                      ("SKEL_HEAD",
                       "Cálculo de parámetros para {}".format(
                           aplicacion.replace("_", " ").replace("_", " "))))
        for snippet, valor in lista_subs:
            if snippet in linea:
                linea = linea.replace(snippet, valor)
    return linea


# pylint: disable=too-many-arguments
def generate_html(pycalculo, pyrecomendador, aplicacion, dir_dest,
                  ruta_calculo, ruta_recomendador):
    """
    Copia el fichero esqueleto skel.html en la ruta destino y sustituye los
    valores del "template" por los que le corresponden.
    """
    if aplicacion is None:
        aplicacion = find_nombre_comun_ficheros(ruta_calculo,
                                                ruta_recomendador)
        aplicacion = aplicacion.replace("-", " ").replace("_", " ")
    ruta_skel = os.path.dirname(os.path.abspath(__file__))
    skel = os.path.join(ruta_skel, "skel.html")
    fskel = open(skel)
    nombre_html = find_nombre_comun_ficheros(ruta_calculo, ruta_recomendador)
    if not nombre_html.endswith(".html"):
        nombre_html += ".html"
    ruta_html = os.path.join(dir_dest, nombre_html)
    fhtml = open(ruta_html, "w")  # Si existe, los sobrescribe.
    for linea in fskel.readlines():
        linea_tratada = templatear(linea, pycalculo, pyrecomendador,
                                   aplicacion)
        fhtml.write(linea_tratada)
    fskel.close()
    fhtml.close()
    return ruta_html


def determinar_tablas(tablas):
    """
    Si recibe una lista de 2 elementos, los devuelve tal cual.
    Pero si recibe una lista de 1 elemento o una cadena directamente,
    determina qué otro fichero de tabla le correspondería y devuelve ambos.
    Para saber si la tabla se refiere al cálculo o a la recomendación, mira
    el tercer carácter. Todas las tablas siguen la nomenclatura:
    xyz aplicacion (fich_html).[ods|csv]
    Donde:
    x = Número de la pantalla de aplicación. De 0 a 7.
    y = Número del subformulario de la aplicación. De 0 en adelante. Si solo
        hay una página para esa aplicación, el valor es 0.
    z = Número del formulario dentro de la página de la aplicación.
        0 = formulario de cálculo.
        1 = formulario de recomendación.
    Devuelve las tablas en orden. Primero la 0 (cálculo) y después la 1.
    """
    try:
        tabla1 = tablas[0]
    except IndexError:  # No es una lista.
        tabla1 = tablas
    try:
        tabla2 = tablas[1]
    except IndexError:  # No es una lista o, si lo es, no trae la 2.ª tabla.
        nombre = os.path.basename(tabla1)
        ruta = os.path.dirname(tabla1)
        if nombre[2] == "0":
            tabla2 = os.path.join(ruta, nombre[:2] + "1" + nombre[3:])
        elif nombre[2] == "1":
            tabla2 = os.path.join(ruta, nombre[:2] + "0" + nombre[3:])
        else:
            raise ValueError("Los nombres de las tablas no siguen el "
                             "estándar: {}".format(tablas))
        # Ahora corrijo el nombre de tabla2, porque la numeración es correcta,
        # pero seguramente la segunda parte del fichero sea "_geotextil" en
        # lugar de "_geotexan" o "_calculo" como es en tabla1 (o viceversa).
        tabla2 = fuzzy_finder(tabla2)
    res = [tabla1, tabla2]
    res.sort()
    return res[0], res[1]


def fuzzy_finder(ruta):
    """
    Detrás de este nombre tan pomposo y arribista lo único que se esconde
    es un algoritmo para buscar el fichero en la ruta recibida que comience
    por el prefijo de «ruta». Es decir, `xyz aplic_subform(fich.html).ods`.
    """
    res = None
    directorio = os.path.dirname(ruta)
    if not directorio:
        directorio = "."
    nombre = os.path.basename(ruta)
    for fichero in os.listdir(directorio):
        if fichero.startswith(nombre[:3]):
            res = os.path.join(os.path.dirname(ruta), fichero)
            break
    if not res:
        raise ValueError("No se pudo encontrar el equivalente a {} en {}"
                         ".".format(ruta, directorio))
    return res


def main():
    """
    Establece las opciones del script, "pythoniza" usando otro script externo
    ambos ficheros y genera el HTML usando la plantilla indicada en el
    directorio actual si no se especifica otro.
    """
    parser = argparse.ArgumentParser(description="Script para generar el "
                                     "HTML y módulos asociados para el cálculo"
                                     " y recomendación del producto de "
                                     "Geotexan para la aplicación indicada.")
    parser.add_argument("tabla", help="Fichero(s) ODS o CSV de la "
                        "tabla que guarda los cálculos de parámetros o el"
                        "producto recomendado en función de esos parámetros"
                        " calculados. Se puede especificar uno, otro o los "
                        "dos.", nargs="+")
    parser.add_argument("-a", "--aplicacion", help="Aplicación a la que "
                        "se corresponden los ficheros de entrada. Si no se "
                        "espeficica, se determinará a partir de los nombres "
                        "de los ficheros de entrada.", dest="aplicacion",
                        type=str, default=None)
    parser.add_argument("-d", "--destino", help="Ruta destino donde se "
                        "generarán todos los ficheros.", dest="ruta_dest",
                        default=".")
    args = parser.parse_args()
    if len(args.tabla) > 2:
        parser.print_help()
        sys.exit(1)
    tabla_calculo, tabla_recomendador = determinar_tablas(args.tabla)
    pycalculo, pyrecomendador = pythonize_tablas(tabla_calculo,
                                                 tabla_recomendador)
    # pycalculo y pyrecomendador es el nombre del fichero python, sin ruta.
    ruta_html = generate_html(pycalculo, pyrecomendador, args.aplicacion,
                              args.ruta_dest, tabla_calculo,
                              tabla_recomendador)
    print("Fichero {} generado.".format(ruta_html))
    sys.exit(0)


if __name__ == "__main__":
    main()
