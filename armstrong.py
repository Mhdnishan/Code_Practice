def num():
    a = input("Enter a number to find Armstrong: ")
    n = int(a)
    total = 0

    for i in a:
        total += int(i) ** len(a)

    if total == n:
        print("Its an Armstrong number")
    else:
        print("Given number is not an Armstrong number")

num()
