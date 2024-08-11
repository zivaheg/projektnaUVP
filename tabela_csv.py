import csv
from preberi_bloke import *
from preberi_info import *
from dodatne_funkcije import *


def zapisi_csv(ime_datoteke):
    """Ustvari csv datoteko z vsemi imeni bitk in vojn, ter izpisuje datume, da lahko slediš napredku (odstrani komentar)."""
    with open(ime_datoteke, "w", encoding="utf8", newline="") as file:
        pisatelj = csv.writer(file)
        pisatelj.writerow(["Ime bitke ali vojne", "Datum"])

        datumi = nastavi_html()
        for datum in datumi:
            [dan, mesec, url] = datum
            mesec = prevedi_mesec(mesec)
            #print(f"{dan} {mesec} {url}")

            bloki = poisci_podatke(poisci_dogodke(html(str(url))))
            for blok in bloki:
                slovar = zberi_bitke(blok)
                #print(slovar)
                if slovar["ime bitke ali vojne"] != None:
                    pisatelj.writerow([slovar["ime bitke ali vojne"], f"{dan}.{mesec}"])

#zapisi_csv("dat_bitk.csv")

def zapisi_csv_oseb(ime_datoteke):
    """Zapiše csv datoteko s podatki o imenu, nazivu, letnici rojstva in smrti, če sta obe podani tudi življensko dobo, ter izpisuje datume, da lahko slediš napredku (odstrani komentar)."""
    with open(ime_datoteke, "w", encoding="utf8", newline="") as file:
        pisatelj = csv.writer(file)

        pisatelj.writerow(["Datum", "Ime", "Naziv", "Rojstvo", "Smrt", "Življenjska doba"])
        datumi = nastavi_html()
        for datum in datumi:
            [dan, mesec, url] = datum
            mesec = prevedi_mesec(mesec)
            #print(f"{dan} {mesec} {url}")

            bloki_smrti = poisci_podatke(poisci_smrti(html(str(url))))
            bloki_rojstev = poisci_podatke(poisci_rojstva(html(str(url))))
            bloki = bloki_smrti + bloki_rojstev
            for blok in bloki:
                zivljenjska_doba = 404
                if blok in bloki_smrti:
                    slovar = zberi_osebe_smrt(blok)
                else:
                    slovar = zberi_osebe_rojstvo(blok)
                #print(slovar)

                if (slovar["rojstvo"] and slovar["smrt"]) != None:
                    zivljenjska_doba = funkcija_zivljenske_dobe(slovar["rojstvo"], slovar["smrt"])

                slovar["rojstvo"] = letnice_pred_0(slovar["rojstvo"])
                slovar["smrt"] = letnice_pred_0(slovar["smrt"])

                pisatelj.writerow([
                    f"{dan}.{mesec}",
                    slovar["ime"],
                    slovar["naziv"],
                    slovar["rojstvo"],
                    slovar["smrt"],
                    zivljenjska_doba
                    ])

#zapisi_csv_oseb("dat_oseb.csv")


def kolicine(ime_datoteke):
    """Za vsak dan izpiše koliko je podatkov o rojstvu in smrti, ter izpisuje datume, da lahko slediš napredku (odstrani komentar)."""
    with open(ime_datoteke, "w", encoding="utf8", newline="") as file:
        pisatelj = csv.writer(file)
        pisatelj.writerow(["Datum","Št. dogodkov","Št. bitk ali vojn", "Št. rojstev", "Št. smrti"])

        datumi = nastavi_html()
        for datum in datumi:
            [dan, mesec, url] = datum
            mesec = prevedi_mesec(mesec)
            print(datum) 

            blok_dogodkov = poisci_podatke(poisci_dogodke(html(str(url))))
            bloki_smrti = poisci_podatke(poisci_smrti(html(str(url))))
            bloki_rojstev = poisci_podatke(poisci_rojstva(html(str(url))))

            st_dogodkov = len(blok_dogodkov)
            st_smrti = len(bloki_smrti)
            st_rojstev = len(bloki_rojstev)

            stevec = 0
            for blok in blok_dogodkov:
                slovar = zberi_bitke(blok)
                if  slovar["ime bitke ali vojne"] != None:
                    stevec += 1

            st_bitk = stevec

            pisatelj.writerow([
                    f"{dan}.{mesec}",
                    st_dogodkov,
                    st_bitk,
                    st_rojstev,
                    st_smrti
                    ])

kolicine("st_podatkov.csv")