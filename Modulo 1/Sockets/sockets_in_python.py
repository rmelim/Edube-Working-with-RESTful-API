"""
Código ejemplo de las clases 1.2.1.5 a la .8

Como crear un socket para HTTP en un dominio INET.
"""

import socket

server_addr = input("What server do you want to connect to? ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_addr, 80))
sock.send(
    b"GET / HTTP/1.1\r\nHost: "
    + bytes(server_addr, "utf8")
    + b"\r\nConnection: close\r\n\r\n"
)
reply = sock.recv(10000)
sock.shutdown(socket.SHUT_RDWR)
sock.close()
print(repr(reply))
