"""
Código ejemplo de la clase 1.7.1.3

Ejemplos de lectura a través del método HTTP GET.

Aquí se procede a analizar el contenido del campo "Content-Type" de la 
propiedad headers que devuelve el objeto Response del servidor.

Esto es para garantizar que si se está recibiendo contenido json y no 
cualquier otro tipo de contenido ( texto, imagen, vídeo, sonido, etc).

El módulo requests analiza el valor del campo Content-Type y, si su valor
anuncia JSON, un método denominado json() devuelve la cadena que contiene 
el mensaje recibido.
"""

import requests

try:
    reply = requests.get("http://localhost:3000/cars")
except:
    print("Communication error")
else:
    if reply.status_code == requests.codes.ok:
        print(reply.headers["Content-Type"])  # Imprime el tipo de contenido.
        print(reply.json())  # Imprimimos el texto devuelto.
    else:
        print("Server error")
