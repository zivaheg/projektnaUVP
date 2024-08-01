from preberi_bloke import *

def zberi_bitke(blok_dogodka):
    """iz dogodka izlušči samo bitko"""
    vzorec_bitke = re.compile(r">Battle of (?P<ime_bitke>.*?)</a>", re.DOTALL)
    najdena_bitka = vzorec_bitke.search(dogodki)
    slovar = {}
    slovar.setdefault("ime_bitke", None)
    if najdena_bitka != None:
        slovar["ime_bitke"] = najdena_bitka["ime_bitke"]
    return slovar

#print(len(zberi_bitke(poisci_dogodke(html("https://en.wikipedia.org/wiki/July_1")))))
#print(zberi_bitke(poisci_dogodke(html("https://en.wikipedia.org/wiki/July_1"))))
