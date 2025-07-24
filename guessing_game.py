from random import randint
c=int(input("guesses = "))
a=randint(1,100)
min=1
max=100
while c!=0:
    print(c, "more guesses")
    c=c-1
    print("pick a number between", min, "-",max)
    b=int(input("= "))
    if a == b:
        print("you guessed the correct number")
        c=0
    elif a>b and b>min:
        min=b
        print(min, "-", max)
    elif a<b and b<max:
        max=b
        print(min, "-", max)
    else:
        print("invalid number")
        c=0