#################### EJERCICIO 15 ############################
# Modifica el ejercicio anterior para que calcule la longitud de la palabra 
# más larga de un string prefijado en el script. Para simplificar el ejercicio 
# los signos de puntuación que pudiera tener una frase se considerarán
# como parte de la longitud de la palabra a la que van unidos. 
# Por ejemplo: quiero, tendrá longitud 7 debido a la coma final.
# Además, deberá mostrar cuantas palabras (no importa si repetidas o no) se encuentran en el string.

phrase = "Te diré lo que quiero, lo que quiero de verdad; dime lo que quieres, " \
"lo que quieres de verdad; te dire lo que quiero, lo que quiero de verdad; " \
"dime lo que quieres, lo que quieres de verdad"
words = phrase.split()
longest = 0

for word in words:
    if len(word) > longest:
        longest = len(word)

print("Longitud máxima: ", longest)
print("Contador de palabras: ",len(words))