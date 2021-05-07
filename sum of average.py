def user():
    i=0
    sum=0
    while i<3:
        d=int(input("enter the number"))
        sum=sum+d
        i=i+1
    print(sum)
    print("avg is:",sum/i)
user()
    