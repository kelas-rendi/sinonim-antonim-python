def typo(kata):
    listkata = [ x for x in kata ]
    newlist = []
    print(listkata)
    for i, x in enumerate(listkata):
        # print(listkata[i])

        if i not in newlist:
            newlist.append(x)

    kata = ''.join(newlist)
    return(kata)

kamus = ['ketahuan','kemurkaan','ketua']

kata = 'kwtahuannn'

bener = typo(kata)
print(bener)