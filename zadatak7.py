def okreni_tekst(niz):
    if not niz:
        return niz
    else:
        return okreni_tekst(niz[1:]) + niz[0]

krajnji_rezultat = okreni_tekst("Programiranje")
print(krajnji_rezultat)