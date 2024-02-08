"""
cars.py -- Creado por Rui Duarte dos Santos Melim.

Escenario:
Implementar una solución de software que gestione una pequeña base de 
datos que reúna datos sobre coches antiguos. 

* Utilizar las herramientas del módulo requests.
* Crear grandes soluciones de software utilizando las tácticas arriba 
hacia abajo.
* Cooperar con una base de datos remota mediante REST.

Nota Importante:
Se requiere de la instalación de un servidor local de Node.js y del 
npm llamado json-server. Se debe iniciar el Servidor JSON de Node.js. 
Ejecutar desde el terminal de comandos: json-server -w cars.json
"""

import json
import sys
import requests

URL_SERVER = "http://localhost:3000/cars"
CARS_HEADERS = ["id", "brand", "model", "production_year", "convertible"]
CARS_WIDTHS = [6, 13, 13, 17, 12]


def check_server(cid=None):
    """
    Verifica el estado del servidor. Devuelve True o False.

    Cuando se invoca sin argumentos, sólo verifica sei el
    servido responde.

    Invocado con el Id, comprueba si este Id está presente
    en la Base de Datos.

    Keyword Arguments:
        cid -- Id del vehículo (default: {None})

    Returns:
        True: Respuesta afirmativa del servidor o Id presente.
    """
    try:
        if cid is None:
            reply = requests.head(URL_SERVER, headers={"Conection": "Close"}, timeout=1)
        else:
            reply = requests.get(f"{URL_SERVER}/{cid}", timeout=1)
        return reply.status_code == requests.codes.ok
    except requests.exceptions.RequestException:
        return False


def print_menu():
    """
    Imprime el Menú Principal.
    """
    print("+" + ("-" * 31) + "+")
    print("|" + "Vintage Cars Database".center(31) + "|")
    print("+" + ("-" * 31) + "+")
    print("M E N U")
    print("=" * 7)
    print("1. List cars")
    print("2. Add new car")
    print("3. Delete car")
    print("4. Update car")
    print("0. Exit")


def read_user_choice():
    """
    Lee la elección de opción del usuario y verifica si es válida.

    Returns:
        Un string con la opción seleccionada: '0', '1', '2', '3' or '4'
    """
    while True:
        choice_ = input("Enter your choice (0..4): ")
        if choice_ not in ["0", "1", "2", "3", "4"]:
            print("Invalid choice. Try again...")
            continue
        return choice_


def print_header():
    """
    Imprime un encabezado elegante para la tabla de vehiculos.
    """
    print("-" * sum(CARS_WIDTHS))
    for name, width in zip(CARS_HEADERS, CARS_WIDTHS):
        print(name.replace("_", " ").title().center(width), end="")
    print()
    print("-" * sum(CARS_WIDTHS))


def print_car(car):
    """
    Imprime los datos de los vehículos de manera que se ajuste al
    encabezado.

    Arguments:
        car -- diccionario con los datos de los vehículos.
    """
    cars = [str(value) for value in car.values()]
    for name, width in zip(cars, CARS_WIDTHS):
        print(name.ljust(width), end="")
    print()


def list_cars():
    """
    Obtiene todos los vehículoo y sus datos desde el servidor y los
    imprime.

    Si la Base de Datos está vacía, en vez imprime un mensaje para
    indicar esto.
    """
    reply = requests.get(URL_SERVER, timeout=1)
    car_json = reply.json()
    if not car_json:
        print("*** Database is empty ***")
    else:
        print_header()
        for car in car_json:
            print_car(car)


def name_is_valid(name):
    """
    Revisa si el nombre del modelo o marca dado por el usuario es valido.

    Un nombre válido no debe ser un string vacía y sólo debe contener
    letras, números y espacios.

    Arguments:
        name -- string con el nombre del modelo o marca.

    Returns:
        True si el nombre es válido.
    """
    if name.strip() == "":
        return False
    return name.isalnum()


def enter_id():
    """
    Permite al usuario dar entrada al Id del vehículo y verificar si es
    válido.

    Un Id válido consiste de sólo dígitos numéricos.

    Returns:
        integer con el Id del vehículo.
    """
    while True:
        id_ = input("Car ID (empty string to exit): ")
        if id_.strip() == "":
            return None
        if not id_.isdigit():
            print("An integer is required for the Id. Please try again.")
            continue
        return int(id_)


