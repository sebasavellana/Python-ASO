words = ["Hola", "Adios", "Después"]
max_long = 0

for i in words:
    long = len(i)
    if long > max_long:
        max_long = long

print("Longitud máxima", max_long)