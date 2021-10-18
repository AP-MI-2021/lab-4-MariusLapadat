def PrintMenu():
    print("1.Citeste lista")
    print("2.Elimina numere prime din lista")
    print("3.")
    print("4.")
    print("5.")
    print("x.Iesire")


def CitireLista():
    l = []
    n = int(input("Dati numarul de elemente din lista: "))
    for i in range(n):
        l.append(int(input("l[" + str(i) + "]=")))
    return l


def NrPrim(n):
    '''
    Functia determina daca un numar este prim sau nu
    :param n numar intreg:
    :return adevarat sau fals:
    '''
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def test_NrPrim():
    assert NrPrim(7) is True
    assert NrPrim(10) is False
    assert NrPrim(5) is True


test_NrPrim()


def ListaFaraPrim(l):
    """
    Returneaza o lista fara numere prime
    :param l lista de numere intregi:
    :return o lista fara numerele prime:
    """
    h=[]
    for x in l:
        if NrPrim(x) is False:
            h.append(x)
    return h


def test_ListaFaraPrim():
    assert ListaFaraPrim([5,6,7,8,9]) == [6,8,9]
    assert ListaFaraPrim([17,20,21,28,29]) == [20,21,28]
    assert ListaFaraPrim([7,11,13]) == []

test_ListaFaraPrim()

def main():
    while True:
        PrintMenu()
        optiune = input("Dati optiunea ")
        if optiune == "1":
            l = CitireLista()
        elif optiune == "2":
            l1 = ListaFaraPrim(l)
            print(l1[:])
        elif optiune == "3":
            break
        elif optiune == "4":
            break
        elif optiune == "5":
            break
        elif optiune == "x":
            break


main()
