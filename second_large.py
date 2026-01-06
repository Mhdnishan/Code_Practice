def largee():
    a=[23,45,65,34,55,59]
    large=a[0]
    second_large=a[0]
    for i in a:
        if i > large:
         large=i
    for j in a:
        if j <large:
            second_large=j
    print(second_large)
largee()