import csv
from preberi_bloke import *
from preberi_info import *


def zapisi_csv(ime_datoteke):
    with open(ime_datoteke, "w", encoding="utf8") as file:
        pisatelj = csv.writer(file)
        pisatelj.writerow(["Ime"])
        html_koda = html("https://en.wikipedia.org/wiki/July_1")
        bloki = poisci_dogodke(html_koda)
        for blok in bloki:
            slovar = zberi_bitke(blok)
            if slovar["ime_bitke"] != None:
                pisatelj.writerow([slovar["ime_bitke"]])

#posploši html

#zapisi_csv("dat.csv")

def zapisi_csv_oseb(ime_datoteke):
    with open(ime_datoteke, "w", encoding="utf8") as file:
        pisatelj = csv.writer(file)
        pisatelj.writerow(["Ime", "Naziv", "Rojstvo", "Smrt"])
        html_koda = html("https://en.wikipedia.org/wiki/July_1")

        bloki1 = poisci_podatke(poisci_rojstva(html_koda))
        for blok1 in bloki1:
            slovar = zberi_osebe_rojstvo(blok1)
            # print(slovar)
            pisatelj.writerow([
                slovar["ime"],
                slovar["naziv"],
                slovar["rojstvo"],
                slovar["smrt"],
                ])

        bloki2 = poisci_podatke(poisci_smrti(html_koda))
        for blok2 in bloki2:
            slovar = zberi_osebe_smrt(blok2)
            #print(slovar)
            pisatelj.writerow([
                slovar["ime"],
                slovar["naziv"],
                slovar["rojstvo"],
                slovar["smrt"],
                ])

zapisi_csv_oseb("dat_oseb.csv")

