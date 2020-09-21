#################### EJERCICIO 08 ############################
# Implementa un script en Python que calcule el factorial de un número introducido por la entrada estándar.
# El factorial de un número natural es el producto de todos los números naturales desde 1 
# hasta dicho número natural. Por ejemplo:
# 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720
# Teniendo en cuenta que 0! = 1 el script deberá comprobar que el usuario 
# no introduce un valor numérico del que no se pueda calcular su factorial.

# 6! = 6 * 5 * 4 * 3 * 2 * 1 = 1 * 2 * 3 * 4 * 5 * 6

res = 1 # es factorial de 0
factorial = int(input("Introduce un número para calcular su factorial: "))
i = 1

if factorial < 0:
    print("Factorial de numero negativo")
    exit()
while i <= factorial:
    res = res * i
    i += 1
print(res)