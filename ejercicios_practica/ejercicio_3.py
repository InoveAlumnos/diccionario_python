
# CODE:57
# IMPORTANTE: NO borrar los comentarios

# La función consultar_stock recibe
# por parámetro el stock de materiales existente
def consultar_stock(stock):
    print('Ejercicios con diccionarios')
    # Deberá consultar al usuario por "input"
    # de que material desea obtener el stock
    
    # El usuario ingresará un texto (ej: tornillos)
    # y usted deberá utilizar un condicional y el operdor "in"
    # para verificar si ese material está dentro del stock

    # Si el material está dentro del stock, se debe
    # retornar la cantidad de stock almacenado en
    # el diccionario para esa key

    # Si el material no está dentro dle stock, se debe
    # retornar 0

    # Comenzar aquí, recuerde el identado dentro de esta funcion


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    # Comenzamos con un diccioario creado de stock
    # de materiales:    
    stock = {'tornillos': 100, 'tuercas': 150, 'arandelas': 300}

    consultar_stock(stock)
