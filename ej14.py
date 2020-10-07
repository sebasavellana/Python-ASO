#################### EJERCICIO 14 ############################
# Implementa un programa en Python que muestre por la salida estándar 
# la palabra de mayor longitud de una lista de strings que estará prefijada 
# en el código del script y siempre será la misma.

words = ["Hola", "Después", "Adios"]
longest = len(words[0])

for word in words:
    if len(word) > longest:
        longest = len(word)

print("Longitud máxima: ", longest)