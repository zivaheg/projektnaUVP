from preberi_bloke import *


def zberi_bitke(blok_dogodka):
    """iz dogodka izlušči samo bitko ali vojno"""
    vzorec_bitke = re.compile(r'>"?(?P<ime_bitke>Battles? of .*?)<\/a>', re.DOTALL)
    vzorec_vojne = re.compile(r'<a.*?(w|W)ar.*?>(?P<ime_vojne>[^"]*?(w|W)ars? ?[^"]*?)<\/a>', re.DOTALL)
    najdena_bitka = vzorec_bitke.search(blok_dogodka)
    najdena_vojna = vzorec_vojne.search(blok_dogodka)
    slovar = {}
    slovar.setdefault("ime bitke ali vojne", None)
    if najdena_bitka != None:
        slovar["ime bitke ali vojne"] = najdena_bitka["ime_bitke"]
    if najdena_vojna != None:
        slovar["ime bitke ali vojne"] = najdena_vojna["ime_vojne"]
    return slovar

#print(len(zberi_bitke(poisci_dogodke(html("https://en.wikipedia.org/wiki/July_1")))))
#print(zberi_bitke(poisci_dogodke(html("https://en.wikipedia.org/wiki/January_1"))))


def zberi_osebe_rojstvo(blok_rojstev):
    """iz bloka rojstva razdeli podatke na ime, naziv, rojstvo in smrt, če je podana in jih vrne v slovarju"""
    vzorec_rojstva = re.compile(r"<li>.*?(?P<rojstvo>\d{1,4}(_BC)?).*?&#8211", re.DOTALL)
    vzorec_imena = re.compile(r'(&#8211;|–).*?<a href="\/wiki\/.*?" title=".*?">(?P<ime>[^"]*?)<\/a>', re.DOTALL)
    vzorec_naziva = re.compile(r"\D\D\D\D\D<\/a>,? (<a.*?>)?(?P<naziv1>.*?) ?(((<\/a>.*?<a.*?>)|(<a.*?>)(?P<naziv2>.*?)))?(\(d. (.*?)?|<)", re.DOTALL)
    vzorec_smrti = re.compile(r"<li>.*?\(d. (?P<smrt>\d{1,4}( BC)?)\)<\/li>", re.DOTALL)

    najdeno_rojstvo = vzorec_rojstva.search(blok_rojstev)
    najdeno_ime = vzorec_imena.search(blok_rojstev)
    najdeno_naziv = vzorec_naziva.search(blok_rojstev)
    najdeno_smrt = vzorec_smrti.search(blok_rojstev)

    slovar = {}
    slovar.setdefault("ime", None)
    if najdeno_ime != None:
        slovar["ime"] = najdeno_ime["ime"]
    slovar.setdefault("naziv", None)
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

    slovar.pop("naziv2")
    return slovar 

#print(zberi_osebe_rojstvo('<li><a href="/wiki/1311" title="1311">1311</a> &#8211; <a href="/wiki/Liu_Bowen" title="Liu Bowen">Liu Bowen</a>, Chinese military strategist, statesman and poet (d. 1375)</li>'))
# print(poisci_rojstva(html("https://en.wikipedia.org/wiki/July_1")))
#print(zberi_osebe_rojstvo(poisci_podatke(poisci_rojstva(html("https://en.wikipedia.org/wiki/July_1")))))

