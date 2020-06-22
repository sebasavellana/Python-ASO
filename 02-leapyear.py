year = int(input("Introduce el año: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(year ,"es bisiesto")
else:
    print(year ,"no es bisiesto")