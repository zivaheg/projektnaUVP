

def nastavi_html():
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