studentlist = input("enter the list of students").split()
big=0
k=0
for i in studentlist:
    k=int(i)

    if k >= big:
        big = k
print(big)
