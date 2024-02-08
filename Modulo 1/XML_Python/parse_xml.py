"""
Código ejemplo de la clase 1.5.1.7

Analizar un documento XML.

Entre lasa herramientas posibles de Python que le permiten crear, 
escribir, leer, analizar y modificar archivos XML está el paquete
xml.etree. 

La mayoría de estas herramientas, xml.etree entre ellas, tratan un 
documento XML como un árbol que consta de objetos, mientras que los 
objetos representan elementos.

Para el documento XML que se trata aquí, su forma de árbol sería así:

cars_for_sale
|
|____ car
|    |_ id:1
|	 |_ brand: Ford
|	 |_ model: Mustang
|	 |_ production_year: 1972
|	 |_ price(USD): 35900
|
|____ car
	 |_ id:2
	 |_ brand: Aston Martin
	 |_ model: Rapide
	 |_ production_year: 2010
	 |_ price(GPB): 32500
"""

import xml.etree.ElementTree

cars_for_sale = xml.etree.ElementTree.parse("cars.xml").getroot()
print(cars_for_sale.tag)
for car in cars_for_sale.findall("car"):
    print("\t", car.tag)
    for prop in car:
        print("\t\t", prop.tag, end="")
        if prop.tag == "price":
            print(prop.attrib, end="")
        print(" =", prop.text)
