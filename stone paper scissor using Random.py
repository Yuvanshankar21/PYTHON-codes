import random

while True:
    a = 3
    b = int(a * random.random()) + 1
    c = int(input("\n1.stone\n2.paper\n3.scissor\nselect the option"))
    #getting input from the user


    if b == c:
        print("draw")
    #draw conditions

    if b==1 or c==1:
        if b==2 or c==2:
            print("")
        elif b== 3 or c==3:
            if b==3:
                print("user win")
            else:
                print("sys win")

    if b==2 or c==2:
        if b==3 or c==3:
            print("")

        elif b == 1 or c == 1:
            if b == 1:
                print("user win")
            else:
                print("sys win")

    if b==3 or c==3:
        if b==1 or c==1:
            print("")
        elif b == 2 or c == 2:
            if b == 2:
                print("user win")
            else:
                print("sys win")

   #checking the user and systems conditions and validation


    a=int(input("do u want to countinue.. press.1\nor exit.0"))
    if a==1:
        continue
    elif a==0:
        break
    #to exit or continue conditions
