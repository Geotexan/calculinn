#!/bin/sh

# Crea los PDF combinados de GEOTEXGRID. Se recomiendan dos versiones
# y es necesario unir sus fichas técnicas en un solo PDF.

pdfunite ../pdf/1-4-151_geotexgrid_I35-20.pdf  ../pdf/1-4-38_geotexgrid_C35-30.pdf     ../pdf/geotexgrid_I35-20_C35-30.pdf
pdfunite ../pdf/1-4-113_geotexgrid_I55-30.pdf  ../pdf/1-4-85_geotexgrid_C55-30.pdf     ../pdf/geotexgrid_55-30.pdf
pdfunite ../pdf/1-4-152_geotexgrid_I80-30.pdf  ../pdf/1-4-98-1_geotexgrid_C60-30.pdf   ../pdf/geotexgrid_I80-30_C60-30.pdf
pdfunite ../pdf/1-4-152_geotexgrid_I80-30.pdf  ../pdf/1-4-86_geotexgrid_C80-30.pdf     ../pdf/geotexgrid_80-30.pdf
pdfunite ../pdf/1-4-123_geotexgrid_I100-30.pdf ../pdf/1-4-150_geotexgrid_C90-30.pdf    ../pdf/geotexgrid_I100-30_C90-30.pdf
pdfunite ../pdf/1-4-123_geotexgrid_I100-30.pdf ../pdf/1-4-109_geotexgrid_C100-30.pdf   ../pdf/geotexgrid_100-30.pdf
pdfunite ../pdf/1-4-121_geotexgrid_I110-30.pdf ../pdf/1-4-87_geotexgrid_C110-30.pdf    ../pdf/geotexgrid_110-30.pdf
pdfunite ../pdf/1-4-153_geotexgrid_I150-30.pdf ../pdf/1-4-100-1_geotexgrid_C120-30.pdf ../pdf/geotexgrid_I150-30_C120-30.pdf
pdfunite ../pdf/1-4-153_geotexgrid_I150-30.pdf ../pdf/1-4-110_geotexgrid_C150-30.pdf   ../pdf/geotexgrid_150-30.pdf
