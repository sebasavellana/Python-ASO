word = list("hipoglucido")
hidden = list()

for char in word:
    hidden.append("_")

maxtries = 5
tries = 0
isgameover = False
guess = ""
hits = 0

while isgameover == False:

    print("Te quedan",maxtries - tries,"intentos")
    print(hidden)

    guess = input("Introduce una letra ")

    if guess in word:
        print("La letra", guess ,"está en la palabra")
        for i in range(len(word)):
            if word[i] == guess:
                hidden[i] = word[i]
                word[i] = "_"
                hits += 1
    else:
        print("La letra",guess,"no está en la palabra")
        tries = tries + 1

    if tries == maxtries:
        print("Has perdido")
        isgameover = True
    if hits == len(word):
        print("Has ganado")
        print(hidden)
        isgameover = True
    
