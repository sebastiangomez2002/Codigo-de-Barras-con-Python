"""
PILDORA A INSTALAR:

pip install python-barcode

"""

import barcode
from barcode.writer import ImageWriter
from barcode import writer

# DEFINIR EL CONTENIDO DEL CODIGO DE BARRAS

number = input("INGRESA EL CODIGO DE ONCE DIGITOS")

# DEFINIR FORMATO DEL CODIGO DE BARRAS

barcode_format = barcode.get_barcode_class("upc")

# GENERAR CODIGO DE BARRAS E IMAGEN

my_barcode = barcode_format(number, writer=ImageWriter())

# GUARDAR IMAGEN Y DAR NOMBRE

my_barcode.save("codigo_barras")