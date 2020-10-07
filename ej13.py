#################### EJERCICIO 13 ############################
# Implementa un script en Python que partiendo de una lista vacía contenga 
# los 20 primeros números naturales elevados al cuadrado. 
# El script deberá mostrar por la salida estándar desde 6^2 hasta 20^2

numlist = list()

for i in range(1,21):
    numlist.append(i**2)
print(numlist[5:])