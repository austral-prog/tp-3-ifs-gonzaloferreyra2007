def positive():
    """
    Ejercicio 1 - Clasificar Número

    Leer un número entero mediante input(). Determinar si es positivo, negativo o cero
    e imprimir el resultado correspondiente.

    Ejemplo:
        Para la entrada "5", la salida esperada es:
        El numero es positivo

        Para la entrada "-3", la salida esperada es:
        El numero es negativo

        Para la entrada "0", la salida esperada es:
        El numero es cero
    """
    pass
    numero_1 = int(input("Ingrese un numero: "))
    numero_2 = int(input("Ingrese un numero: "))
    numero_3 = int(input("Ingrese un numero: "))

    if numero_1 > 0:
        print("El numero es positivo")
    if numero_2 < 0:
        print("El numero es negativo")
    if numero_3 == 0:
        print("El numero es cero")
#positive()
