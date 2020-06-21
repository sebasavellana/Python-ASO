try:
    dividendo = int(input("Introduce el dividendo "))
    divisor = int(input("Introduce el divisor "))
    print (dividendo / divisor)
except ZeroDivisionError:
    print("División por cero")
except ValueError:
    print("División en coma flotante no soportada")