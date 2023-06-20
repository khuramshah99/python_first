animals=["tiger","goat","elephant","cat"]
#append

animals.append("dog")
print(animals)

#remove
animals.remove("tiger")
print(animals)

#pop
animals.pop()
print(animals)


 #insert

animals.insert(2,"bull")
print(animals)

#for loop

for i in animals:
    print(i)


#if else


marks = int(input("Enter your Marks----: "))

if marks > 50:
    print("congratulations You Done a Good job.." )
elif marks == 50:
    print("congratulations  ! Hardly Passed.." )
else:
    print(" Dont Loose HOPES and try AGAIN")
