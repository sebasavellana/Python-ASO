ent = input("Introduce un string: ")

if len(ent) <= 2:
    print("Debes introducir un string más largo")
    exit
else:
    print(ent[1:-1])