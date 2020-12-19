kata = "gua suka lu"

f = open("data.txt", "r")
sinonim = []
list_kata = kata.split()
for x in f:
    word = x.rstrip('\n')
    sx = word.split(':')
    sinonim.append(sx)

print(sinonim)
new_kata = []
for k in list_kata:
    for s in sinonim:
        if s[0] == k:
            k = s[1]
    new_kata.append(k)

print(new_kata)
