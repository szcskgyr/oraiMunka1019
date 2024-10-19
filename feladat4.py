def negy():
    n=1
    k=1
    if (k % 2 == 1) and (n > 0) and (pow(2, n) > k):
        # jó eset
        print("Proth számok: ", end="")
        for n in range(10):
            proth = (k * pow(2, n)) + 1
            print(str(proth) + ", ", end="")
        proth = (k * pow(2, 10)) + 1
        print(str(proth))
    else:
        print("HIBA: nem megfelelő számok!")

def negyB():
    n=0
    k=0
    print("Proth számok: ", end="")
    szamlalo = 0
    while szamlalo < 10:
        if (k % 2 == 1) and (n > 0) and (pow(2, n) > k):
            proth = (k * pow(2, n)) + 1
            print(str(proth) + ", ", end="")
            szamlalo += 1
        else:
            pass
            # print("HIBA: nem megfelelő számok!")
        n += 1
        k += 1
    proth = (k * pow(2, n)) + 1
    print(str(proth))