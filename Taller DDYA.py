def positivo(n):
    if n > 0:
        print(f"{n} es positivo.")
        return 1
    elif n < 0:
        print(f"{n} es negativo.")
        return -1
    else:
        print(f"{n} es cero.")
        return 0


def fibonacci(n):
    fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    if n in fib:
        print(f"{n} pertenece a la serie de Fibonacci.")
    else:
        print(f"{n} no pertenece a la serie de Fibonacci.")


def primo(n):

    if n <= 1:
        print(f"{n} no es primo.")
        return

    divisores = 0

    for i in range(1, n + 1):
        if n % i == 0:
            divisores += 1

    if divisores == 2:
        print(f"{n} es primo.")
    else:
        print(f"{n} no es primo.")


def analizar_numero(n):

    estado = positivo(n)
    fibonacci(n)
    primo(n)

    return estado


def suma_dig(a, b):

    if a < b:
        menor = a
        mayor = b
    else:
        menor = b
        mayor = a

    suma = 0

    for i in range(menor, mayor + 1):
        suma += i

    return suma


def mult_dig(a, b):

    if a < b:
        menor = a
        mayor = b
    else:
        menor = b
        mayor = a

    mult = 1

    for i in range(menor, mayor + 1):
        mult *= i

    return mult


def proceso(a, b):

    estados = []

    print(f"\nProcesando {a} y {b}\n")

    for n in [a, b]:
        estado = analizar_numero(n)
        estados.append(estado)
        print()

    if estados[0] == -1 and estados[1] == -1:
        resultado = mult_dig(a, b)
        print("Multiplicación de los intermedios:", resultado)
    else:
        resultado = suma_dig(a, b)
        print("Suma de los intermedios:", resultado)

    if resultado % 2 == 0:
        print("El resultado es par.")
        print("Elevado al cubo:", resultado ** 3)
    else:
        print("El resultado es impar.")
        print("Elevado al cuadrado:", resultado ** 2)


def main():

    print("========== PUNTOS 1 AL 6 ==========")

    enteros = list(map(int, input("Ingrese 2 números separados por una coma: ").split(",")))

    proceso(enteros[0], enteros[1])

    print("\n========== PUNTO 7 ==========")

    codigo = input("Ingrese su código estudiantil: ")

    for i in range(len(codigo) - 1):

        a = int(codigo[i])
        b = int(codigo[i + 1])

        proceso(a, b)


main()

# =======================
# Punto 8

# 1. Solicitar el día.
# 2. Solicitar el mes en letras.
# 3. Solicitar el año.
# 4. Solicitar el código estudiantil.
# 5. Formar la fecha completa.
# 6. Recorrer el código estudiantil de dos en dos.
# 7. Enviar cada pareja de dígitos a la función proceso() para volver a realizar
#    las validaciones anteriores.
# 8. Mostrar la fecha completa.

# Leer día
# Leer mes
# Leer año
# Leer código
#
# fecha = día + "/" + mes + "/" + año
#
# Para cada pareja de dígitos del código:
#     proceso(a,b)
#
# Mostrar fecha
# =======================

# Punto 9

# Recorrer la fecha caracter por caracter.
# Si el caracter es una letra: 
#    Si pertenece a "aeiouAEIOU":
#        Mostrar "Vocal"
#    Sino:
#        Mostrar "Consonante"
#
# Los números y símbolos como "/" se ignoran.

# =======================

# Punto 10

# vocales = 0
# consonantes = 0
#
# Para cada carácter de la fecha:
#
#     Si es una letra:
#
#         Si es vocal:
#             vocales = vocales + 1
#
#         Sino:
#             consonantes = consonantes + 1
#
# Mostrar la cantidad de vocales.
# Mostrar la cantidad de consonantes.

# =======================
