
def sinonim(kata):
    kata = kata.lower()
    print(kata)
    f = open("data.txt", "r")
    sinonim = []
    list_kata = kata.split()
    for x in f:
        word = x.rstrip('\n')
        sx = word.split(':')
        sinonim.append(sx)

    new_kata = []
    for k in list_kata:
        for s in sinonim:
            if s[0] == k:
                k = s[1]
        new_kata.append(k)

    return ' '.join(new_kata)

data = sinonim('lu gk cinta gua')
print(data)

import csv

with open('by.u_sentimen_oct20.csv',encoding="utf8") as csvfile:
    hasilBaca = csv.reader(csvfile, delimiter=';')
    print(hasilBaca) # karena bentuknya csv object yang berbentuk iterasi
    lendata = 0
    for row in hasilBaca:
        lendata += 1
        print(sinonim(row[2]))
        if lendata == 30:
            break