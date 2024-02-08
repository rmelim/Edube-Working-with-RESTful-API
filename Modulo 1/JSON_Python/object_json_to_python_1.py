"""
Código ejemplo de la clase 1.4.1.4

Convertir un objeto JSON a Python.

Esto se puede realizar a través del método loads() el cual convierte una
cadena JSON en el tipo de dato adecuado de Python (integr, float, string,
list, dict). Pero cuando se trata de deserializar un objeto Python, se
requiere de algunos pasos adicionales.

Como loads() no es capaz de adivinar qué objeto (de qué clase) necesita
realmente deserializar, se debe proporcionar esta información.

Hay un nombre de argumento de palabra clave "object_hook", que se usa 
para apuntar a la función responsable de crear un nuevo objeto de una 
clase necesaria y llenarlo con datos reales. 

Notas: 
En este código, la función decode_who() recibe un diccionario de Python.
Como el constructor espera dos valores (una cadena y un número) y no 
un diccionario, hay que usar un pequeño truco. Se emplea el operador 
double * para convertir el directorio en una lista de argumentos de 
palabras clave construidos a partir de los pares key:value del diccionario.
Por supuesto, las claves del diccionario deben tener los mismos nombres que
los parámetros del constructor de Who().

la función, especificada por "object_hook" se invocará solo cuando la cadena 
JSON describa un objeto JSON. No hay excepciones a esta regla.

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
    raise TypeError(w.__class__.__name__ + "is not JSON serializable")


def decode_who(w):
    # regresa Who(w["name"], w["age"])
    return Who(**w)


old_man = Who("Jane Doe", 23)
json_str = json.dumps(old_man, default=encode_who)
new_man = json.loads(json_str, object_hook=decode_who)
print(type(new_man))
print(new_man.__dict__)
