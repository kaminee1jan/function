def calculator(number_x,number_y):
    if symble == ("+"):
        return(num1+num2)
    elif symble == ("-"):
        return (num1-num2)
    elif symble == ("*"):
        return (num1*num2)
    elif symble== ("/"):
        return (num1/num2)
num1=int(input("enter the number"))
symble=input("Enter the  symble")
num2=int(input("enter the number"))
print(calculator(num1,num2))
