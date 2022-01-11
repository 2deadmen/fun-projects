import random

print("""WELCOME TO  HANGMAN    
                                 +===|
                                 |   |
                                 0   |
                               / | \ |
                                 |   |
                                / \  |
                                     |
                              =======|      """)
list = ["""
=======|
   |   |
   0   |
   |   |
       |
       |
=======|       
""", """
=======|
   |   |
   0   |
   | \ |
       |
       |
=======|              
""", """"
=======|
   |   |
   0   |
 / | \ |
       |
       |
========        

""", """
=======|
   |   |
   0   |
 / | \ |
   |   |
       |
========         
"""
    , """
=======|
   |   |
   0   |
 / | \ |
   |   |
  /    |
=======|  

""", """
=======|
   |   |
   0   |
 / | \ |
   |   |
  / \  |
=======|       
"""]
print("remember:you are guessing a clash of clans character")
words = ["gaint", "barbarian", "goblin", "archer", "balloon", "witch", "bowler", "dragon", "wizard", "healer", "pekka",
         "miner", "yeti", "minion", "valkyrie",
         "golem"]
k = random.choice(words)

display = []
for i in k:
    display += "_"

print(display)
c = 0
end_of_game = False
while not end_of_game:
    guess = input("guess the letter").lower()
    for position in range(len(k)):

        letter = k[position]
        if letter == guess:
            display[position] = guess
            print(display)
    if guess not in display:
        print("oops...wrong guess")
        print(list[c])
        print(f"you have {5 - c} lives left")
        c += 1
    if c == 6:
        print("game over...YOUR MAN IS DEAD")
        break

    if "_" not in display:
        end_of_game = True
        print("\t\t\tSUP\n"
              "\t\t\tERC\n"
              "\t\t\tELL\n")
        print("you won   ")

