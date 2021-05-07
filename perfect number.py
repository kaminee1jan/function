def perfect(n):
    i=1
    sum=0
    while i<n:
        if n%i==0:
            sum=sum+i
        i=i+1
    if sum==n:
        print(n,'perfect number')
    else:
        print(n,'nhi hai')
n=int(input("enter the number"))
perfect(n)