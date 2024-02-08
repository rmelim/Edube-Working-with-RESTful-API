"""
Código ejemplo de la clase 1.7.1.2

Ejemplos de lectura a través del método HTTP GET.

Se procede a leer el contenido del archivo cars.json, sumunistrado por 
un servidor json-server, y luego la impresión en el terminal del mismo
a través de la propiedad text del objeto Response (reply).
"""

import requests

try:
    reply = requests.get("http://localhost:3000/cars")
except requests.RequestException:
    print("Communication error")
else:
    if reply.status_code == requests.codes.ok:
        print(reply.text)
    else:
        print("Server error")
