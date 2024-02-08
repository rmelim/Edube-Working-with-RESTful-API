"""
Código ejemplo de la clase 1.7.1.4

Ejemplos de lectura a través del método HTTP GET.

Código sencillo para presentar las respuestas del servidor de una manera
elegante y clara.
"""

import requests

# Nombre de todos los campos claves en el archivo JSON.
key_names = ["id", "brand", "model", "production_year", "convertible"]
key_widths = [10, 15, 10, 20, 15]  # Ancho que se dará a cada campo.


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
    de elementos.

    Arguments:
        json -- Objeto que contiene un mensaje JSON.
    """
    show_head()
    for car in json:
        show_car(car)


try:
    reply = requests.get("http://localhost:3000/cars")
except requests.RequestException:
    print("Communication error")
else:
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    else:
        print("Server error")
