import math

#1
def zadanie1() -> int:
    with open("TXT/slowa.txt", "r") as plik:
        f = plik.readlines()
        total = 0
        for slowo in f:
            if list(slowo).count("a") > 3:
                total += 1
    return total

#2
def zadanie2() -> list[int]:
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
        return p

#3
def zadanie3() -> int:
    bitek = "wfnjsdneinvrefmemcicmiircedjnddjjmxsxwp"
    bajtek = "anhnfdiacidmcdmcodcpmwsicmwdimcwmic"
    lvl_podobienstwa = 0
    for i in range(0, len(bitek) - 1):
        for j in range(0, len(bajtek) - 1):
            if bajtek[j] == bitek[i]:
                lvl_podobienstwa += 1
    return lvl_podobienstwa

#4
def zadanie4() -> int:
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
    return m(578)

#5
def zadanie5() -> int:
    curr = 0
    calosc = 0
    while curr + 13 < 1000:
        curr += 13
        calosc += curr
    return calosc

#6
def zadanie6() -> float:
    num = ((((49343-23343+46632)*8)-330)*16-19)/100
    result = num % 327327
    return result

#7
def zadanie7() -> str:
    a = 0.0001
    b = "Konik"
    c = 123*456+999-1000
    d = 'r'
    lista = [a,b,c,d]
    for k in lista:
        lista[lista.index(k)] = str(type(k))
    odp = ";".join(lista)
    return odp

#8
def zadanie8(a: int,b: int,c: int) -> str:
    delta = math.sqrt(b**2-4*a*c)
    if delta < 0:
        return "Funkcja nie ma rzeczywistych miejsc zerowych!"
    else:
        odp1 = (-1 * b + delta)/2*a
        odp2 = (-1 * b - delta)/2*a
        odp = [str(odp1),str(odp2)]
        return ";".join(odp)

#9
def zadanie9() -> str:
    with open("TXT/gwiazdki.txt", "r") as plik:
        f = plik.readlines()
        for i in range(0, len(f)):
            f[i] = f[i].split()
            if max(float(f[i][0])+10,float(f[i][1])**2) == float([i][0])+10:
                f[i] = f[i][0]
            else:
                f[i] = f[i][1]
        f = ";".join(f)
        return f

#10
def zadanie10(num: int) -> str:
    if num < 40:
        if num % 4 == 0:
            return "Jestem mała i dzielę się przez 4"
        else:
            return "Jestem mała i nie dzielę się przez 4"
    else:
        if num % 4 == 0:
            return "Jestem duża i dzielę się przez 4"
        else:
            return "Jestem duża i nie dzielę się przez 4"

#11
def zadanie11() -> str:
    with open("TXT/ile.txt", "r") as plik:
        f = plik.read().split()
        ile = [str(f.count(x)) for x in f]
        ile = ";".join(ile)
        return ile

#12
def zadanie12() -> list[str]:
    with open("TXT/te_same_cyfry.txt", "r", encoding="utf-8") as f:
        liczby = f.readlines()
        liczby = [liczba.strip() for liczba in liczby]
        liczby = [liczba for liczba in liczby if len(set(liczba)) == 1]
        return liczby
#13
def zadanie13(a: int, b: int) -> str:
    dzielniki = []
    for i in  range(1, max(a, b) + 1):
        if a % i == 0 and b % i == 0:
            dzielniki.append(str(i))
    return ";".join(dzielniki)

#14
def zadanie14() -> str:
    with open("TXT/3_liczby.txt", "r", encoding="utf-8") as f:
        liczby = f.readlines()
        liczby = [x.strip() for x in liczby]
        liczby = [x for x in liczby if len(x) > 0]
        for i,liczba in enumerate(liczby):
            match i:
                case 0:
                    liczby[i] = str(hex(int(liczba)))
                case 1:
                    liczby[i] = str(oct(int(liczba)))
                case 2:
                    liczby[i] = str(bin(int(liczba)))
        return ";".join(liczby)

#15
def zadanie15() -> str:
    with open("TXT/tablica.txt", "r", encoding="utf-8") as f:
        slowa = f.readline().split()
        for i,x in enumerate(slowa):
            if i == 0:
                slowa[i] = x.lower()
            elif i == 1:
                slowa[i] = x.upper()
            else:
                slowa[i] = x.swapcase()
        return ';'.join(slowa)

#16
def zadanie16() -> str:
    with open("TXT/wielkie_sprzatanie.txt", "r", encoding="utf-8") as f:
        zdania = f.readlines()
        zdania = [line.strip() for line in zdania]
        zdania = [line.split() for line in zdania]
        for j,line in enumerate(zdania):
            for i,x in enumerate(line):
                line[i] = x.lower()
                if i == 0 or i == 1:
                    line[i] = x.capitalize()
                else:
                    line[-1] = line[-1].replace("_", "")
            if len(line) == 3:
                zdania[j] = f"{line[0]}: {line[1]}, {line[2]}"
            else:
                zdania[j] = f"{line[0]}: {line[1]} {line[2]}, {line[3]}"
        return "\n".join(zdania)

#17
def zadanie17() -> str:
    with open("TXT/dane2.txt", "r", encoding="utf-8") as f:
        dziennik = f.readlines()
        srednia = []
        dziennik.pop(0)
        dziennik = [uczen.split() for uczen in dziennik]
        for uczen in dziennik:
            uczen.pop(0)
            uczen = [int(x) for x in uczen if x.strip().isdigit()]
            srednia.append(sum(uczen)/len(uczen))
        srednia = max(srednia)
        return f"{srednia:.2f}"

#18
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

#19
def zadanie19():
    with open("TXT/kolorowe_nawiasy.txt", "r", encoding="utf-8") as f:
        naszyjniki = f.readlines()
        naszyjniki.pop(0)
        naszyjniki = [x.strip().split() for x  in naszyjniki]
        
        return naszyjniki

def main():
    print(zadanie18())


if __name__ == "__main__":
    main()