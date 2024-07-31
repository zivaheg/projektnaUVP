import re
import requests


with open("1.html", "r", encoding="utf8") as d:
    vsebina = d.read()

def poisci_letnice(niz: str, vzorec):
    indeks = niz.find(vzorec)
    letnica = niz[indeks]
    yield letnica

vzorec = r"\b\d{1,4}\s\–"
#začetek besede   med 1 in 4 ponovitve črk   presledek aka white space  znakec – 