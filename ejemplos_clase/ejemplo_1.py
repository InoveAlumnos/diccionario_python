# Archivos [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.2

import csv


def diccionario():
    print("Ejemplo: diccionario")
    # Crear un diccionario de inquilinos en un piso
    # de un edificio
    piso_2 = {'a': 'Tucuman', 'b': 'Mendoza', 'c': 'Cordoba'}

    # Imprimir los datos del diccionario
    print(piso_2)

    # Ahora crear un diccionario vacio
    # Vamos a crear nuevamente piso_2 y se borrará
    # su información
    piso_2 = {}  # Diccionario vacio del segundo piso

    # Imprimir los datos del diccionario
    print(piso_2)

    # Completar el diccionario nuevo
    piso_2['a'] = 'Tucuman'  # 2a
    piso_2['b'] = 'Mendoza'  # 2b
    piso_2['c'] = 'Cordoba'  # 2c

    # Imprimir los datos del diccionario
    print(piso_2)

    # ¿Quíen vive en el 2b?
    print(piso_2['b'])  # Mendoza

    # Ahora digamos que se mundo "Mendoza"
    # y viene la familia Neuquen en su lugar:
    piso_2['b'] = 'Neuquen'  # 2b

    # ¿Quíen vive ahora en el 2b?
    print(piso_2['b'])  # Neuquen

    # Acceso seguro a los datos
    # ¿Quíen vive en el 1e?
    # ¿Cómo podemos acceder a un valor que no existe
    # y que no explite el programa --> Utilizando "get":
    print(piso_2.get('e'))


def operar():
    print("Ejemplo: operar")
    # Ahora tenemos un diccionario que contiene
    # el listado de precios de productos
    productos = {
        "pizza": 40,
        "hamburguesa": 20,
        "helado": 25,        
        "torta": 60
    }

    # Un cliente compra una pizza y un helado
    # ¿Cuánto ha gasdo el cliente?

    # Podemos obtener el precio de la pizza del diccionario
    precio_pizza = productos["pizza"]
    print("Precio de la pizza:", precio_pizza)

    # Podemos obtener el precio del helado del diccionario
    precio_helado = productos["helado"]
    print("Precio de la helado:", precio_helado)

    # Sumar el total
    gasto_total = precio_pizza + precio_helado
    print("Gasto total:", gasto_total)

    # Podríamos sumar todo accediendo a los datos
    # directamente del diccionario:
    gasto_total = productos["pizza"] + productos["helado"]
    print("Gasto total:", gasto_total)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    diccionario()
    operar()
