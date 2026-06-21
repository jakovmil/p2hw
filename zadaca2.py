import random

lista_studenata = ["Jakov", "Tin", "Ivan", "Toni", "Robert", "Marko", "Ljubo",
         "Josipa", "Magdalena", "Ivana", "Stipe", "Emanuel", "Petar",
         "Ivan", "Luka", "Filip", "Lara", "Laura", "Mario", "Ana", "Marija",
         "Nikolina", "Andrija", "Slaven", "Sebastian", "Marko", "Frano",
         "Stipan", "Eugen", "Toni", "Dražan", "Matej", "Nives", "Nemanja",
         "Sara", "Ružica", "Gabrijel", "Darian", "Ivana", "Ivan Stjepan",
         "Kristian", "Josip", "Tomislav", "Jovan", "Gabrijel", "Mia", "Ante",
         "Josip", "Ante", "Josip", "Danijel", "Goran", "Zoran Ivan",
         "Franjo Francisko", "Sergej", "Matej", "Marin", "Sara", "Josip",
         "Stjepan", "Iva", "Marko", "Sara", "Krešimir", "Magdalena", "Marko",
         "Mirko", "David", "Ema", "Paul", "Sven", "Natalija", "Petar",
         "Emanuel", "Helena", "Antonio", "Petar"]

evidencija_rezultata = []
frekvencija_ocjena = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
broj_pozitivnih = 0

for osoba in lista_studenata:
    dobivena_ocjena = random.randint(1, 5)
    
    evidencija_rezultata.append((osoba, dobivena_ocjena))
    frekvencija_ocjena[dobivena_ocjena] += 1
    
    if dobivena_ocjena >= 2:
        broj_pozitivnih += 1

ukupno_upisanih = len(lista_studenata)
udio_prolaznosti = (broj_pozitivnih / ukupno_upisanih) * 100

print("Prikaz ocjena svih studenata:")
for ime, ocj in evidencija_rezultata:
    print(f"{ime} -> {ocj}")

print("\nDistribucija ocjena:", frekvencija_ocjena)
print(f"Uspješnost prolaza: {udio_prolaznosti:.2f}%")