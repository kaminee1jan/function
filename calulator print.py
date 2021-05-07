def calculator(number_x,number_y):
    if symble == ("+"):
        print(num1+num2)
    elif symble == ("-"):
        print(num1-num2)
    elif symble == ("*"):
        print(num1 * num2)
    elif symble== ("/"):
        print(num1/num2)
num1=int(input("enter the number"))
symble=input("Enter the  symble")
num2=int(input("enter the number"))
calculator(num1,num2)