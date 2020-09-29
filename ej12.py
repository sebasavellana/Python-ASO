#################### EJERCICIO 12 ############################
# Implementa un script que introducido un string por la entrada estándar 
# muestre por la salida estándar los dos caracteres centrales de dicho string.
# Si el string tiene una longitud impar deberá mostrar un único carácter central. 
# Sin embargo, un string de longitud impar deberá mostrar los dos caracteres centrales. 
# Si introduce un string vacío deberá mostrar un aviso al usuario.

inp = input("Introduce un string: ")

position = len(inp) // 2

if len(inp) == 0:
    print("String vacío")
elif len(inp) % 2 == 0:
    print(inp[position-1:position+1])
else:
    print(inp[position])