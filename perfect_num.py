def perfect():
    n=int(input("enter a number"))
    a=[]
    sum=0
    for i in range(1,n):
     if n%i==0:
        a.append(i)
    for j in a:
     sum+=j
    if sum==n:
     print("its pefect number")
    else:
     print("not perfect number")

    print(a)
perfect()