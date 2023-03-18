# Diccionarios [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.2


def exepciones_numeros():
    print("Ejemplo: exepciones_numeros")
    # Una excepcion ocurre cuando el sistema falla
    # de tal forma que Python no puede contener la falla.
    # Esto produce que el programa deba detenerse sin poder continuar
    # con su ejecución.

    # Veamos una falla tipica matemática, la division por cero:
    # Al intentar dividir un número por cero el sistema no puede
    # ejecutar la división.
    try:
        division = 3 / 0
    except:
        print('No existe la division por cero')

    print("terminamos")


def exepciones_diccionarios():
    print("Ejemplo: exepciones_diccionarios")
    # Una excepcion ocurre cuando el sistema falla
    # de tal forma que Python no puede contener la falla.
    # Esto produce que el programa deba detenerse sin poder continuar
    # con su ejecución.

    # Veamos que sucede cuando intentamos acceder a un dato
    # de un diccionario que no existe (no existe la calve)
    # Al intentar acceder al dato sistema no puede
    # completar la acción.
    stock_productos = {"monitor": 6, "teclado": 3, "mouse": 54}
    try:
        cantidad = stock_productos["bicicleta"]
    except:
        print("En mi stock NO hay bicicletas")

    # Es por eso que es importante utilizar el
    # el operador "in" para verificar que la clave (key)
    # existe en el diccionario
    print("terminamos")


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    exepciones_numeros()
    exepciones_diccionarios()
