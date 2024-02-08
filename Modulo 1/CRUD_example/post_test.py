"""
Código ejemplo de la clase 1.7.1.10

Ejemplos de creación a través del método HTTP POST.

Se procede a crear un nuevo elemento en el archivo cars.json, 
suministrado por un servidor json-server, a través del uso de la
función post() del objeto Response (reply) y luego la impresión
de los elementos en el terminal.
"""

import json
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


h_close = {"Connection": "Close"}

# Si se envía algo al servidor, el servidor debe ser consciente de lo
# que realmente es. El servidor nos informa sobre el tipo de contenidos
# mediante el campo Content-Type.
#
# Se usa la misma técnica para advertir al servidor que estamos enviando
# algo más que una simple solicitud, preparando el campo Content-Type con
# el valor adecuado.
h_content = {"Content-Type": "application/json"}

# Este es el nuevo carro. Preparamos todos los datos necesarios y los
# empaquetamos dentro de un diccionario de Python.
new_car = {
    "id": 7,
    "brand": "Porsche",
    "model": "911",
    "production_year": 1963,
    "convertible": False,
}

# Los convertiremos en JSON antes de enviarlos al servidor.
h_data = json.dumps(new_car)

# Comprobamos cómo se ve el mensaje JSON resultante.
print(h_data)

# invocamos la función post() (El URI, solo apunta al recurso, no al
# elemento en particular) y establecemos dos parámetros adicionales:
#
# 1.- headers, para complementar el encabezado de la solicitud con el
# campo Content-Type.
# 2.- data, para pasar el mensaje JSON a la solicitud.
try:
    reply = requests.post("http://localhost:3000/cars", headers=h_content, data=h_data)
    print("reply=" + str(reply.status_code))
    reply = requests.get("http://localhost:3000/cars/", headers=h_close)
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
