#################### EJERCICIO 02 ############################
#### Escribe un programa en Python que reciba un año por la entrada estándar 
#### y devuelva si es un año bisiesto o no. 
#### Un año bisiesto es divisible por 4 pero no lo es si es divisible por 100 pero no por 400.
#### El programa deberá informar al usuario si introduce un valor de año no válido
#### considerando que el calendario gregoriano entró en vigor en 1582.

year = int(input("Introduce un año: "))

if year < 1582:
    print("Año introducido anterior al calendario gregoriano")
elif year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
    print(year,"es bisiesto")
else:
    print(year,"no es bisiesto")