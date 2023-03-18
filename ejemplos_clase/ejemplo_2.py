# Diccionarios [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.2


def operador_in():
    print("Ejemplo: operador_in")
    # El operador "in" (en) devuelve True si
    # un elemento se encuentra dentro de otro

    # En diccionarios nos indica si existe
    # una clave (key) definido en su interior

    # En este diccionario almacenaremos
    # cuantos productos hay en stock
    stock_productos = {"monitor": 6, "teclado": 3, "mouse": 54}

    if "monitor" in stock_productos:
        print("En mi stock hay monitores")

    if "bicicleta" in stock_productos:
        print("En mi stock hay bicicletas")

    if "bicicleta" not in stock_productos:
        print("En mi stock NO hay bicicletas")


def sumar_stock():
    print("Ejemplo: sumar_stock")
    # En este diccionario almacenaremos
    # cuantos productos hay en stock
    stock_productos = {"monitor": 6, "teclado": 3, "mouse": 54}

    # Utilizando el operador "in" podremos
    # obtener la cantidad de productos hay
    # en stock por cada categoria

    # Basada en la siguiente listas de posibles
    # productos
    lista_productos = ["teclado", "remeras", "monitor"]

    # Sumar la cantidad de productos en stock total
    # de toda la lista de productos
    # utilizando el operador in para evitar solicitar
    # el stock de un producto que no existe

    suma_total = 0
    for producto in lista_productos:
        if producto in stock_productos:
            # Cómo el producto existe entre las
            # keys de stock_productos
            # Accedemos al dato y lo sumamos
            # a suma total
            cantidad = stock_productos[producto]
            suma_total += cantidad
        else:
            print("En mi stock NO hay", producto)

    print("Suma total:", suma_total)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    operador_in()
    sumar_stock()
