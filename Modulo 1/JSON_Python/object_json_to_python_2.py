"""
Código ejemplo de la clase 1.4.1.5

Convertir un objeto JSON a Python.

Este enfoque está basado en la redefinición de la clase JSONDecoder. No 
necesitamos reescribir ningún método, pero sí tenemos que redefinir el 
constructor de superclases, lo que hace que el código sea un poco más 
minucioso. El nuevo constructor está destinado a hacer un solo truco: 
establecer una función para la creación de objetos.

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
        return super().default(o)


class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_who)

    def decode_who(self, d):
        return Who(**d)


some_man = Who("Jane Doe", 23)
json_str = json.dumps(some_man, cls=MyEncoder)
new_man = json.loads(json_str, cls=MyDecoder)

print(type(new_man))
print(new_man.__dict__)
