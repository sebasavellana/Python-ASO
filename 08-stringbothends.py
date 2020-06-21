ent = input("Introduce un string ")

if len(ent) > 2:
    print(ent[0:2] + ent[-2:])
else:
    print("")