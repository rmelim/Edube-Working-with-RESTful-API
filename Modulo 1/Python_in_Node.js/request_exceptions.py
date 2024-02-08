"""
Código ejemplo de las clases 1.6.1.9 a la .10

Ejemplos de excepciones con el módulo requests.

A continuación está reunidas todas las excepciones de solicitudes
presentada como un árbol:

RequestException
|___HTTPError
|___ConnectionError
|   |___ProxyError	
|   |___SSLError	
|___Timeout
|   |___ConnectTimeout
|   |___ReadTimeout
|___URLRequired
|___TooManyRedirects
|___MissingSchema
|___InvalidSchema
|___InvalidURL
|   |___InvalidProxyURL
|___InvalidHeader
|___ChunkedEncodingError
|___ContentDecodingError
|___StreamConsumedError
|___RetryError
|___UnrewindableBodyError
"""

import requests

# La función get() toma un argumento adicional llamado timeout.
# Es el tiempo máximo medido en segundos y expresado como un número real
# que acordamos esperar la respuesta de un servidor.
#
# Si se excede el tiempo, se generará una excepción denominada:
# requests.exceptions.Timeout
try:
    reply = requests.get("http://localhost:3000", timeout=1)
except requests.exceptions.Timeout:
    print("Sorry, Mr. Impatient, you didn't get your data")
else:
    print("Here is your data, my Master!")

# En este ejemplo, el código no tiene ninguna posibilidad de ejecutarse
# correctamente, ya que está dirigiendo sus esfuerzos al puerto 3001,
# mientras que nuestro servidor está escuchando en el puerto 3000.
#
# El cliente y el servidor no se encontrarán y se planteará la excepción:
# requests.exceptions.ConnectionError
try:
    reply = requests.get("http://localhost:3001", timeout=1)
except requests.exceptions.ConnectionError:
    print("Nobody's home, sorry!")
else:
    print("Everything fine!")

# También es posible que el desarrollador deje el URI del recurso en un
# estado algo mal formado.
#
# Esto es atendido por una excepción denominada:
# requests.exceptions.InvalidURL
try:
    reply = requests.get("http:////////////")
except requests.exceptions.InvalidURL:
    print("Recipient unknown!")
else:
    print("Everything fine!")
