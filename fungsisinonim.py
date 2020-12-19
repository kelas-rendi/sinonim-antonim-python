
def sinonim(kata):
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