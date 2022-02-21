
from replit import clear
bidders = {}
finished = False
while not finished:
    name = input("enter your name")
    price =int(input("enter the amount"))
    bidders[name]=price
    con = input("are there any more bidders 'yes or 'no'").lower()
    if (con=="no"):
        finished = True
    elif(con=="yes"):
        clear()


high = 0
for i in bidders:
    score = bidders[name]
    if score>high:
        high = score
        winner = name
print(f"the winner is {winner} who bid {high}")