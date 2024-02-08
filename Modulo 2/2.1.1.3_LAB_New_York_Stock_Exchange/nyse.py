"""
nyse.py -- Creado por Rui Duarte dos Santos Melim.

Escenario:
Tenemos un pequeño extracto de la lista de cotizaciones de la Bolsa de
Valores de Nueva York para analizar su estructura (ver archivo nyse.xml).

Escribir un código que lea los datos y los presente en una forma similar
a la mostrada en la imagen nyse.jpg.

Consejos:
1.- No olvidar controlar al menos dos posibles excepciones: 
FileNotFoundError y xml.etree.ElementTree.ParseError.
2.- Siéntase libre de mejorar y embellecer la salida.
"""
import sys
import xml.etree.ElementTree

# Nombres de los atributos en el XML que también se usarán de encabezado.
KEY_NAMES = ["company", "last", "change", "min", "max"]
KEY_WIDTHS = [40, 10, 10, 10, 10]  # Ancho para cada columna.

# Se lee el XML y se crea un objeto a partir de sus elementos.
#
# Se comprueba que exista el archivo XML y que sus datos sean válidos.
try:
    companies = xml.etree.ElementTree.parse("nyse.xml").getroot()
except FileNotFoundError:
    print("XML file no exist.")
    sys.exit()
except xml.etree.ElementTree.ParseError:
    print("XML parser error. Data not valid.")
    sys.exit()

# Se construye el encanezado de la tabla de datos impresa a partir de
# las constantes KEY_NAMES y KEY_WIDTHS.
for name, width in zip(KEY_NAMES, KEY_WIDTHS):
    print(name.center(width).upper(), end="")
print()
print("-" * sum(KEY_WIDTHS))


for company in companies:
    for name, width in zip(KEY_NAMES, KEY_WIDTHS):
        if name == "company":
            print(company.text.ljust(width), end="")
        else:
            print(company.attrib[name].rjust(width), end="")
    print()
