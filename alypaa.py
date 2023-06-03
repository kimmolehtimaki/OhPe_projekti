# Stepit:
# 1. Create a basic application that can ask multiple-choice questions.
# 2. Separate question data from source code by storing questions in a dedicated data file.
# 3. Refactor the code to use functions.
# 4. Add interest by supporting different quiz topics to choose from.
# 5. Expand the app to give hints, and provide explanations.
# 6. Make the app more user-friendly by improving how it looks and how it handles user errors.

# Quiz

nimi = input("Anna nimesi: ")


def uusi_peli():
    arvaukset = []
    tulos = 0
    kysymys_numero = 0

    with open("maantieto.csv") as tiedosto:

        for rivi in tiedosto:
            rivi = rivi.replace("\n", "")
            osat = rivi.split(";")
            kysymys = osat[0]
            vaihtoehdot = osat[1:5]
            print("----------------")
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


print()


"""def nayta_tulokset():
    taulu = nayta_tulokset(nimi)
    tulos2 = int(tulos / len(kysymykset))/100
    print("****************************************")
    print(taulu)
    print("Tuloksesi on: " + "?" + " / " + str(len(kysymykset)))
    print(tulos2 + "%")"""


def pelaa_uudelleen():
    valinta = input("Haluatko pelata uudelleen? (kyllä/ei): ")
    valinta = valinta.upper()

    if valinta == "KYLLÄ":
        return True
    else:
        return False


uusi_peli()

while pelaa_uudelleen():
    uusi_peli()

print("Kiitos, moi!")