#################### EJERCICIO 09 ############################
# Implementa un script en Python que calcule el máximo común divisor (MCD)
# de dos números enteros positivos.
# Para realizar el cálculo deberás implementar el algoritmo de Euclides, 
# en el cual se realizan los siguientes pasos:
# 1 - Divide el número mayor por el número menor
# 2 - Si la división es exacta, el divisor es el MCD
# 3 - Si la división no es exacta, divide el divisor entre el resto obtenido y continúa hasta 
# obtener una división exacta. El último divisor obtenido será el MCD
# El script deberá interrumpirse si el usuario introduce un número negativo.

num1 = int(input("Introduce un número "))
num2 = int(input("Introduce un número "))

if num1 >= num2:
    dividendo = num1
    divisor = num2
else:
    dividendo = num2
    divisor = num1

resto = 1

while resto != 0:
    resto = dividendo % divisor
    if resto  == 0:
        print("MCD es",divisor)
    else:
        dividendo = divisor
        divisor = resto