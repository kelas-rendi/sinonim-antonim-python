kata = "meluu"
def typo(kata):
    listkata = [ x for x in kata ]

    newlist = []
    for i in listkata:
    if i not in newlist:
        newlist.append(i)

    kata = ''.join(newlist)
    return(kata)