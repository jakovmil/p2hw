imena = ["Ivan", "Ana", "Marko"]
prezimena = ["Ivic", "Anic", "Markic"]
godine = [20, 19, 21]
skor = [45, 78, 92]

studenti = list(zip(imena, prezimena, godine, skor))

def sortiraj_po_prezimenu(osoba):
    return osoba[1]

studenti.sort(key=sortiraj_po_prezimenu)

print("--- Sortirana lista po prezimenima ---")
for s in studenti:
    print(s)

kategorije_ocjena = {
    "Nedovoljan": 0,
    "Dovoljan": 0,
    "Dobar": 0,
    "Vrlodobar": 0,
    "Izvrstan": 0
}

for _, _, _, postotak in studenti:
    if postotak < 50:
        kategorije_ocjena["Nedovoljan"] += 1
    elif 50 <= postotak <= 65:
        kategorije_ocjena["Dovoljan"] += 1
    elif 65 < postotak <= 80:
        kategorije_ocjena["Dobar"] += 1
    elif 80 < postotak <= 90:
        kategorije_ocjena["Vrlodobar"] += 1
    else:
        kategorije_ocjena["Izvrstan"] += 1

print("\n--- Broj ostvarenih ocjena ---")
for ocjena, kolicina in kategorije_ocjena.items():
    print(f"{ocjena} : {kolicina}")