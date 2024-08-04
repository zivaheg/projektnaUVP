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

#posploši html

#zapisi_csv("dat.csv")

def zapisi_csv_oseb(ime_datoteke):
    """zapiše csv datoteko s podatki o imenu, nazivu, letnici rojstva in smrti, če sta ti podani in življensko dobo"""
    with open(ime_datoteke, "w", encoding="utf8") as file:
        pisatelj = csv.writer(file)
        pisatelj.writerow(["Ime", "Naziv", "Rojstvo", "Smrt", "Življenska doba"])
        html_koda = html("https://en.wikipedia.org/wiki/July_1")

        bloki1 = poisci_podatke(poisci_smrti(html_koda))
        for blok1 in bloki1:
            zivljenska_doba = r"¯\_(ツ)_/¯"
            slovar = zberi_osebe_smrt(blok1)
            if (slovar["rojstvo"] and slovar["smrt"]) != None:
                #print(slovar["smrt"], slovar["rojstvo"], int(slovar["smrt"]) - int(slovar["rojstvo"]))
                zivljenska_doba = int(slovar["smrt"]) - int(slovar["rojstvo"])
            #print(slovar)
            pisatelj.writerow([
                slovar["ime"],
                slovar["naziv"],
                slovar["rojstvo"],
                slovar["smrt"],
                zivljenska_doba
                ])

        bloki2 = poisci_podatke(poisci_rojstva(html_koda))
        for blok2 in bloki2:
            zivljenska_doba = r"¯\_(ツ)_/¯"
            slovar = zberi_osebe_rojstvo(blok2)
            if (slovar["rojstvo"] and slovar["smrt"]) != None:
                zivljenska_doba = int(slovar["smrt"]) - int(slovar["rojstvo"])
                #print(slovar["smrt"], slovar["rojstvo"], int(slovar["smrt"]) - int(slovar["rojstvo"]))
            # print(slovar)
            pisatelj.writerow([
                slovar["ime"],
                slovar["naziv"],
                slovar["rojstvo"],
                slovar["smrt"],
                zivljenska_doba
                ])


zapisi_csv_oseb("dat_oseb.csv")

