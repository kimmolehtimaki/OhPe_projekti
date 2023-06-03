def uusi_peli():
    arvaukset = []
    tulos = 0
    kysymys_numero = 0

    with open("maantieto.csv") as tiedosto:

        for rivi in tiedosto:
            rivi = rivi.replace("\n", "")
            osat = rivi.split(";")
            kysymys = osat[0]
            vaihtoehdot = osat[1:4]
            print(kysymys)
            print(vaihtoehdot)
        arvaus = input("Anna oikea vaihtoehto: ").upper()
        arvaukset.append(arvaus)

        if arvaus == osat[5]:
            tulos += 1
            print("Oikein!")
        else:
            print("Väärin...")
            # print(f"Oikea vastaus on {vastaukset[kysymys_numero]}")
        kysymys_numero += 1


uusi_peli()
