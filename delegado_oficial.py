import random
numbers = list()

for num in range(1,50000):
    num = random.randint(1,50000)
    numbers.append(num)

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        odd += 1
    else:
        even += 1

if odd > even:
    print("Pares:",odd,"\nImpares:",even,"\n\n**** Delegado oficial del subgrupo A (ALBERGES) ****")
else:
    print("Pares:",odd,"\nImpares:",even,"\n\n**** Delegado oficial del subgrupo B (BORRAJAS) ****")
