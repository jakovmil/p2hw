def poruka_pozdrava(ime_korisnika):
    return f"Pozdrav {ime_korisnika}!"

izraz_dobrodoslice = lambda ime_korisnika: f"Dobrodošao {ime_korisnika}!"

def pokreni(akcija):
    print(akcija("Jakov"))

pokreni(poruka_pozdrava)