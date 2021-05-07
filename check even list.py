def check_numbers_list(num1,num2):
    i=0
    while i<len(num1):
        if num1[i]%2==0 and num2[i]%2==0:
            print(num1[i],num2[i],"dono se divisble hai ","even hai ")
        else:
            print(num1[i],num2[i],"divisble nhi hai")
        i=i+1

check_numbers_list([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87])
            