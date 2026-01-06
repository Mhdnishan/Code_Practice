def vowel():
    s=input("enter a string to check vowels :")
    vowels=["A","E","I","O","U","a","e","i","o","u"]
    count=0
    for i in s:
        if i in vowels:
            count+=1
    print(f"count of vowels in string :{count}")
vowel()
        