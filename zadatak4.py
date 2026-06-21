import re

sablon = r"^[Tt](?=.*[0-5])(?=.* ).*[Ss]$"

nizovi = [
    "T 3 S",          
    "t neki 4 teksts",
    "T9 S",           
    "T3S",            
    "M 3 S"           
]

print("--- Rezultati provjere ---")
for tekst in nizovi:
    if re.match(sablon, tekst):
        print(f"'{tekst}' -> ODGOVARA")
    else:
        print(f"'{tekst}' -> NE ODGOVARA")