def enter_name(what):
    """
    Perimite al usuario dar entrada al nombre de marca o modelo del
    vehículo y verificar su validez a través de la función name_is_valid().

    Arguments:
        what -- determina si el nombre a entrar es la marca ("brand") o
        el modelo.

    Returns:
        Un string con el nombre entrado o None si se dejó en blanco.
    """
    if what == "brand":
        while True:
            if (brand_ := input("Car brand (empty string to exit): ").strip()) == "":
                return None
            if name_is_valid(brand_):
                return brand_.capitalize()
            print("The brand name is not valid. Please try again.")
    else:
        while True:
            if (model_ := input("Car model (empty string to exit): ").strip()) == "":
                return None
            if name_is_valid(model_):
                return model_.capitalize()
            print("The model name is not valid. Please try again.")


def enter_production_year():
    """
    Perimite al usuario dar entrada al año de producción del vehículo y
    revisar que el valor sea válido.

    Un valor válido debe constar de un año en un integer entre los rangos
    1900 al 2000

    Returns:
        Un integer con el año entrado o None si se dejó vacío.
    """
    while True:
        if (year_ := input("Production year (empty string to exit): ").strip()) == "":
            return None
        if not year_.isdigit():
            print("Not digit")
            continue
        year_ = int(year_)
        if year_ not in range(1900, 2001):
            print("Invalid range for year. Range must be between 1900 and 2000")
            continue
        return year_


def enter_convertible():
    """
    Permite al usuario dar entrada a si el vehículo es convertible o no.

    Returns:
        True, si el vehículo es convertible.
    """
    while True:
        if (
            convertible_ := input(
                "Is this car convertible? [y/n] (empty string to exit): "
            ).strip()
        ) == "":
            return None
        if convertible_.lower() not in ("y", "n"):
            print("Yes o no.")
            continue
        return convertible_.lower() == "y"


def input_car_data(with_id):
    """
    Permite al usuario dar entrada a los datos del vahículo.

    Arguments:
        with_id -- Si es True, se da entrada al Id del vehívculo.

    Returns:
        None si se canceló la operación. De lo contrario, se devuelve
        un diccionario con la estructura siguiente:
        {
            'id': int,
            'brand': str,
            'model': str,
            'production_year': int,
            'convertible': bool
        }
    """
    if with_id:
        id_ = enter_id()
        if id_ is None:
            return None
    else:
        id_ = 0
    brand_ = enter_name("brand")
    if brand_ is None:
        return None
    model_ = enter_name("model")
    if model_ is None:
        return None
    year_ = enter_production_year()
    if year_ is None:
        return None
    convertible_ = enter_convertible()
    if convertible_ is None:
        return None
    return dict(zip(CARS_HEADERS, [id_, brand_, model_, year_, convertible_]))


def add_car():
    """
    Invoca la función input_car_data(True) para obtener la información
    del vehículo y añadirlo a la Base de Datos.
    """
    if (car := input_car_data(True)) is not None:
        if check_server(str(car["id"])):
            print("Id exist")
        else:
            try:
                reply = requests.post(
                    URL_SERVER,
                    headers={"Content-Type": "application/json"},
                    data=json.dumps(car),
                    timeout=1,
                )
                if reply.status_code != requests.codes.created:
                    print("Existing Id. The new car was not created.")
            except requests.exceptions.RequestException:
                print("Communication error. Creation failed.")


def update_car():
    """
    Invoca la función enter_id() paar obtener el Id del vehículo y saber
    si está presente en la Base de Datos.

    Invoca la función input_car_data(False) para obtener la información
    del vehículo y actualizarla en la Base de Datos.
    """
    while True:
        id_ = enter_id()
        if id_ is not None:
            if not check_server(id_):
                print("The Id does not exist. Please try again.")
                continue
            if (car := input_car_data(False)) is not None:
                car["id"] = id_
                try:
                    reply = requests.put(
                        f"{URL_SERVER}/{id_}",
                        headers={"Content-Type": "application/json"},
                        data=json.dumps(car),
                        timeout=1,
                    )
                    if reply.status_code != requests.codes.ok:
                        pass
                except requests.exceptions.RequestException:
                    print("Communication error. The update has failed.")
        break


def delete_car():
    """
    Solicita al usuario el Id del vehículo e intenta eliminarlo de la
    Base de Datos.
    """
    while True:
        id_ = enter_id()
        if id_ is not None:
            if not check_server(id_):
                print("The Id does not exist. Please try again.")
                continue
            try:
                reply = requests.delete(f"{URL_SERVER}/{id_}", timeout=1)
                if reply.status_code != requests.codes.ok:
                    pass
            except requests.RequestException:
                print("Communication error. The delete has failed.")
        break


while True:
    if not check_server():
        print("Server is not responding - quitting!")
        sys.exit(1)
    print_menu()
    choice = read_user_choice()
    if choice == "0":
        print("Bye!")
        sys.exit(0)
    elif choice == "1":
        list_cars()
    elif choice == "2":
        add_car()
    elif choice == "3":
        delete_car()
    elif choice == "4":
        update_car()
