def string(length1,length2):
    if len(length1)<len(length2):
        print(length2,"length2 is greater ")
    elif len(length1)>len(length2):
        print(length1,"length1 is greater")
    else:
        print("both are equel")
length1=str(input("enter the number"))
length2=str(input("enter the number"))
string(length1,length2)