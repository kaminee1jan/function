def strong_password(x):
    l,u,d,s=0,0,0,0
    for i in x:
        if (i.islower()):
            l+=1
        if (i.isupper()):
            u+=1
        if (i.isdigit()):
            d+=1
        if(i=="@" or i=="#" or i=="$"):
            s+=1
    if len(x)>=16:
        if (l>=1 and u>=1 and d>=1 and s>=1):
            print("strong password")
        else:
            print("not a strong password")
    else:
        print("plz make sure password should be at least 8 characters")
x=input("enter ur password:")
strong_password(x)
