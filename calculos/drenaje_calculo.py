#!/usr/bin/env python
# -*- coding: utf-8 -*-

NUMENTRADAS = 3
NUMSALIDAS = 6
CABECERA = (u'Tipo terreno (desplegable)', u'Tipo \xe1rido (desplegable)', u'D. m\xe1x', u'Rt', u'Elong.', u'R CBR perf', u'R perf cono', u'Abertura poro', u'K vert', u'Es para cotejar los valores. No se muestra en el formulario.', u'Producto recomendado')
CALCULO = [(u'Cohesivo', u'Machacado', u'[0..60)', u'7', u'50', u'1200', u'<35', u'<0,075', u'>90', u'NT 12'), (u'Cohesivo', u'Machacado', u'[60..100)', u'7,5', u'50', u'1300', u'<35', u'<0,07', u'>90', u'NT 12'), (u'Cohesivo', u'Machacado', u'[100..\u221e]', u'8', u'50', u'1500', u'<35', u'<0,065', u'>90', u'NT 13'), (u'Cohesivo', u'Redondeado', u'[0..60)', u'5', u'50', u'1000', u'<40', u'<0,08', u'>90', u'NT 10'), (u'Cohesivo', u'Redondeado', u'[60..100)', u'6', u'50', u'1100', u'<40', u'<0,075', u'>90', u'NT 11'), (u'Cohesivo', u'Redondeado', u'[100..\u221e]', u'7', u'50', u'1200', u'<35', u'<0,075', u'>90', u'NT 12'), (u'No cohesivo', u'Machacado', u'[0..60)', u'7,5', u'50', u'1300', u'<35', u'<0,07', u'>90', u'NT 12'), (u'No cohesivo', u'Machacado', u'[60..100)', u'6', u'50', u'1100', u'<40', u'<0,075', u'>90', u'NT 11'), (u'No cohesivo', u'Machacado', u'[100..\u221e]', u'7', u'50', u'1200', u'<35', u'<0,075', u'>90', u'NT 12'), (u'No cohesivo', u'Redondeado', u'[0..60)', u'7,5', u'50', u'1300', u'<35', u'<0,07', u'>90', u'NT 12'), (u'No cohesivo', u'Redondeado', u'[60..100)', u'7', u'50', u'1200', u'<35', u'<0,075', u'>90', u'NT 12'), (u'No cohesivo', u'Redondeado', u'[100..\u221e]', u'7,5', u'50', u'1300', u'<35', u'<0,07', u'>90', u'NT 12')]
RANGOS = {u'Tipo terreno (desplegable)': (u'Cohesivo', u'No cohesivo'), u'D. m\xe1x': (0, 2147483647), u'Tipo \xe1rido (desplegable)': (u'Machacado', u'Redondeado')}