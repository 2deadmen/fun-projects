from data import data
import random


player = random.choice(data)
player_name = player["name"]
player_follower_count = player["follower_count"]

count =0
k = True
while k == True:
 player2 = random.choice(data)
 while player == player2:

   player2 = random.choice(data)

 player2_name = player2["name"]
 player2_follower_count = player2["follower_count"]

 print(f"{player_name}"
      f" vs "
      f"{player2_name}")
#take user input
 ans = int(input(" is second one higher=1    or   lower=2"))


#check for the answer
 if player_follower_count < player2_follower_count and ans==1 or player_follower_count > player2_follower_count and ans==2 :
   count += 1
   print(count)
   print("correct")
   if player_follower_count < player2_follower_count:
     big = player2
   else:
     big = player


   player = big
 else:
  print("game over")
  k = False


