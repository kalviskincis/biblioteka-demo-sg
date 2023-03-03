def personas_kods(pk) -> str:
    """ 
    jābūt 12 zīmes garam, 7. zīme -, pārējās skaitļi   
    """
    atbilst = False
    if len(pk) == 12 and pk[6] == "-":
        pk_sak = pk[0:6]
        pk_beig = pk[7:]
        if pk_sak.isdigit() and pk_beig.isdigit():
            atbilst = True

    return atbilst

def talrunis(nr) -> str:
    """
    Jābūt 8 zīmes garam, satur skaitļus, nesākas ar 0
    Ja ievadīts ar atstarpēm
    """
    atbilst = False
    nr = nr.replace(" ","")
    if len(nr) == 8 and nr.isdigit() and nr[0] != "0":
        atbilst = True

    return atbilst

def teksts(virkne) -> str:
    """
    Pārbaude, vai simbolu virknes tajās vietās, kur visu jāazipilda, ir ierakstītas,
    t.i., to garums lielāks par 0
    """
    atbilst = False
    if len(virkne) > 0:
        atbilst = True

    return atbilst
