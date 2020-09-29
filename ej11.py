#################### EJERCICIO 11 ############################
# Implementa un script que muestre por la salida estándar un string formado por 
# los dos primeros y los dos últimos caracteres de un string introducido por la entrada estándar.
# El script deberá mostrar un string vacío en caso de que la longitud del string introducido sea menor que dos.

inp = input("Introduce un string ")

if len(inp) > 2:
    print(inp[0:2] + inp[-2:])
else:
    print("")