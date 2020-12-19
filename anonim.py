kata = "gua suka gkgkgkgk lu"

f = open("data.txt", "r")
for x in f:
    word = x.rstrip('\n')
    onim = word.split(':')
    print(onim)
    kata2 = kata.split()
    new_kata = []
    for k in kata2:
        print(k)
        if onim[0] == k:
            k = (onim[1])
        new_kata.append(k)

    new_kata = ' '.join(str(e) for e in new_kata)

print(new_kata)