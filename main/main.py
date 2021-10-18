def PrintMenu():
    print("1.Citeste lista")
    print("2.Elimina numere prime din lista")
    print("3.Afisati daca media aritmetica a numerelor este mai mare decat n")
    print("4.Adauga la lista numarul de divizori proprii ai elementului")
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
    h = []
    for x in l:
        if NrPrim(x) is False:
            h.append(x)
    return h


def test_ListaFaraPrim():
    assert ListaFaraPrim([5, 6, 7, 8, 9]) == [6, 8, 9]
    assert ListaFaraPrim([17, 20, 21, 28, 29]) == [20, 21, 28]
    assert ListaFaraPrim([7, 11, 13]) == []


test_ListaFaraPrim()


def MediaAritmetican(l, n):
    """
    Determina daca media aritmetica a numerelor din lista l este mai mare decat n
    :param l lista de numere:
    :param n numarul cu care se compara media aritmetica a elementelor din lista:
    :return True sau false:
    """
    s = 0
    for x in l:
        s = s + x
    if s // len(l) > n:
        return True
    return False


def test_MediaAritmetican():
    assert MediaAritmetican([10, -3, 25, -1, 3, 25, 18], 10) is True
    assert MediaAritmetican([10, -3, 25, -1, 3, 25, 18], 12) is False
    assert MediaAritmetican([1, 2, 3, 4, 5], 10) is False


test_MediaAritmetican()


def AdaugaDivizori(l):
    """
    Adauga dupa fiecare element al listei numarul de divizori al sau
    :param l lista de numere intregi:
    :return o lista cu numerele urmate de cati divizori au fiecare:
    """
    k = []
    for x in l:
        k.append(x)
        c = 0
        for i in range(2, x // 2 + 1):
            if x % i == 0:
                c = c + 1
        k.append(c)
    return k


def test_AdaugaDivizori():
    assert AdaugaDivizori([19, 5, 24, 12, 9]) == [19, 0, 5, 0, 24, 6, 12, 4, 9, 1]
    assert AdaugaDivizori([3, 5, 7]) == [3, 0, 5, 0, 7, 0]
    assert AdaugaDivizori([10, 13, 17, 20]) == [10, 2, 13, 0, 17, 0, 20, 4]


test_AdaugaDivizori()


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
            n = int(input("Dati numarul n "))
            if MediaAritmetican(l, n) is True:
                print("DA")
            else:
                print("NU")
        elif optiune == "4":
            l2 = AdaugaDivizori(l)
            print(l2[:])
        elif optiune == "5":
            break
        elif optiune == "x":
            break


main()
