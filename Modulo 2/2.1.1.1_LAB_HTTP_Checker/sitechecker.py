"""
sitechecker.py -- Creado por Rui Durte dos Santos Melim

Escenario:
Herramienta CLI (interfaz de línea de comandos) simple que se pueda usar
para diagnosticar el estado actual de un servidor http en particular. La
herramienta debe aceptar uno o dos argumentos de la línea de comandos:

1.- (obligatorio) la dirección (IP o nombre de dominio calificado) del 
servidor a diagnosticar (el diagnóstico será extremadamente simple, solo 
queremos saber si el servidor está muerto o vivo).
2.- (opcional) el número de puerto del servidor (cualquier ausencia del 
argumento significa que la herramienta debe usar el puerto 80).
3.- Usa el método HEAD en lugar de GET. Obliga al servidor a enviar el 
encabezado de respuesta completo pero sin ningún contenido. Basta con 
comprobar si el servidor funciona correctamente.

También asumimos que:
1.- La herramienta comprueba si se invoca correctamente y, cuando la 
invocación carece de argumentos, imprime un mensaje de error y devuelve
un código de salida igual a 1.
2.- Si hay dos argumentos en la línea de invocación y el segundo no es un
número entero en el rango 1..65535, la herramienta imprime un mensaje de 
error y devuelve un código de salida igual a 2.
3.- Si la herramienta experimenta un tiempo de espera durante la conexión, 
se imprime un mensaje de error y se devuelve 3 como código de salida.
4.- Si la conexión falla por cualquier otro motivo, aparece un mensaje de 
error y se devuelve 4 como código de salida.
5.- Si la conexión se realiza correctamente, se imprime la primera línea
de la respuesta del servidor.

Consejos:
1.- Para acceder a los argumentos de la línea de comandos, se utiliza la 
variable argv del módulo sys, en donde su longitud es siempre uno más 
que el número real de argumentos, ya que argv[0] almacena el nombre de 
su script. Esto significa que el primer argumento está en argv[1] y el 
segundo en argv[2]. Los argumentos de la línea de comandos son siempre 
cadenas. 
2.- La devolución de un código de salida igual a n se logra invocando la 
función exit(n).
"""

import sys
import socket

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

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(5)
        sock.connect((site, port))
        sock.send(
            b"HEAD / HTTP/1.1\r\nHost: "
            + bytes(site, "utf8")
            + b"\r\nConnection: close\r\n\r\n"
        )
        reply = sock.recv(128).decode("utf8")
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
except socket.timeout:
    print(f"Timeout error: {site} took too long to respond.")
    sys.exit(3)
except socket.error as err:
    print(f"Exception error: connection failed or {site} not exist.")
    sys.exit(4)
else:
    print(reply[: reply.find("\n")])
