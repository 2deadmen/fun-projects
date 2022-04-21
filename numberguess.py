import random

print("NUMBER GUESS")



def result(attempt,n,number):


    if (n == number ):
        print("you won")
        return 0
    elif (n > number):
        print("too high")
        print("guess again")
        return attempt - 1
    elif (n< number ):
        print("too low")
        print("guess again")
        return attempt -1



choice = int(input("level 1:easy  2:hard"))
print(" try guessing the  number between 1 and 100")

if choice == 1:
    attempt = 10

elif choice == 2:
    attempt = 5
number = random.randint(1,100)
while (attempt != 0):
    n = int(input(" try guessing "))
    attempt =result(attempt,n,number)
    print(f"you have {attempt} guesses left")
