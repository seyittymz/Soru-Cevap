def asal_sayi_toplam():
    toplam = 0
    for index in range(2,1000000):
        temp = index
        while index % 2 == 0:
           index /=2
        while index % 3 == 0:
           index /=3
        while index % 5 == 0:
           index /=5
        if index == 1 :
            toplam += temp
    return toplam

print(asal_sayi_toplam())