# projektna naloga - Analiza datumov na strani Wikipedia
Avtor : Živa Hegler

## uvod
Za projektno nalogo sem se odločila analizirati podatke na spletni strani (https://en.wikipedia.org/wiki/List_of_days_of_the_year), ki vsebuje seznam vseh dni v letu. Vsak izmed dni pa vsebuje seznam posebnih dogodkov, rojstev, smrti in praznikov. 
Nekaj vprašanj, ki so motivirala projektno nalogo:
- Koliko je podatkov za posamezen dan?
   - Je število rojstev in smrti očitno manjše 29. Februarja?
   - Ali obstaja kakšen trend za smrti ali rojstva skozi leto?
- Kako je naša informiranost naraščala skozi leta?
- Koliko je zabeleženih bitk?
- Ali bo podaljšana življenjska doba očitna?
- Kateri dan imamo največ praznikov?
- Ali obstaja korelacija med prazniki, ter rojstvom in smrtjo?

## navodila
Za nemoteno delovanje, mora imeti uporabnik naložene knjižnice ali pakete re, requests, pandas in csv.
Če pri letnici zraven piše -, to pomeni da je to leto izpred našega štetja.

## kratek opis postopka
1. preberi_bloke.py je datoteka, ki iz spletnih strani posameznih datumov pobere html in ga razdeli na bloke o rojstvu, smrti in praznikih
2. preberi_info.py iz posameznega bloka izlušči pomembne podatke.
3. dodatne_funkcije.py vsebuje funkcije, ki kodo v ostalih datotekah naredijo bolj pregledno.
4. tabela_csv.py vzame izluščene podatke in jih zapiše v csv datoteke.
5. analiza.ipynb zbrane podatke predstavi s pomočjo grafov in histogramov.
