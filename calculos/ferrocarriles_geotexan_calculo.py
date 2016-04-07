#!/usr/bin/env python
# -*- coding: utf-8 -*-

NUMENTRADAS = 3
NUMSALIDAS = 4
CABECERA = (u'CBR', u'D m\xe1x', u'Espesor', u'Rt', u'Elong', u'R CBR perf', u'K vert', u'Solo para cotejar valores. El formulario no lo muestra.', u'Producto recomendado')
CALCULO = [(u'[0..1)', u'[0..150)', u'[200..400)', u'17', u'50', u'3', u'>25', u'NT 25'), (u'[0..1)', u'[0..150)', u'[400..\u221e]', u'16', u'50', u'2,6', u'>25', u'NT 23'), (u'[0..1)', u'[150..300)', u'[400..\u221e]', u'20', u'50', u'3,3', u'>25', u'NT 30'), (u'[1..\u221e]', u'[0..150)', u'[200..400)', u'16', u'50', u'2,6', u'>25', u'NT 23'), (u'[1..\u221e]', u'[0..150)', u'[400..\u221e]', u'16', u'50', u'2,6', u'>25', u'NT 23'), (u'[1..\u221e]', u'[150..300)', u'[200..400)', u'19', u'50', u'3', u'>25', u'NT 25'), (u'[1..\u221e]', u'[150..300)', u'[400..\u221e]', u'16', u'50', u'2,6', u'>25', u'NT 23'), (u'[1..\u221e]', u'[300..400)', u'En la tabla original va de 450 a 600. Para no dejar hueco, ampl\xedo el rango.', u'[400..600)', u'21', u'50', u'3,8', u'>25', u'NT 35'), (u'[1..\u221e]', u'[400..500)', u'[600..750)', u'24', u'50', u'4,4', u'>15', u'NT 40'), (u'[1..\u221e]', u'[500..600)', u'[750..900)', u'27', u'50', u'5,1', u'>15', u'NT 46'), (u'[1..\u221e]', u'[600..\u221e)', u'[900..\u221e]', u'30', u'50', u'6', u'>15', u'NT 58')]
RANGOS = {u'CBR': (0, 2147483647), u'Espesor': (200, 2147483647), u'D m\xe1x': (0, 2147483647)}