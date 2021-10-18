def PrintMenu():
    print("1.Citeste lista")
    print("2.Afiseaza numere intregi din l")
    print("3.Afiseaza cel mai mare numar divizibil cu k")
    print("4.Afiseaza numerele care au partea fractionara palindrom")
    print("5.")
    print("x.Iesire")


"""
def get_base_10_from_2(n):
rez = 0
p = 1
while n:
rez = rez + p * (n%10)
p *= 2
n //= 10
return rez


def get_base_16_from_2(n):
rez = ""
n_in_base10 = get_base_10_from_2(n)
while n_in_base10:
if n_in_base10 % 16 == 15:
rez = rez + "F"
elif n_in_base10 % 16 == 14:
rez = rez + "E"
elif n_in_base10 % 16 == 13:
rez = rez + "D"
elif n_in_base10 % 16 == 12:
rez = rez + "C"
elif n_in_base10 % 16 == 11:
rez = rez + "B"
elif n_in_base10 % 16 == 10:
rez = rez + "A"
elif n_in_base10 % 16 <= 9:
for x in range(10):
if n_in_base10 % 16 == x:
rez = rez + str(x)
break
n_in_base10 //= 16
return rez[::-1]
"""

def CitireLista():
    l = []
    n = int(input("Dati numarul de elemente din lista: "))
    for i in range(n):
        l.append(float(input("l[" + str(i) + "]=")))
    return l


def NumereIntregi(l):
    """
    Determina numerele intregi din l
    :param l lista de numere float:
    :nu returneaza:
    """
    k = []
    for x in l:
        if x == int(x):
            k.append(x)
    return k


def test_NumereIntregi():
    assert NumereIntregi([78.3, 63, 3, 45, 6.0]) == [63, 3, 45, 6]
    assert NumereIntregi([34.34, 27, 89]) == [27, 89]


test_NumereIntregi()


def MaxDivK(l, j):
    """
    Determina cel mai mare numar divizibil cu k din lista
    :param l lista de numere:
    :return cel mai mare numar divizibil cu k:
    """
    maxim = None
    for x in l:
        if (maxim == None) or (x > maxim and x % j == 0):
            maxim = x
    return maxim


def test_MaxDivK():
    assert MaxDivK([6, 36, 18.03, 48.05], 6) == 36
    assert MaxDivK([25, 50, 75.58, 48.05], 5) == 50


test_MaxDivK()


def is_palindrome(n):
    '''
    Determina daca un numar este palindrom sau nu
    :param n numar intreg:
    :return True daca n este palindrom sau False daca nu:
    '''
    auxiliar = int(n)
    k = 0
    while auxiliar > 0:
        k = k * 10 + auxiliar % 10
        auxiliar = auxiliar // 10
    if n == k:
        return True
    else:
        return False


def test_is_palindrome():
    assert is_palindrome(189) is False
    assert is_palindrome(18981) is True
    assert is_palindrome(72) is False


test_is_palindrome()


def ParteFractionaraPalindrom(l):
    """
    Determina daca partea fractionara a unui numar este palindrom
    :param l lista de numere de tip float:
    :return lista cu numerele care au partea fractionara palindrom:
    """
    h = []
    for x in l:
        if x!=int(x):
            k = str(x)
            j = int((k.split(".")[1]))
            if is_palindrome(j) is True:
                h.append(x)
        else:
            h.append(x)
    return h


def test_ParteFractionaraPalindrom():
    assert ParteFractionaraPalindrom([37.81, 213.1426]) == []
    assert ParteFractionaraPalindrom([0.88788, 90.38983,4, 7.382]) == [0.88788, 90.38983,4]


test_ParteFractionaraPalindrom()


def main():
    while True:
        PrintMenu()
        optiune = input("Dati optiunea ")
        if optiune == "1":
            l = CitireLista()
        elif optiune == "2":
            l1 = NumereIntregi(l)
            print(l1[:])
        elif optiune == "3":
            j = int(input("Introduceti divizorul k "))
            x = MaxDivK(l, j)
            print(x)
        elif optiune == "4":
            l2 = ParteFractionaraPalindrom(l)
            print(l2[:])
        elif optiune == "5":
            break
        elif optiune == "x":
            break


main()
