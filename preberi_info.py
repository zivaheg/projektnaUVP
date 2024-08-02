from preberi_bloke import *

def zberi_bitke(blok_dogodka):
    """iz dogodka izlušči samo bitko"""
    vzorec_bitke = re.compile(r">Battle of (?P<ime_bitke>.*?)</a>", re.DOTALL)
    najdena_bitka = vzorec_bitke.search(blok_dogodka)
    slovar = {}
    slovar.setdefault("ime_bitke", None)
    if najdena_bitka != None:
        slovar["ime_bitke"] = najdena_bitka["ime_bitke"]
    return slovar

#print(len(zberi_bitke(poisci_dogodke(html("https://en.wikipedia.org/wiki/July_1")))))
#print(zberi_bitke(poisci_dogodke(html("https://en.wikipedia.org/wiki/July_1"))))

#nekje dodam izpisan datum, ki bo znotraj for zanke
#podatki so samo o osebah z wikipedia stranjo

def zberi_osebe_rojstvo(blok_rojstev):
    """iz bloka rojstva razdeli podatke na ime, naziv, rojstvo in smrt, če je podana in jih vrne v slovarju"""
    vzorec_rojstva = re.compile(r"<li>.*?(?P<rojstvo>\d{1,4}).*?&#8211", re.DOTALL)
    vzorec_imena = re.compile(r'&#8211; <a href="/wiki/.*?" title=".*?">(?P<ime>.*?)</a>', re.DOTALL)
    vzorec_naziva = re.compile(r"\D<\/a>,?(?P<naziv>.*?)(\(|<)", re.DOTALL)
    vzorec_smrti = re.compile(r"<li>.*?\(d. (?P<smrt>\d{1,4})\)</li>", re.DOTALL)

    # for blok in bloki_rojstev:
    najdeno_rojstvo = vzorec_rojstva.search(blok_rojstev)
    najdeno_ime = vzorec_imena.search(blok_rojstev)
    najdeno_naziv = vzorec_naziva.search(blok_rojstev)
    najdeno_smrt = vzorec_smrti.search(blok_rojstev)

    slovar = {}
    #slovar.setdefault("ime", None)
    #if najdeno_ime != None:
    slovar["ime"] = najdeno_ime["ime"]
    slovar.setdefault("naziv", None)
    if najdeno_naziv != None:
        slovar["naziv"] = najdeno_naziv["naziv"]
    # slovar.setdefault("rojstvo", None)
    # if najdeno_rojstvo != None:
    slovar["rojstvo"] = najdeno_rojstvo["rojstvo"]
    slovar.setdefault("smrt", None)
    if najdeno_smrt != None:
        slovar["smrt"] = najdeno_smrt["smrt"]

    return slovar
    #nekej (1-4 stevilke) nekej  

#print(zberi_osebe_rojstvo('<li><a href="/wiki/1311" title="1311">1311</a> &#8211; <a href="/wiki/Liu_Bowen" title="Liu Bowen">Liu Bowen</a>, Chinese military strategist, statesman and poet (d. 1375)</li>'))
# print(poisci_rojstva(html("https://en.wikipedia.org/wiki/July_1")))
print(zberi_osebe_rojstvo(poisci_podatke(poisci_rojstva(html("https://en.wikipedia.org/wiki/July_1")))))

def zberi_osebe_smrt(blok_smrti: list):
    """iz bloka smrti razdeli podatke na ime, naziv, rojstvo in smrt, če je podana in jih vrne v slovarju"""
    vzorec_smrti = re.compile(r"<li>.*?(?P<smrt>\d{1,4}).*?&#8211", re.DOTALL)
    vzorec_imena = re.compile(r'&#8211; <a href="/wiki/.*?" title=".*?">(?P<ime>.*?)</a>', re.DOTALL)
    vzorec_naziva = re.compile(r"\D<\/a>,?(?P<naziv>.*?)(\(|<)", re.DOTALL)
    vzorec_rojstva = re.compile(r"<li>.*?\(b. (?P<rojstvo>\d{1,4})\)?</li>", re.DOTALL)

    #for blok in bloki_smrti:
    najdeno_ime = vzorec_imena.search(blok_smrti)
    najdeno_naziv = vzorec_naziva.search(blok_smrti)
    najdeno_rojstvo = vzorec_rojstva.search(blok_smrti)
    najdeno_smrt = vzorec_smrti.search(blok_smrti)

    slovar = {}
    #slovar.setdefault("ime", None)
    #if najdeno_ime != None:
    slovar["ime"] = najdeno_ime["ime"]
    slovar.setdefault("naziv", None)
    if najdeno_naziv != None:
        slovar["naziv"] = najdeno_naziv["naziv"]
    slovar.setdefault("rojstvo", None)
    if najdeno_rojstvo != None:
        slovar["rojstvo"] = najdeno_rojstvo["rojstvo"]
    #slovar.setdefault("smrt", None)
    #if najdeno_smrt != None:
    slovar["smrt"] = najdeno_smrt["smrt"]

    return slovar
#print(zberi_osebe_smrt(poisci_podatke(poisci_smrti(html("https://en.wikipedia.org/wiki/July_1")))))
#print(poisci_podatke(poisci_smrti(html("https://en.wikipedia.org/wiki/July_1"))))