import re
import requests



def html(url_link):
    """Poišče html, podane spletne strani in ga vrne kot niz."""
    html = requests.get(url_link)
    return html.text



def poisci_dogodke(niz: str):
    """Iz podanega html izlušči blok dogodkov."""
    vzorec = r'<div class="mw-heading mw-heading2"><h2 id="Events">Events</h2>.*?<div class="mw-heading mw-heading2"><h2 id="Births">Births</h2>'
    vse_pojavitve = re.findall(vzorec, niz, flags=re.DOTALL)
    return vse_pojavitve[0]



def poisci_rojstva(niz: str):
    """Iz podanega html izlušči blok rojstev."""
    vzorec = r'<div class="mw-heading mw-heading2"><h2 id="Births">Births</h2>.*?<div class="mw-heading mw-heading2"><h2 id="Deaths">Deaths</h2>'
    vse_pojavitve = re.findall(vzorec, niz, flags=re.DOTALL)
    return vse_pojavitve[0]



def poisci_smrti(niz: str):
    """Iz podanega html izlušči blok smrti."""
    vzorec = r'<div class="mw-heading mw-heading2"><h2 id="Deaths">Deaths</h2>.*?<div class="mw-heading mw-heading2"><h2 id="Holidays_and_observances">Holidays and observances</h2>'
    vse_pojavitve = re.findall(vzorec, niz, flags=re.DOTALL)
    return vse_pojavitve[0]



def poisci_podatke(blok: list):
    """Iz podanega bloka poišče podatke."""
    vzorec = r'<li>.*?</li>'
    return re.findall(vzorec, blok, flags=re.DOTALL)







    




