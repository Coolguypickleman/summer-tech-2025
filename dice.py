from random import randint

f=int(input("how many dice do you want?: "))
while f!=0:
    a=input("what type of dice do you want? (d4, d6, d10, d20): ")
    for i in range(0,f):
        f=f-1
        if a=="d4":
            b=randint(1,4)
            print(b)
        elif a=="d6":
            c=randint(1,6)
            print(c)
        elif a=="d10":
            d=randint(1,10)
            print(d)
        elif a=="d20":
            e=randint(1,20)
            print(e)
        else:
            print("invalid dice")