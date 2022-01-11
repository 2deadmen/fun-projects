import random

each = input("enter the names with a comma")
names = each.split(",")

n = len(names)

pick = random.randint(0,n)

print(f"{names[pick]} should pay the bill")