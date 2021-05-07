def list_change(num1,num2):
    i=0
    b=[]
    while i<len(num1):
        c=num1[i]*num2[i]
        b.append(c)
        i=i+1
    print(b)
list_change([5,10,50,20],[2,20,3,5])
