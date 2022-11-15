def sucin(zoznam):
    vys = 1
    for i in zoznam:
        vys *= i
    return vys


c = [2, 3, 5, 7, 11]
print(sucin(c))                     # čo je 2*3*5*7*11
print(sucin(list(range(1, 11))))   # čo je 10 faktorial
print(sucin([2] * 20))  # čo je 2 ** 20
print(sucin([]))