def zberi_osebe_smrt(blok_smrti: list):
    """iz bloka smrti razdeli podatke na ime, naziv, rojstvo in smrt, če je podana in jih vrne v slovarju"""
    vzorec_smrti = re.compile(r"<li>.*?(?P<smrt>\d{1,4}(_BC)?).*?&#8211", re.DOTALL)
    vzorec_imena = re.compile(r'(&#8211;|–).*?<a href="\/wiki\/.*?" title=".*?">(?P<ime>.*?)<\/a>', re.DOTALL)
    vzorec_naziva = re.compile(r"\D\D\D\D\D<\/a>,? (<a.*?>)?(?P<naziv1>.*?) ?(((<\/a>.*?<a.*?>)|(<a.*?>)(?P<naziv2>.*?)))?(\(b. (.*?)?|<)", re.DOTALL)
    vzorec_rojstva = re.compile(r"<li>.*?\(b. (c. )?(?P<rojstvo>\d{1,4}( BC)?)\)?.*?<\/li>", re.DOTALL)

    #for blok in bloki_smrti:
    najdeno_ime = vzorec_imena.search(blok_smrti)
    najdeno_naziv = vzorec_naziva.search(blok_smrti)
    najdeno_rojstvo = vzorec_rojstva.search(blok_smrti)
    najdeno_smrt = vzorec_smrti.search(blok_smrti)
    
    #print(najdeno_ime)
    #print(najdeno_rojstvo)
    #print(najdeno_smrt)
    #print(najdeno_smrt["smrt"])

    slovar = {}
    slovar.setdefault("ime", None)
    if najdeno_ime != None:
        slovar["ime"] = najdeno_ime["ime"]
    slovar.setdefault("naziv", None)
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

    slovar.pop("naziv2")
    return slovar
#print(zberi_osebe_smrt(poisci_podatke(poisci_smrti(html("https://en.wikipedia.org/wiki/July_1")))))
#print(poisci_podatke(poisci_smrti(html("https://en.wikipedia.org/wiki/July_1"))))

#bloki = poisci_podatke(poisci_rojstva(html("https://en.wikipedia.org/wiki/January_1")))
#for blok in bloki:
#    print(zberi_osebe_rojstvo(blok))


#popravi/odstrani nepotrebne narekovaje

#narekovaji = """<li><a href="/wiki/1774" title="1774">1774</a> &#8211; <a href="/wiki/Henry_Fox,_1st_Baron_Holland" title="Henry Fox, 1st Baron Holland">Henry Fox, 1st Baron Holland</a>, English politician, <a href="/wiki/Secretary_of_State_for_the_Southern_Department" title="Secretary of State for the Southern Department">Secretary of State for the Southern Department</a> (b. 1705)</li>
#<li><a href="/wiki/1782" title="1782">1782</a> &#8211; <a href="/wiki/Charles_Watson-Wentworth,_2nd_Marquess_of_Rockingham" title="Charles Watson-Wentworth, 2nd Marquess of Rockingham">Charles Watson-Wentworth, 2nd Marquess of Rockingham</a>, English politician, <a href="/wiki/Prime_Minister_of_Great_Britain" class="mw-redirect" title="Prime Minister of Great Britain">Prime Minister of Great Britain</a> (b. 1730)<sup id="cite_ref-76" class="reference"><a href="#cite_note-76">&#91;76&#93;</a></sup></li>"""
#print(zberi_osebe_smrt(narekovaji))

#poskus = '''<li><a href="/wiki/1766" title="1766">1766</a> – <a href="/wiki/James_Francis_Edward_Stuart" title="James Francis Edward Stuart">James Francis Edward Stuart</a>, Jacobite pretender (b. 1688)<sup 
#<li><a href="/wiki/1780" title="1780">1780</a> &#8211; <a href="/wiki/Johann_Ludwig_Krebs" title="Johann Ludwig Krebs">Johann Ludwig Krebs</a>, German organist and composer (b. 1713)<sup id="cite_ref-383" class="reference"><a href="#cite_note-383">&#91;383&#93;</a></sup></li>
#<li><a href="/wiki/1782" title="1782">1782</a> &#8211; <a href="/wiki/Johann_Christian_Bach" title="Johann Christian Bach">Johann Christian Bach</a>, German composer (b. 1735)<sup id="cite_ref-384" class="reference"><a href="#cite_note-384">&#91;384&#93;</a></sup></li>
#<li><a href="/wiki/1789" title="1789">1789</a> &#8211; <a href="/wiki/Fletcher_Norton,_1st_Baron_Grantley" title="Fletcher Norton, 1st Baron Grantley">Fletcher Norton, 1st Baron Grantley</a>, English lawyer and politician, <a href="/wiki/Speaker_of_the_House_of_Commons_(United_Kingdom)" title="Speaker of the House of Commons (United Kingdom)">British Speaker of the House of Commons</a> (b. 1716)<sup id="cite_ref-385" class="reference"><a href="#cite_note-385">&#91;385&#93;</a></sup></li>'''
#
#zberi_osebe_smrt(poskus)

