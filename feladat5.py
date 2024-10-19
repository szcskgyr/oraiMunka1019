import math

def ot():
    #  Kérj be egy [40, 95] intervallumban lévő egész számot (ha nem ebben az intervallumban van, jelezz hibát!), majd írasd ki az első számjegyét!
    szam = int(input("Adj meg egy egész számot!"))
    if szam < 40 or szam > 95:
        print("HIBA: nem megfelelő szám!")
    else:
        # megoldás1
        szam = str(szam)
        print(szam[0])

        # megoldás2
        print(str(int(int(szam)/10)))

        # megoldás3
        print(str(math.floor(int(szam)/10)))