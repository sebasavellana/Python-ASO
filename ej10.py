#################### EJERCICIO 10 ############################
# Implementa un script en Python en el que se borrarán el primer y el último carácter 
# de un string introducido por la entrada estándar. 
# El string resultante deberá ser mostrado por la salida estándar.
# Deberás comprobar que el usuario no introduce un string de longitud menor o igual a 2 caracteres.

inp = input("Introduce un string: ")

if len(inp) <= 2:
    print("Debes introducir un string más largo")
    exit()
else:
    print(inp[1:-1])