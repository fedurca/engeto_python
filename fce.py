from math import pi as pa
import math

jmeno = "Matous"
vek = 44
je_uzivatel = True


def vytvor_pozdrav(jmeno, / ,uzivatel):
    if not uzivatel:
        pozdrav = "Neni uzivatel" + jmeno
    else:
        pozdrav = "Ahoj, " + jmeno
    return pozdrav
    

print(help(math))