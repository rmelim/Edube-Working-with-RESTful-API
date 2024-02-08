"""
Código ejemplo de la clase 1.7.1.8

Ejemplos de lectura a través del método HTTP GET.

De forma predeterminada, un servidor que implementa la versión 1.1 de 
HTTP funciona de la siguiente manera:

1 - Espera la conexión del cliente.
2 - Lee la solicitud del cliente.
3 - Envía su respuesta.
4 - Mantiene viva la conexión esperando de la próxima solicitud del 
cliente.
5 - Si el cliente está inactivo durante algún tiempo, el servidor cierra
silenciosamente la conexión. Esto significa que el cliente está obligado
a volver a establecer una nueva conexión si desea enviar otra solicitud.

El servidor informa al cliente si la conexión se mantiene o no mediante 
un campo denominado "Connection". Este se encuentra en el encabezado de
la respuesta.

Connection=keep-alive
Significa que el servidor mantiene la conección activa a la espera de 
otra solicitud del cliente.

Connection=close
Significa que el servidor va a cerrar la conexión tan pronto como la 
respuesta se transmita por completo. En el servidor HTTP 1.0, este era
el comportamiento predeterminado.

Si el cliente sabe que no usará al servidor con solicitudes posteriores
durante algún tiempo, puede alentar al servidor a cambiar temporalmente 
sus hábitos y cerrar la conexión de inmediato, conservando los recursos 
del servidor. Para lograrlo, se de enviar {"Connection": "Close"} como 
argumento al parámetro headers del método get() de requests. En este 
código en particular, no se empleará este método.
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
    reply = requests.get("http://localhost:3000/cars")
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
