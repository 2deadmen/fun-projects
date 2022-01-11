tot = int(input("enter the total amountof bill"))
num = int(input("enter the number of people to split among"))
per = int(input("enter the percentage of the tip"))
tip = float((per/100)*tot)
each = tip/num
each1 = str(each)

print("the amount for each"+each1)
