def ketto():
    szam = int(input("Adj meg egy háromjegyű, 5-tel osztható számot! "))

    if (((szam > 99) and (szam < 1000)) or ((szam < -99) and (szam > -1000))) and (szam%5==0):
        # jó
        print("A megadott szám négyzete: "+str(szam**2))
    else:
        # rossz
        print("HIBA: nem megfelelő szám!")
