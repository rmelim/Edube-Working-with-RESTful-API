"""
Código ejemplo de la clase 1.7.1.6

Ejemplos de lectura a través del método HTTP GET.

Algunos servidoresw pueden proporcionar algunas facilidades adicionales, 
por ejemplo, puede manipular datos antes de enviarlos al cliente. 

El json-server, entre esa facilidades, es capaz de ordenar los elementos 
utilizando cualquiera de las propiedades como clave de ordenación. De 
forma predeterminada, ordena los elementos por sus identificadores, pero 
por lo general, el URI hace el truco. Hay que recordar que no existe un 
estándar común que cubra estas funciones adicionales. Siempre se consulta
la documentación del servidor para obtener más información al respècto.

El json-server, supone que un URI se formó de la siguiente manera:
http://server:port/resource?_sort=prop. Esto ocasiona que el objeto
Response se ordene en orden ascendente mediante la propiedad "prop".
Se debe tener en cuenta el carácter "?" separa la identificación del
recurso de los parámetros de solicitud adicionales.
"""

import requests

key_names = ["id", "brand", "model", "production_year", "convertible"]
key_widths = [10, 15, 10, 20, 15]


def show_head():
    for n, w in zip(key_names, key_widths):
        print(n.ljust(w), end="| ")
    print()


def show_empty():
    for w in key_widths:
        print(" ".ljust(w), end="| ")
    print()


def show_car(car):
    for n, w in zip(key_names, key_widths):
        print(str(car[n]).ljust(w), end="| ")
    print()


def show(json):
    show_head()
    if type(json) is list:
        for car in json:
            show_car(car)
    elif type(json) is dict:
        if json:
            show_car(json)
        else:
            show_empty()


try:
    reply = requests.get("http://localhost:3000/cars?_sort=production_year")
except requests.RequestException:
    print("Communication error")
else:
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print("Server error")
