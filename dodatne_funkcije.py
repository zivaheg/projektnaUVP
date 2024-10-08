


def nastavi_html():
    """Vrne seznam vseh dni v letu."""
    meseci = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    krajsi_mesci = ["April", "June", "September", "November"]
    dnevi = []
    for mesec in meseci:
        for dan in range(1,32):
            dan_info = []
            if mesec == "February":
                if dan > 29:
                    continue

            if mesec in krajsi_mesci and dan == 31: 
                continue

            url = (f"https://en.wikipedia.org/wiki/{mesec}_{dan}")
            dan_info.append(dan)
            dan_info.append(mesec)
            dan_info.append(url)
            dnevi.append(dan_info)
    return dnevi



def csv_oseb_po_dnevih():
    """Vrne url naslove vseh dni v letu."""
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
    """Izračuna življensko dobo."""
    if "BC" in rojstvo and "BC" not in smrt:
        return int(rojstvo[:-3]) + int(smrt)
    elif "BC" in rojstvo and "BC" in smrt:
        return int(rojstvo[:-3]) - int(smrt[:-3])
    else:
        return int(smrt) - int(rojstvo)



def letnice_pred_0(letnica):
    """Letnice pred našim štetjem zapiše kot negativne."""
    if letnica != None:
        if "BC" in letnica:
            return int(letnica[:-3]) * (-1)
        else:
            return int(letnica)
    else:
        return None



def prevedi_mesec(mesec_anglesko):
    """Prevede mesec v angleščini v mesec v slovenščini."""
    if mesec_anglesko == "January":
        return "januar"
    elif mesec_anglesko == "February":
        return "februar"
    elif mesec_anglesko == "March":
        return "marc"
    elif mesec_anglesko == "April":
        return "april"
    elif mesec_anglesko == "May":
        return "maj"
    elif mesec_anglesko == "June":
        return "junij"
    elif mesec_anglesko == "July":
        return "julij"
    elif mesec_anglesko == "August":
        return "avgust"
    elif mesec_anglesko == "September":
        return "september"
    elif mesec_anglesko == "October":
        return "oktober"
    elif mesec_anglesko == "November":
        return "november"
    else:
        return "december"

