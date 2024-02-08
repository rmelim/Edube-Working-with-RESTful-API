"""
Código ejemplo de la clase 1.7.1.9

Ejemplos de eliminación a través del método HTTP DELETE.

Se procede a eliminar el elemento con id=1 del archivo cars.json, 
suministrado por un servidor json-server, a través del uso de la
función delete() del objeto Response (reply) y luego la impresión
del resto de elementos en el terminal.

Nota propia:
Realicé algunos cambis en el código por mismo para corregir algún error en el 
ejercicio o para ajustar el mismo a las normativas PEP del linter de Python.
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


headers = {"Connection": "Close"}
try:
    reply = requests.delete("http://localhost:3000/cars/1")
    print("res=" + str(reply.status_code))
    reply = requests.get("http://localhost:3000/cars/", headers=headers)
except requests.RequestException:
    print("Communication error")
else:
    print("Connection=" + reply.headers["Connection"])
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print("Server error")
