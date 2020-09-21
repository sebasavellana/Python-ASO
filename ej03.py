#################### EJERCICIO 03 ############################
#### Implementa un script en Python que muestre por la salida estándar 
#### si el usuario ha introducido un carácter en mayúsculas, minúsculas, número o carácter especial.
#### Python dispone de varios métodos incluidos para realizar estas comprobaciones.
#### Si el usuario no introduce un único carácter el script deberá mostrar un mensaje de error.

inp = input("Introduce un carácter: ")

if len(inp) != 1:
    print("Solo debes introducir un carácter")
elif inp.islower() == True:
    print("Es minúscula")
elif inp.isupper() == True:
    print("Es mayúscula")
elif inp.isnumeric() == True:
    print("Es un número")
else:
    print("Es un carácter especial")