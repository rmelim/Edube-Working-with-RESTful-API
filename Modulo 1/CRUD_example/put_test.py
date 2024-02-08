"""
Código ejemplo de la clase 1.7.1.11

Ejemplos de actualización a través del método HTTP PUT.

Se procede a actualizar un elemento en el archivo cars.json, que se
suministra por un servidor json-server, a través del uso de la función
put() del objeto Response (reply). Actualizar un elemento es, en realidad,
similar a agregar uno. 

Luego se imprime todos los elementos en el terminal.

Nota propia:
Realicé algunos cambis en el código por mismo para corregir algún error en el 
ejercicio o para ajustar el mismo a las normativas PEP del linter de Python.
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

# Estos son los nuevos datos para el elemento con id igual a 6.
#
# Se actualiza el año de producción (cambia a 1967 en lugar de 1957).
car = {
    "id": 6,
    "brand": "Mercedes Benz",
    "model": "300SL",
    "production_year": 1967,
    "convertible": True,
}

# Los convertiremos en JSON antes de enviarlos al servidor.
h_data = json.dumps(car)

# Invocamos la función put(). Se crea un URI que indique claramente el
# elemento que se está modificando. Además, se debe enviar el artículo
# completo, no solo la propiedad cambiada.
try:
    reply = requests.put("http://localhost:3000/cars/6", headers=h_content, data=h_data)
    print("res=" + str(reply.status_code))
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
