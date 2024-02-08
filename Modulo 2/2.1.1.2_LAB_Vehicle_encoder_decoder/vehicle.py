"""
vehicle.py -- Creado por Rui Duarte dos Santos Melim.

Escenario:
Las imágenes vechicle_example_1.jpg y vechicle_example_2.jpg presentan
dos casos de uso diferentes de este programa.

El código tiene exactamente la misma conversación con el usuario y cumple
con los siguientes puntos:

1.- Define una clase llamada Vehicle, cuyos objetos pueden transportar
los datos del vehículo que se muestran en la imagen (la estructura de 
la clase se deduce del cuadro de diálogo de la imagen).
2.- Define una clase capaz de codificar el objeto Vehicle en una cadena 
JSON equivalente.
3.- Define una clase capaz de descodificar la cadena JSON en el objeto 
Vehicle recién creado.

También se realizan algunas comprobaciones básicas de validez de datos,
para asegurar la protección del código de usuarios imprudentes.
"""

import json


class Vehicle:
    def __init__(self, registration_number, year_of_production, passenger, mass):
        self.registration_number = registration_number
        self.year_of_production = year_of_production
        self.passenger = passenger
        self.mass = mass


class EncoderVehicle(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Vehicle):
            return o.__dict__
        return super().default(self)


class DecoderVehicle(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_vehicle)

    def decode_vehicle(self, d):
        return Vehicle(**d)


def validate_choice():
    while True:
        choice_ = input("Your choice: ")
        if choice_ in ("1", "2"):
            return choice_
        print("Invalid choice. To choose 1 or 2.")


def validate_number():
    while True:
        number_ = input("Registration number: ").upper()
        if number_ != "":
            return number_
        print("You must enter a valid registration number.")


def validate_year():
    while True:
        year_ = input("Year of production: ")
        try:
            year_ = int(year_)
            if year_ < 1900:
                raise ValueError
            return year_
        except ValueError:
            print("A number representing a valid year is expected.")
            print("Must be between the year 1900 and the current year.")


def validate_passenger():
    while True:
        passenger_ = input("Passenger [y/n]: ").lower()
        if passenger_ in ("y", "n"):
            return passenger_ == "y"
        print("Either 'y' or 'n' is expected in response.")


def validate_mass():
    while True:
        mass_ = input("Vehicle mass: ")
        try:
            mass_ = float(mass_)
            if mass_ <= 0:
                raise ValueError
            return mass_
        except ValueError:
            print("A number valid for the mass of the vehicle and")
            print("greater than 0 is expected.")


def validate_json_string():
    while True:
        json_string_ = input("Enter vehicle JSON string: ")
        try:
            result = json.loads(json_string_, cls=DecoderVehicle)
            return result
        except ValueError:
            print("The supplied string is not a valid JSON string.")
        except TypeError:
            print(
                "The JSON string provided does not describe valid data for a vehicle."
            )


print("What can I do for you?")
print("1 - produce a JSON string describing a vehicle")
print("2 - decode a JSON string into vehicle data")

choice = validate_choice()
if choice == "1":
    number = validate_number()
    year = validate_year()
    passenger = validate_passenger()
    mass = validate_mass()

    vehicle = Vehicle(number, year, passenger, mass)
    vehicle_json = json.dumps(vehicle, cls=EncoderVehicle)

    print("Resulting JSON string is:")
    print(vehicle_json)
else:
    json_string = validate_json_string()
    print(json_string.__dict__)
