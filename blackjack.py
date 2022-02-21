import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def draw():
    card = random.choice(cards)
    return card
comp =[]
player =[]

def draw2():

        card1 = draw()
        comp.append(card1)

        card1 = draw()
        player.append(card1)
        print(f"your deck=={player}")
        print(" The result is that\n")
        result()



def result():

    sum=0
    sum1=0
    for i in player:
        sum += i

    for j in comp:
        sum1 += j

    if (sum > 21):
        print("you loose\n")
        print(f"comp's deck== {comp}")

    elif (sum == 21 and (sum1 > sum or sum1 < sum )):
        print("you win")
        print(f"comp's deck== {comp}")

    elif (sum == sum1):
        print("draw")
        print(f"comp's deck== {comp}")


    elif (sum <= 16 and len(player)==2):
        print("you will have to draw one more card because the value is less than 16")
        draw2()

    else:
        if ( sum < sum1):
            print("you loose\n")
            print(f"comp's deck== {comp}")
        elif( sum > sum1):
            print("you win\n")
            print(f"comp's deck== {comp}")






print("BLACKJACK\n"
      "bet on  your luck here\n")

st = input("type 'y' to start the game")
if (st=="y"):
    card1 = draw()
    comp.append(card1)
    print(f"computer's deck =={comp}")

    card1 = draw()
    player.append(card1)
    print(f"your deck=={player}")
    cont1= input("enter 'y' to draw the next card")
    if (cont1 =="y"):
        card1 = draw()
        comp.append(card1)

        card1 = draw()
        player.append(card1)
        print(f"your deck=={player}")
        cont2 = input("enter 'y' to draw another card or 'n' to get the result")
        if (cont2 == "y"):
            draw2()


        elif (cont2 =="n"):
             result()


        else:
            print("invalid key")



