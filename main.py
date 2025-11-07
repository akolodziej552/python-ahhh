import math
from operator import index


#zad 1
def zadanie1():
    with open("TXT/slowa.txt", "r") as plik:
        f = plik.readlines()
        total = 0
        for slowo in f:
            if list(slowo).count("a") > 3:
                total += 1
    print(total)

#zad 2
def zadanie2():
    with open("TXT/co_trzecia_parzysta.txt", "r") as plik:
        f = plik.read().split()
        p = []
        for x in f:
            try:
                n = int(x)
            except ValueError:
                continue
            if n % 2 == 0:
                p.append(n)
        p = [x for i, x in enumerate(p, start=1) if i % 3 != 0]
        print(p)

#3
def zadanie3():
    bitek = "wfnjsdneinvrefmemcicmiircedjnddjjmxsxwp"
    bajtek = "anhnfdiacidmcdmcodcpmwsicmwdimcwmic"
    lvl_podobienstwa = 0
    for i in range(0, len(bitek) - 1):
        for j in range(0, len(bajtek) - 1):
            if bajtek[j] == bitek[i]:
                lvl_podobienstwa += 1
    print(lvl_podobienstwa)

#4
def zdanie4():
    def s(num):
        total = 0
        for x in str(num):
            total += int(x)
        return total

    def m(l):
        if l <= 9:
            return 1
        else:
            return m(s(l)) + 1
    print(m(578))

#zad 5
def zadanie5():
    curr = 0
    calosc = 0
    while curr + 13 < 1000:
        curr += 13
        calosc += curr
    print(calosc)

#6
def zadanie6():
    num = ((((49343-23343+46632)*8)-330)*16-19)/100
    result = num % 327327
    print(result)

#7
def zadanie7():
    a = 0.0001
    b = "Konik"
    c = 123*456+999-1000
    d = 'r'
    lista = [a,b,c,d]
    for k in lista:
        lista[lista.index(k)] = str(type(k))
    odp = ";".join(lista)
    print(odp)

#8
def zadanie8(a,b,c):
    delta = math.sqrt(b**2-4*a*c)
    if delta < 0:
        print("Funkcja nie ma rzeczywistych miejsc zerowych!")
    else:
        odp1 = (-1 * b + delta)/2*a
        odp2 = (-1 * b - delta)/2*a
        odp = [str(odp1),str(odp2)]
        print(";".join(odp))

#9
def zdanie9():
    with open("TXT/gwiazdki.txt", "r") as plik:
        f = plik.readlines()
        for i in range(0, len(f)):
            f[i] = f[i].split()
            if max(float(f[i][0])+10,float(f[i][1])**2) == float([i][0])+10:
                f[i] = f[i][0]
            else:
                f[i] = f[i][1]
        f = ";".join(f)
        print(f)

#10
def zadanie10(num):
    if num < 40:
        if num % 4 == 0:
            print("Jestem mała i dzielę się przez 4")
        else:
            print("Jestem mała i nie dzielę się przez 4")
    else:
        if num % 4 == 0:
            print("Jestem duża i dzielę się przez 4")
        else:
            print("Jestem duża i nie dzielę się przez 4")

#11
def zadanie11():
    with open("TXT/ile.txt", "r") as plik:
        f = plik.read().split()
        ile = [str(f.count(x)) for x in f]
        ile = ";".join(ile)
        print(ile)

#12
def zadanie12():
    pass
#13
def zadanie13(num1,num2):
    wspolne_dziel = []
    for i in range(1,max(num1,num2)+1):
        if num1 % i == 0 and num2 % i == 0:
            wspolne_dziel.append(str(i))
    print(";".join(wspolne_dziel))

def zadanie18():
    with open("TXT/zapis.txt", "r", encoding="utf-8") as f:
        log = [x.strip().split() for x in f]
        total = 0
        for i, x in enumerate(log):
            if x[0] == "zatrudniam":
                imie = x[1]
                pensja = int(x[2])
                zwolnienie_index = 0
                for y in range(i + 1, len(log)):
                    if log[y][0] == "zwalniam" and log[y][1] == imie:
                        zwolnienie_index = y
                        break
            if not zwolnienie_index != 0:
                dni = zwolnienie_index - i + 1
            else:
                dni = len(log) - i
            total += dni * pensja
        return total

def zadanie19():
    with open("TXT/kolorowe_nawiasy.txt", "r", encoding="utf-8") as f:
        naszyjniki = f.readlines()
        naszyjniki.pop(0)
        naszyjniki = [x.strip().split() for x  in naszyjniki]
        
        return naszyjniki

def main():
    print(zadanie19())


if __name__ == "__main__":
    main()