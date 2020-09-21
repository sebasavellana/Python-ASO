#################### EJERCICIO 05 ############################
# Implementa un script que calcule los divisores de un numero entero introducido por la entrada estándar. 
# Al finalizar el script deberá indicar si el número introducido es primo o no.

num = int(input("Introduce un número: "))
i = 2
is_prime = True

print(num,"es divisible por 1 y por",num)

while i < num:
    if num % i == 0:
        print(num,"es divisible por",i)
        is_prime = False
    i += 1

if is_prime == True:
    print(num,"es primo")