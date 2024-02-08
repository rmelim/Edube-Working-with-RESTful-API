"""
serverchecker -- Creado por Rui Duarte dos Santos Melim.

Escenario:
En este código se regresa a los temas tratados en el laboratorio 2.1.1.1
De hecho, implementa exactamente la misma funcionalidad que incrustó en 
su código anteriormente, pero esta vez usa el módulo "requests" en lugar 
del módulo "socket".

Todo lo demás sigu3 igual; los argumentos de la línea de comandos y las 
salidas son indistinguibles.

Sugerencia:
Se usa el método head() en lugar de get(), ya que no necesita todo el 
documento raíz que envía el servidor. El encabezado es suficiente para 
probar si el servidor está respondiendo o no. 

Se manejan todas las excepciones necesarias; no se deja al usuario sin 
explicaciones claras sobre cualquier cosa que haya salido mal.
"""

import sys
import requests

if len(sys.argv) not in [2, 3]:
    print(
        "Improper number of arguments: at least one is required and not more than two are allowed:"
    )
    print("- http server's address (required)")
    print("- port number (default to 80 is not specified)")
    sys.exit(1)
else:
    if len(sys.argv) == 3:
        try:
            port = int(sys.argv[2])
            if port < 1 or port > 65535:
                raise ValueError
        except ValueError:
            print("Port number is invalid - exiting.")
            sys.exit(2)
    else:
        port = 80
    site = sys.argv[1]
    if site[:4] != "http":
        site = ("https://" if port == 443 else "http://") + site

try:
    reply = requests.head(f"{site}:{port}", timeout=1)
except requests.exceptions.InvalidURL:
    print(f"Invalid URL: {site} not exist.")
    sys.exit(3)
except requests.exceptions.ConnectionError:
    print(f"Connection error: connection failed to {site}")
    sys.exit(4)
except requests.exceptions.Timeout:
    print(f"Timeout error: {site} took too long to respond.")
    sys.exit(5)
except requests.exceptions.RequestException:
    print(f"Request exception. Unexpected error when requesting {site}")
    sys.exit(6)
else:
    print(reply.status_code, reply.reason)
