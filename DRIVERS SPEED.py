def drivers(speed):
    if speed<=70:
        print("ok")
    elif speed>70:
        i=70
        c=0
        while i<speed:
            c=c+1
            i=i+5
        print(c)
    if c>12:
        print("liscence suspend")
speed=int(input("enter the number:"))
drivers(speed)