ent = input("Introduce un carácter o número: ")

if ent.islower() == True:
    print("Es minúscula")
elif ent.isupper() == True:
    print("Es mayúscula")
elif ent.isnumeric() == True:
    print("Es un número")
else:
    print("Es un carácter especial")