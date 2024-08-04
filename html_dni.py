
meseci = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
krajsi_mesci = ["April", "June", "September", "November"]

def nastavi_html():
    vsi_html = []
    for mesec in meseci:
        for dan in range(1,32):
            if mesec == "February":
                if dan < 29:
                    vsi_html.append(f"https://en.wikipedia.org/wiki/{mesec}_{dan}")
            if mesec in krajsi_mesci:
                if dan < 31:     
                    vsi_html.append(f"https://en.wikipedia.org/wiki/{mesec}_{dan}")
            vsi_html.append(f"https://en.wikipedia.org/wiki/{mesec}_{dan}")
    return vsi_html

vse_html_strani = nastavi_html()
#print(vse_html_strani)