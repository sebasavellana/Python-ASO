""" ent1 = input("Introduce un número: ")
ent2 = input("Introduce otro número: ")

if ent1.isnumeric() == True and ent2.isnumeric() == True:
    int(ent1)
    int(ent2)
    if ent1 == ent2:
        print("Son iguales")
    elif ent1 > ent2:
        print(ent1,"es mayor")
    else:
        print(ent2,"es mayor")
else:
    print("Debes introducir un número") """

try:
    ent1 = int(input("Introduce un número: "))
    ent2 = int(input("Introduce otro número: "))
    if ent1 == ent2:
        print("Son iguales")
    elif ent1 > ent2:
        print(ent1,"es mayor")
    else:
        print(ent2,"es mayor")
except ValueError:
    print("Debes introducir un número")