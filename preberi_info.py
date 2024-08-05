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
    vzorec_imena = re.compile(r'(&#8211;|–).*?<a href="\/wiki\/.*?" title=".*?">(?P<ime>.*?)<\/a>', re.DOTALL)
    vzorec_naziva = re.compile(r"\D<\/a>,? (<a.*?>)?(?P<naziv1>.*?) ?(<\/a>.*?<a.*?>(?P<naziv2>.*?))?(\(b. (.*?)?|<)", re.DOTALL)
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
    slovar.setdefault("naziv1", None)
    slovar.setdefault("naziv2", None)
    if najdeno_naziv != None:
        if najdeno_naziv["naziv2"] != None:
            slovar["naziv"] = najdeno_naziv["naziv1"] + najdeno_naziv["naziv2"]
        else:
            slovar["naziv"] = najdeno_naziv["naziv1"]
    #slovar.setdefault("rojstvo", None)
    #if najdeno_rojstvo != None:
    slovar["rojstvo"] = najdeno_rojstvo["rojstvo"]
    slovar.setdefault("smrt", None)
    if najdeno_smrt != None:
        slovar["smrt"] = najdeno_smrt["smrt"]

    slovar.pop("naziv1")
    slovar.pop("naziv2")
    return slovar
    #nekej (1-4 stevilke) nekej  

#print(zberi_osebe_rojstvo('<li><a href="/wiki/1311" title="1311">1311</a> &#8211; <a href="/wiki/Liu_Bowen" title="Liu Bowen">Liu Bowen</a>, Chinese military strategist, statesman and poet (d. 1375)</li>'))
# print(poisci_rojstva(html("https://en.wikipedia.org/wiki/July_1")))
#print(zberi_osebe_rojstvo(poisci_podatke(poisci_rojstva(html("https://en.wikipedia.org/wiki/July_1")))))

def zberi_osebe_smrt(blok_smrti: list):
    """iz bloka smrti razdeli podatke na ime, naziv, rojstvo in smrt, če je podana in jih vrne v slovarju"""
    vzorec_smrti = re.compile(r"<li>.*?(?P<smrt>\d{1,4}).*?&#8211", re.DOTALL)
    vzorec_imena = re.compile(r'(&#8211;|–).*?<a href="\/wiki\/.*?" title=".*?">(?P<ime>.*?)<\/a>', re.DOTALL)
    vzorec_naziva = re.compile(r"\D<\/a>,? (<a.*?>)?(?P<naziv1>.*?) ?(<\/a>.*?<a.*?>(?P<naziv2>.*?))?(\(b. (.*?)?|<)", re.DOTALL)
    vzorec_rojstva = re.compile(r"<li>.*?\(b. (?P<rojstvo>\d{1,4})\)?</li>", re.DOTALL)

    #for blok in bloki_smrti:
    najdeno_ime = vzorec_imena.search(blok_smrti)
    najdeno_naziv = vzorec_naziva.search(blok_smrti)
    najdeno_rojstvo = vzorec_rojstva.search(blok_smrti)
    najdeno_smrt = vzorec_smrti.search(blok_smrti)

    slovar = {}
    slovar.setdefault("ime", None)
    if najdeno_ime != None:
        slovar["ime"] = najdeno_ime["ime"]
    #slovar.setdefault("naziv1", None)
    slovar.setdefault("naziv2", None)
    if najdeno_naziv != None:
        if najdeno_naziv["naziv2"] != None:
            slovar["naziv"] = najdeno_naziv["naziv1"] + " " + najdeno_naziv["naziv2"]
        else:
            slovar["naziv"] = najdeno_naziv["naziv1"]
    slovar.setdefault("rojstvo", None)
    if najdeno_rojstvo != None:
        slovar["rojstvo"] = najdeno_rojstvo["rojstvo"]
    slovar.setdefault("smrt", None)
    if najdeno_smrt != None:
        slovar["smrt"] = najdeno_smrt["smrt"]

    #slovar.pop("naziv1")
    slovar.pop("naziv2")
    return slovar
#print(zberi_osebe_smrt(poisci_podatke(poisci_smrti(html("https://en.wikipedia.org/wiki/July_1")))))
#print(poisci_podatke(poisci_smrti(html("https://en.wikipedia.org/wiki/July_1"))))

bloki = poisci_podatke(poisci_smrti(html("https://en.wikipedia.org/wiki/January_1")))
for blok in bloki:
    print(zberi_osebe_smrt(blok))


#popravi/odstrani nepotrebne narekovaje

#narekovaji = """<li><a href="/wiki/1774" title="1774">1774</a> &#8211; <a href="/wiki/Henry_Fox,_1st_Baron_Holland" title="Henry Fox, 1st Baron Holland">Henry Fox, 1st Baron Holland</a>, English politician, <a href="/wiki/Secretary_of_State_for_the_Southern_Department" title="Secretary of State for the Southern Department">Secretary of State for the Southern Department</a> (b. 1705)</li>
#<li><a href="/wiki/1782" title="1782">1782</a> &#8211; <a href="/wiki/Charles_Watson-Wentworth,_2nd_Marquess_of_Rockingham" title="Charles Watson-Wentworth, 2nd Marquess of Rockingham">Charles Watson-Wentworth, 2nd Marquess of Rockingham</a>, English politician, <a href="/wiki/Prime_Minister_of_Great_Britain" class="mw-redirect" title="Prime Minister of Great Britain">Prime Minister of Great Britain</a> (b. 1730)<sup id="cite_ref-76" class="reference"><a href="#cite_note-76">&#91;76&#93;</a></sup></li>"""
#print(zberi_osebe_smrt(narekovaji))