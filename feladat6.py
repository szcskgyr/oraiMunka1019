def tortSzamBeolvas(szoveg):
    szam = float(input(szoveg))
    return szam

def hat():
    a = tortSzamBeolvas("Adja meg a háromszög első oldalát! ")
    b = tortSzamBeolvas("Adja meg a háromszög második oldalát! ")
    c = tortSzamBeolvas("Adja meg a háromszög harmadik oldalát! ")
    if a > 0 and b > 0 and c > 0:
        if (a<b+c) and (b<a+c) and (c<a+b):
            print("A háromszög megszerkeszthető")
        else:
            print("A háromszög nem megszerkeszthető")
    else:
        print("HIBA: nem megfelelő bemenő adatok!")