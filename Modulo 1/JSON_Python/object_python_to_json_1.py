"""
Código ejemplo de la clase 1.4.1.2

Convertir un objeto Python a JSON.

Esto se basa en el hecho de sustituir la función que usa dumps() para 
obtener una representación textual de su argumento. Se siguen dos pasos:

1.- Escribe tu propia función sabiendo cómo manejar tus objetos.
2.- Hcer que dumps() lo sepa estableciendo el argumento de palabra clave 
llamado "default".

Notas:
El proceso en el que un objeto almacenado internamente por Python se 
convierte en textual o en cualquier otro aspecto portátil se denomina 
"serialización".

Es obligatorio el verificar y lanzar la excepción TypeError en caso que el
objeto no sea serializable.

Nota propia:
Realicé algunos cambis en el código por mismo para corregir algún error en el 
ejercicio o para ajustar el mismo a las normativas PEP del linter de Python.
"""

import json


class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def encode_who(w):
    if isinstance(w, Who):
        return w.__dict__
    raise TypeError(w.__class__.__name__ + " is not JSON serializable")


some_man = Who("John Doe", 42)
print(json.dumps(some_man, default=encode_who))
