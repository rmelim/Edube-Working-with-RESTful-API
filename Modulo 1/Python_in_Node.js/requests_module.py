"""
Código ejemplo de las clases 1.6.1.5 a la .8

Diferentes ejemplos con el módulo requests.
"""

import requests

# Si la conexión es exitosa, se devuelve un objeto Response que contiene
# toda la información que describe la ejecución del método GET.
#
# Como no se indica ningún puerto, éste utiliza el puerto por defecto
# para HTTP, el cual es igual a 80.
reply = requests.get("http://localhost:3000")

# Imprime el contenido de la propiedad status_code del objeto Response
# (reply). Si el resultado es 200, significa que la conexión está OK.
print("\nPropiedad reply.status_code:")
print(reply.status_code)

# El módulo requests ofrece muchas formas diferentes de especificar y
# reconocer códigos de estado. Una de ellas es con el contenido de un
# diccionario de estado de la propiedad codes. Pero el resultado es muy
# largo y confuso.
print("\nPropiedad requests.codes.__dict__:")
print(requests.codes.__dict__)

# También se puede usar la propiedad codes para probar los códigos
# de estado de una manera más detallada que comparándolos con valores
# enteros simples.
if reply.status_code == requests.codes.ok:
    print("\nPropiedad requests.codes.ok:")
    print("Conection OK")

# Cuando la respuesta del servidor es correcta, consta de dos partes:
# el encabezado y el contenido.
#
# El encabezado de la respuesta se almacena dentro de la propiedad del
# objeto Response (reply) denominada headers (es un diccionario).
print("\nPropiedad reply.headers:")
print(reply.headers)

# El contenido de la respuesta sin procesar se almacena mediante la
# propiedad text.
print("\nPropiedad reply.text:")
print(reply.text)
