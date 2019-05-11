def zarojelek_ellenorzese(sor):
    cnt = 0
    for c in sor:
        if c == '(':
            cnt += 1
        if c == ')':
            cnt -= 1
            if cnt < 0:
                return False
            #
    # endfor
    return cnt == 0


def elemez(sor):
    zarojek = zarojelek_ellenorzese(sor)
    if zarojek == False:
        return False
    #
    if (not sor.endswith("')")) and (not sor.endswith("');")):
        return False

    if not sor.startswith("if("):
        return False

    if "):" not in sor:
        return False

    if ":print('" not in sor:
        return False

    poz1 = sor.find("print(") + 5
    poz2 = sor.rfind(")")
    belul = sor[poz1+1:poz2]
    if not (len(belul) >= 2 and belul[0] == "'" and belul[-1] == "'"):
        return False

    # ha minden ellenorzesen atment a sor
    return True


def main():
    sor = "if(a<b):print('hello');"
    eredmeny = elemez(sor)

    print(eredmeny)

#############################################################################

main()



