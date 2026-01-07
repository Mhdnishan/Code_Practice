def dup():
    a = [1, 2, 2, 3, 5, 3, 4, 6, 7]
    b = []   
    c = []   

    for i in a:
        if i not in b:
            b.append(i)
        else:
            c.append(i)

    print(c)

dup()
