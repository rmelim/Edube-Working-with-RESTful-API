"""
Código ejemplo de la clase 1.7.1.5

Ejemplos de lectura a través del método HTTP GET.

Si no se necesita todo el contenido de un recurso, puede preparar una 
solicitud específica que requiera solo un elemento y use id como clave. 
El URI tendrá el siguiente aspecto: http://server:port/resource/id
"""


import requests

key_names = ["id", "brand", "model", "production_year", "convertible"]
key_widths = [10, 15, 10, 20, 15]


def show_head():
    """
    Función para imprimir el encabezado de la tabla.

    Se itera a través de key_names y key_widths acoplados por la
    función zip() y se imprime el nombre de cada clave expandido a
    la longitud deseada y se coloca una barra al final.
    """
    for n, w in zip(key_names, key_widths):
        print(n.ljust(w), end="| ")
    print()


def show_empty():
    """
    Función que imprime una línea vacia.
    """
    for w in key_widths:
        print(" ".ljust(w), end="| ")
    print()


def show_car(car):
    """
    Función para imprimir una línea llena con los datos de cada carro.

    Argumentos:
        car -- Diccionario que contienen los datos de cada carro.
    """
    for n, w in zip(key_names, key_widths):
        print(str(car[n]).ljust(w), end="| ")
    print()


def show(json):
    """
    Función para imprimir el contenido del mensaje JSON como una lista
    de elementos pero que esta preparada para el hecho de que el servidor
    envie sólo un elemento cuando se le solicite..

    Arguments:
        json -- Objeto que contiene un mensaje JSON.
    """
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
    reply = requests.get("http://localhost:3000/cars/5")
except requests.RequestException:
    print("Communication error")
else:
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    # Si no hay ningún elemento del id solicitado, el servidor
    # establecerá el código de estado en 404 ("not found").
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print("Server error")
