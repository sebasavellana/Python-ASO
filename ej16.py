#################### EJERCICIO 15 ############################
# . Modifica el ejercicio anterior de manera que el usuario introduzca 
# por la entrada estándar las palabras que desea comprobar. 
# El script deberá devolver la longitud de la palabra más larga que ha introducido y
# la cantidad de palabras que ha introducido.
# El script detectará que el usuario ha dejado de introducir palabras cuando 
# el usuario introduzca una cadena compuesta únicamente de un punto "."

words = list()
longest = 0
word = ""

print("Introduce una palabra. Para finalizar introduce un punto .")

while True:
    word = input()
    if word == ".":
        break
    words.append(word)

for word in words:
    if len(word) > longest:
        longest = len(word)

print("Longitud máxima: ", longest)
print("Contador de palabras: ",len(words))