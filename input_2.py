def nakup(zoznam):
    cena = 0
    for i in range(0, len(zoznam)-1, 2):
        cena += zoznam[i] * zoznam[i+1]
    return cena


print(nakup([3, 2.5, 0.5, 10, 1.2, 1.2]))
