# Stepit:
# 1. Create a basic application that can ask multiple-choice questions.
# 2. Separate question data from source code by storing questions in a dedicated data file.
# 3. Refactor the code to use functions.
# 4. Add interest by supporting different quiz topics to choose from.
# 5. Expand the app to give hints, and provide explanations.
# 6. Make the app more user-friendly by improving how it looks and how it handles user errors.

# Quiz

kysymykset = ("Mikä on maailman syvin kohta?: ",
              "Mikä on maailman pienin valtio?: ",
              "Mikä on maailman pisin joki?: ",
              "Mikä on Perun pääkaupunki?: ",
              "Mikä on maailman suurin järvi?: ")

vaihtoehdot = (("A. Mt. Everest", "B. Mariaanien hauta", "C. Kuollut meri", "D. Tongan hauta"),
               ("A. San Marino", "B. Liechenstain", "C. Tonga", "D. Vatikaani"),
               ("A. Niili", "B. Amazon", "C. Inn", "D. Kemijoki"),
               ("A. Lima", "B. Peru", "C. Cusco", "D. Pisco"),
               ("A. Michiganjärvi", "B. Eriejärvi", "C. Iso Karhujärvi", "D. Kaspianmeri"))

vastaukset = ("B", "D", "A", "A", "D")

nimi = input("Anna nimesi: ")


def uusi_peli():
    arvaukset = []
    tulos = 0
    kysymys_numero = 0

    for kysymys in kysymykset:
        print("-" * len(kysymys))
        print(kysymys)
        for vaihtoehto in vaihtoehdot[kysymys_numero]:
            print(vaihtoehto)

        arvaus = input("Anna oikea vaihtoehto: ").upper()
        arvaukset.append(arvaus)
        if arvaus == vastaukset[kysymys_numero]:
            tulos += 1
            print("Oikein!")
        else:
            print("Väärin...")
            # print(f"Oikea vastaus on {vastaukset[kysymys_numero]}")
        kysymys_numero += 1
    # nayta_tulokset()


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
