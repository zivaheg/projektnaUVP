from preberi_bloke import *



def zberi_bitke(blok_dogodka):
    """Iz dogodka izlušči samo bitko ali vojno."""
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



def zberi_osebe_rojstvo(blok_rojstev):
    """Iz bloka rojstva razdeli podatke na ime, naziv, rojstvo in smrt, če je podana in jih vrne v slovarju."""
    vzorec_rojstva = re.compile(r"<li>.*?(?P<rojstvo>\d{1,4}(_BC)?).*?&#8211", re.DOTALL)
    vzorec_imena = re.compile(r'(&#8211;|–).*?<a href=\"\/wiki\/.*?\" title=\".*?\">(?P<ime>[^#]*?)<\/a>', re.DOTALL)
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



def zberi_osebe_smrt(blok_smrti: list):
    """Iz bloka smrti razdeli podatke na ime, naziv, rojstvo in smrt, če je podana in jih vrne v slovarju."""
    vzorec_smrti = re.compile(r"<li>.*?(?P<smrt>\d{1,4}(_BC)?).*?&#8211", re.DOTALL)
    vzorec_imena = re.compile(r'(&#8211;|–).*?<a href="\/wiki\/.*?" title=".*?">(?P<ime>[^#]*?)<\/a>', re.DOTALL)
    vzorec_naziva = re.compile(r"\D\D\D\D\D<\/a>,? (<a.*?>)?(?P<naziv1>.*?) ?(((<\/a>.*?<a.*?>)|(<a.*?>)(?P<naziv2>.*?)))?(\(b. (.*?)?|<)", re.DOTALL)
    vzorec_rojstva = re.compile(r"<li>.*?\(b. (c. )?(?P<rojstvo>\d{1,4}( BC)?)\)?.*?<\/li>", re.DOTALL)

    najdeno_ime = vzorec_imena.search(blok_smrti)
    najdeno_naziv = vzorec_naziva.search(blok_smrti)
    najdeno_rojstvo = vzorec_rojstva.search(blok_smrti)
    najdeno_smrt = vzorec_smrti.search(blok_smrti)

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

