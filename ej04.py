#################### EJERCICIO 04 ############################
#### Escribe un script que pida dos números por la entrada estándar y 
# muestre por pantalla, si dichos números son iguales o cual es el mayor de los dos. 
# Deberás implementar el control de errores necesario para verificar que se cargan valores numéricos.

ent1 = input("Introduce un número: ")
ent2 = input("Introduce otro número: ")

if ent1.isnumeric() == True and ent2.isnumeric() == True:
    ent1 = int(ent1)
    ent2 = int(ent2)
    if ent1 == ent2:
        print("Son iguales")
    elif ent1 > ent2:
        print(ent1,"es mayor")
    else:
        print(ent2,"es mayor")
else:
    print("No has introducido un número")