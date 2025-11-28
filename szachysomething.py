def zadanie1(boards):
    total_pustych = 0
    maximum = 0
    for board in boards:
        total = 0
        for kolmn in range(8):
            pusta_kolumna = False
            for wiersz in range(8):
                if board[wiersz][kolmn] == ".":
                    pusta_kolumna = True
                else:
                    pusta_kolumna = False
                    break
            if pusta_kolumna:
                total += 1
        if total > 0:
            total_pustych += 1
            if total > maximum:
                maximum = total
    return f"{total_pustych} {maximum}"

def zadanie2(boards):
    min_rownowaga = 10000000
    ilosc_rownowaga = 0
    for board in boards:
        count = {}
        for x in board:
            for y in x:
                if y != ".":
                    if y not in count:
                        count[y] = 1
                    else:
                        count[y] += 1
        rownowaga = False
        for pion in count:
            if count.get(pion) == count.get(pion.swapcase()):
                rownowaga = True
            else:
                rownowaga = False
                break
        if rownowaga:
            ilosc_rownowaga += 1
            temp = 0
            for pion in count:
                temp += count[pion]
            if temp < min_rownowaga:
                min_rownowaga = temp
    return f"{ilosc_rownowaga} {min_rownowaga}"

def zadanie3(boards):
    bialy_szach = 0
    czarny_szach = 0
    for board in boards:
        for x in board:
            for y in x:
                if y.lower() == "w":
                    pass


def main():
    with open("TXT/szachy.txt", "r", encoding="utf-8") as plansze:
        plansze = plansze.read().strip().split("\n\n")
        plansze = [x.split("\n") for x in plansze]
        print(zadanie1(plansze))
        print(zadanie2(plansze))

if __name__ == "__main__":
    main()
