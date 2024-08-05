import re
import requests


#zaenkrat potujemo samo po 1.7. 

def html(url_link):
    """poišče html, podane spletne strani in ga vrne kot niz"""
    html = requests.get(url_link)
    return html.text


#poskus = html(https://en.wikipedia.org/wiki/January_1)
#html("https://en.wikipedia.org/wiki/July_1")
#print(poskus)

def poisci_dogodke(niz: str):
    """iz podanega html izlušči blok dogodkov"""
    vzorec = r'<div class="mw-heading mw-heading2"><h2 id="Events">Events</h2>.*?<div class="mw-heading mw-heading2"><h2 id="Births">Births</h2>'
    vse_pojavitve = re.findall(vzorec, niz, flags=re.DOTALL)
    return vse_pojavitve[0]

#print(len(poisci_dogodke(html("https://en.wikipedia.org/wiki/July_1"))))

def poisci_rojstva(niz: str):
    """iz podanega html izlušči blok rojstev"""
    vzorec = r'<div class="mw-heading mw-heading2"><h2 id="Births">Births</h2>.*?<div class="mw-heading mw-heading2"><h2 id="Deaths">Deaths</h2>'
    vse_pojavitve = re.findall(vzorec, niz, flags=re.DOTALL)
    return vse_pojavitve[0]

#print(len(poisci_rojstva(html("https://en.wikipedia.org/wiki/July_1"))))

def poisci_smrti(niz: str):
    """iz podanega html izlušči blok smrti"""
    vzorec = r'<div class="mw-heading mw-heading2"><h2 id="Deaths">Deaths</h2>.*?<div class="mw-heading mw-heading2"><h2 id="Holidays_and_observances">Holidays and observances</h2>'
    vse_pojavitve = re.findall(vzorec, niz, flags=re.DOTALL)
    return vse_pojavitve[0]

#print(len(poisci_smrti(html("https://en.wikipedia.org/wiki/July_1"))))



def poisci_praznike(niz: str):
    """iz podanega html izlušči blok praznikov"""
    vzorec = r'<div class="mw-heading mw-heading2"><h2 id="Holidays_and_observances">Holidays and observances</h2>.*?<div class="mw-heading mw-heading2"><h2 id="References">References</h2>'
    vse_pojavitve = re.findall(vzorec, niz, flags=re.DOTALL)
    return vse_pojavitve[0]

def prazniki(blok: list):
    #kodo ki radeli na posamezne dneve svetnikov, ne upošteva zadnje alineje in normalno šteje stvari naprej
    return None

#print(len(poisci_praznike(html("https://en.wikipedia.org/wiki/July_1"))))

def poisci_podatke(blok: list):
    """iz podanega bloka poišče podatke"""
    vzorec = r'<li>.*?</li>'
    return re.findall(vzorec, blok, flags=re.DOTALL)


#print(len(poisci_podatke(poisci_dogodke(html("https://en.wikipedia.org/wiki/July_1")))))
#print(len(poisci_podatke(poisci_rojstva(html("https://en.wikipedia.org/wiki/July_1")))))
#print(len(poisci_podatke(poisci_smrti(html("https://en.wikipedia.org/wiki/July_1")))))
##print(len(poisci_podatke(poisci_praznike(html("https://en.wikipedia.org/wiki/July_1")))))





    




