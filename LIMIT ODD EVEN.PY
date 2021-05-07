def shownumbers(limit):
    i=0
    while i<=limit:
        if i%2==0:
            print(i,"even number")
        else:
            print(i,"odd number")
        i=i+1
n=int(input("enter the number"))
shownumbers(n)