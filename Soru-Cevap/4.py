def asal_mi(sayi):
    if sayi < 2:
        return False
    for i in range(2, int(sayi**0.5)+1):
        if sayi % i == 0:
            return False
    return True


def asal_sayi(istenilen):
    asal_listesi = []
    sayi = 2
    while len(asal_listesi) < istenilen:
        if asal_mi(sayi):
            asal_listesi.append(sayi)
        sayi += 1
    return asal_listesi[-1]


print(asal_sayi(10101))
