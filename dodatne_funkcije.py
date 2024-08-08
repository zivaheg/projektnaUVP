

def nastavi_html():
    """vrne seznam vseh dni v letu"""
    meseci = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    krajsi_mesci = ["April", "June", "September", "November"]
    dnevi = []
    for mesec in meseci:
        for dan in range(1,32):
            dan_info = []
            if mesec == "February":
                if dan > 29:
                    continue
                    #url = (f"https://en.wikipedia.org/wiki/{mesec}_{dan}")
            if mesec in krajsi_mesci and dan == 31: 
                continue    
                    #url = (f"https://en.wikipedia.org/wiki/{mesec}_{dan}")
            url = (f"https://en.wikipedia.org/wiki/{mesec}_{dan}")
            dan_info.append(dan)
            dan_info.append(mesec)
            dan_info.append(url)
            dnevi.append(dan_info)
    return dnevi

#vse_html_strani = nastavi_html()
#print(vse_html_strani)

def csv_oseb_po_dnevih():
    """vrne url naslove vseh dni v letu"""
    meseci = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    krajsi_mesci = ["April", "June", "September", "November"]
    vsi_html = []
    for mesec in meseci:
        for dan in range(1,32):
            if mesec == "February":
                if dan <= 29:
                    continue
            if mesec in krajsi_mesci:
                if dan < 31:     
                    vsi_html.append(f"https://en.wikipedia.org/wiki/{mesec}_{dan}")
            vsi_html.append(f"https://en.wikipedia.org/wiki/{mesec}_{dan}")
    return vsi_html


def funkcija_zivljenske_dobe(rojstvo, smrt):
    """izračuna življensko dobo"""
    if "BC" in rojstvo and "BC" not in smrt:
        return int(rojstvo[:-3]) + int(smrt)
    elif "BC" in rojstvo and "BC" in smrt:
        return int(rojstvo[:-3]) - int(smrt[:-3])
    else:
        return int(smrt) - int(rojstvo)

def letnice_pred_0(letnica):
    if letnica != None:
        if "BC" in letnica:
            return int(letnica[:-3]) * (-1)
        else:
            return int(letnica)
    else:
        return None



def prevedi_mesec(mesec_anglesko):
    """prevede mesec v angleščini v mesec v slovenščini"""
    if mesec_anglesko == "January":
        return "Januar"
    elif mesec_anglesko == "February":
        return "Februar"
    elif mesec_anglesko == "March":
        return "Marc"
    elif mesec_anglesko == "May":
        return "Maj"
    elif mesec_anglesko == "June":
        return "Junij"
    elif mesec_anglesko == "July":
        return "Julij"
    elif mesec_anglesko == "October":
        return "Oktober"
    else:
        return mesec_anglesko

