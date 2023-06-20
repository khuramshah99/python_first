import random
compnum = random.randrange(1,51)
userinput = int(input("Enter yout Number..."))
if userinput > compnum:
    print("computer number ",compnum)
    print("your Guess number is High")
elif compnum>userinput:
    print("computer number ", compnum)
    print("your Guess number is low")
else:
    print("computer number ", compnum)
    print("your Guess number is Equal..")


