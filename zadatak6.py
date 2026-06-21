def stvori_brojeve(limit):
    print("Parni:")
    for broj in range(limit):
        if broj % 2 == 0:
            yield broj

    print("Neparni:")
    for broj in range(limit):
        if broj % 2 != 0:
            yield broj

generator = stvori_brojeve(10)

for vrijednost in generator:
    print(vrijednost)