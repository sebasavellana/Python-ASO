num = int(input("Introduce un número "))
div = 0
i = 1
contdivisors = 0

# BUCLE WHILE
while (i < num):
    if num % i == 0:
        print(i ,"es divisor de", num)
        contdivisors += 1
    i += 1

print(contdivisors)
if contdivisors == 1:
    print(num ,"es primo")

## BUCLE FOR
for i in range(1,num):
    if num % i == 0:
        print(i,"es divisor de", num)
        contdivisors += 1

print(contdivisors)
if contdivisors == 2:
    print(num ,"es primo")