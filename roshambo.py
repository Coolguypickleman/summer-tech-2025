from random import randint

c=int(input("best of: "))

while c!=0:
    print(c,"more rounds")
    

    a=input("rock, paper, or scissors: ")
    b = randint(1,2)

    if b==1:
        print("rock")
    if b==2:
        print("paper")
    if b==3:
        print("scissor")

    if a=="rock":
        if b==1:
            print("tie")
            c=c
        if b==2:
            print("you lose")
            c=c-1
        if b==3:
            print("you win")
            c=c-1

    if a=="paper":
        if b==1:
            print("you win")
            c=c-1
        if b==2:
            print("tie")
            c=c
        if b==3:
            print("you lose")
            c=c-1

    if a=="scissor":
        if b==1:
            print("you lose")
            c=c-1
        if b==2:
            print("you win")
            c=c-1
        if b==3:
            print("tie")
            c=c