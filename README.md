# projektna naloga - Analiza datumov na strani Wikipedia
Avtor: Živa Hegler

## uvod
Za projektno nalogo sem se odločila analizirati podatke na spletni strani (https://en.wikipedia.org/wiki/List_of_days_of_the_year), ki vsebuje seznam vseh dni v letu. Vsak izmed dni pa vsebuje seznam posebnih dogodkov, rojstev in smrti, pri čemer se rojstva in smrti ne štejejo pod dogodke. 
Nekaj vprašanj, ki so usmerjala projektno nalogo:
- Koliko je podatkov za posamezen dan?
   - Ali je očitno manj podatkov za 29. februar?
   - Ali obstaja kakšen trend za smrti ali rojstva skozi leto?
- Kako širok je razpon podatkov?
    - Koliko je različnih oseb?
    - Je naša informiranost skozi leta naraščala?
    - Ali je podaljšana življenjska doba očitna?
    - Kako je življenjska doba porazdeljena?
    - Kako so podatki porazdeljeni?
- V kolikšni meri vplivajo bitke na ostale podatke?
    - Ali bo zaradi bitk očiten narast števila smrti?

## navodila
Za nemoteno delovanje mora imeti uporabnik naložene knjižnice re, requests, pandas, numpy, csv in matplotlib.pyplot.
Če pri letnici zraven piše -, to pomeni, da je to leto pred našim štetjem.
koda 404 pri življenski dobi pomeni, da je ni bilo mogoče izračunati.

## kratek opis postopka
1. preberi_bloke.py je datoteka, ki iz spletnih strani posameznih datumov pobere html in ga razdeli na bloke o rojstvu in smrti.
2. preberi_info.py iz posameznega bloka izlušči pomembne podatke.
3. dodatne_funkcije.py vsebuje funkcije, ki kodo v ostalih datotekah naredijo bolj pregledno.
4. tabela_csv.py vzame izluščene podatke in jih zapiše v csv datoteke.
5. grafi.py ima shranjeno funkcijo za graf v analizi.
6. analiza.ipynb zbrane podatke predstavi s pomočjo grafov in histogramov.
