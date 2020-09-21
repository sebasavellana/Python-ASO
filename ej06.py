#################### EJERCICIO 06 ############################
# Obtén mediante un script en Python un número natural que cumpla las siguientes tres condiciones:
# Sea mayor que el resultado de la operación 13 * 6
# Sea menor que el resultado de la operación 5 * 17
# Sea divisible por 10

for num in range(65,85):
    if num > 13 * 6 and num < 5 * 17 and num % 10 == 0:
        print(num)