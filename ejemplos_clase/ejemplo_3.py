# Diccionarios [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.2


def bucles_y_diccionario():
    print("Ejemplo: bucles_y_diccionario")
    # Crear un diccionario de inquilinos del primero piso
    piso_1 = {'a': 'Gutierrez', 'b': 'Naon', 'c': 'Palermo'}

    # Crear un diccionario de inquilinos del segundo piso
    piso_2 = {}  # Diccionario vacio del segundo piso
    piso_2['a'] = 'Tucuman'  # 2a
    piso_2['b'] = 'Mendoza'  # 2b
    piso_2['c'] = 'Cordoba'  # 2c

    # Imprimir los diccionarios
    print(piso_1)
    print(piso_2)

    # En que departamento del segundo piso vive Cordoba
    # Realizar un bucle de diccionarios
    # k --> key
    # v --> value
    for k,v in piso_2.items():
        if v == "Cordoba":
            print(v, "se encuentra en el departamento", k)

    print("terminamos")


def listas_y_diccionario():
    print("Ejemplo: listas_y_diccionario")
    # Crear un diccionario de inquilinos del primero piso
    piso_1 = {'a': 'Gutierrez', 'b': 'Naon', 'c': 'Palermo'}

    # Crear un diccionario de inquilinos del segundo piso
    piso_2 = {}  # Diccionario vacio del segundo piso
    piso_2['a'] = 'Tucuman'  # 2a
    piso_2['b'] = 'Mendoza'  # 2b
    piso_2['c'] = 'Cordoba'  # 2c

    # Armemos ahora el edificio de 2 pisos, 
    # el cual es una lista de diccionarios
    edificio = []
    edificio.append(piso_1)
    edificio.append(piso_2)

    # Imprimir la lista de diccionarios
    print(edificio)

    # Imprimir las familias que viven
    # en cada departamento "a"
    for i in range(len(edificio)):
        print(f"Piso {i+1} depto a:", edificio[i]["a"])


    # Recorrer todo el edificio en búsqueda de la familia Tucuman:
    for i in range(len(edificio)):  # --> recorre los pisos
        piso = edificio[i]
        for k,v in piso.items():    # --> recorre los departamentos
            if v == "Tucuman":
                print(v, "se encuentra en el piso", i, "departamento", k)

    print("terminamos")


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    bucles_y_diccionario()
    listas_y_diccionario()
