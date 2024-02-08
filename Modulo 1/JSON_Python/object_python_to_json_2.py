"""
Código ejemplo de la clase 1.4.1.3

Convertir un objeto Python a JSON. 

Este enfoque se basa en el hecho de que la serialización se realiza 
realmente mediante el método denominado default(), que forma parte de 
la clase json.JSONEncoder. Esto le da la oportunidad de sobrecargar el
método definiendo una subclase de JSONEncoder y pasarlo adentro de 
dumps() usando el argumento de palabra clave "cls".

En este enfoque no es obligatorio verificar y lanzar Excepciones.

Nota propia:
Realicé algunos cambis en el código por mismo para corregir algún error en el 
ejercicio o para ajustar el mismo a las normativas PEP del linter de Python.
"""

import json


class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class MyEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Who):
            return o.__dict__
        return super().default(self)


some_man = Who("John Doe", 42)
print(json.dumps(some_man, cls=MyEncoder))
