# Dado un string de palabras, el cual estará prefijado en el script, 
# obtén la longitud de la palabra más corta que contiene.

phrase = "Te diré lo que quiero, lo que quiero de verdad; dime lo que quieres, " \
"lo que quieres de verdad; te dire lo que quiero, lo que quiero de verdad; " \
"dime lo que quieres, lo que quieres de verdad"
words = phrase.split()
shortest = len(words[0])

for word in words:
    if len(word) < shortest:
        shortest = len(word)
print("Palabra más corta: ",shortest)