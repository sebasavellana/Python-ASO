#!/usr/bin/env python

lista = [2,3,4,5,6,7]
suma = 0
multi = 1

ent = input("Introduce s para suma m para multiplicación ")
if ent == "s":
    for i in lista:
        suma = suma + i
    print("Resultado final de la suma: ", suma)
elif ent == "m":
    for i in lista:
        multi = multi * i
    print("Resultado final de la multiplicación ", multi)
else:
    print("Parámetro incorrecto")