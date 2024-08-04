import csv
from preberi_bloke import *
from preberi_info import *


def zapisi_csv(ime_datoteke):
    """ustvari csv datoteko z vsemi imeni bitk"""
    with open(ime_datoteke, "w", encoding="utf8") as file:
        pisatelj = csv.writer(file)
        pisatelj.writerow(["Ime"])
        html_koda = html("https://en.wikipedia.org/wiki/July_1")
        bloki = poisci_dogodke(html_koda)
        for blok in bloki:
            slovar = zberi_bitke(blok)
            if slovar["ime_bitke"] != None:
                pisatelj.writerow([slovar["ime_bitke"]])

#zapisi_csv("dat.csv")

def zapisi_csv_oseb(ime_datoteke):
    """zapiše csv datoteko s podatki o imenu, nazivu, letnici rojstva in smrti, če sta obe podani tudi življensko dobo"""
    with open(ime_datoteke, "w", encoding="utf8") as file:
        pisatelj = csv.writer(file)
        pisatelj.writerow(["Ime", "Naziv", "Rojstvo", "Smrt", "Življenska doba"])
        html_koda = html("https://en.wikipedia.org/wiki/July_1")


        bloki_smrti = poisci_podatke(poisci_smrti(html_koda))
        bloki_rojstev = poisci_podatke(poisci_rojstva(html_koda))
        bloki = bloki_smrti + bloki_rojstev
        for blok in bloki:
            zivljenska_doba = r"¯\_(ツ)_/¯"
            if blok in bloki_smrti:
                slovar = zberi_osebe_smrt(blok)
            else:
                slovar = zberi_osebe_rojstvo(blok)

            if (slovar["rojstvo"] and slovar["smrt"]) != None:
                zivljenska_doba = int(slovar["smrt"]) - int(slovar["rojstvo"])

            pisatelj.writerow([
                slovar["ime"],
                slovar["naziv"],
                slovar["rojstvo"],
                slovar["smrt"],
                zivljenska_doba
                ])

zapisi_csv_oseb("dat_oseb.csv")

