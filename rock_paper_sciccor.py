import random
#
# rock=0
# paper=1
# sciccors=2
ch = int(input("enter 0 for rock 1 for paper and 2 for sciccors"))
if ch == 0:
    print("you chose rock")
if ch == 1:
    print("you chose paper")
if ch == 2:
    print("you chose sciccors")

cmp = random.randint(0,2)
if cmp == 0:
    print("cmp chose rock")
if cmp == 1:
    print("cmp chose paper")
if cmp == 2:
    print("cmp chose sciccors")

if ch == cmp:
    print("its a draw")
else:
    if ch == 0 and cmp ==1:
        print("you loose")
    if ch == 1 and cmp ==0:
        print("you win")
    if ch == 2 and cmp ==0:
        print("you loose")
    if ch == 2 and cmp==1:
        print("you win")
    if ch==1 and cmp==2:
        print("you loose")
    if ch==0 and cmp==2:
        print("you win ")
