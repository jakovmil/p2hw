import random

velicina_mreze = 7

mreza = [[random.randint(1, 9) for _ in range(velicina_mreze)] for _ in range(velicina_mreze)]

print("Generirana matrica:")
for redak in mreza:
    print(redak)

suma_okvira = 0

if velicina_mreze > 0:
    suma_okvira += sum(mreza[0])
    
    if velicina_mreze > 1:
        suma_okvira += sum(mreza[-1])
        
        for i in range(1, velicina_mreze - 1):
            suma_okvira += mreza[i][0] + mreza[i][-1]

print(f"\nZbroj elemenata na rubovima matrice je: {suma_okvira}")