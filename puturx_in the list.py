r1 = ["0","0","0"]
r2 = ["0","0","0"]
r3 = ["0","0","0"]
print(f"{r1}\n{r2}\n{r3}")
row = [r1,r2,r3]
k = input("enter the column and row of the place u want to place ur x ")
ver = int(k[0])
hor = int(k[1])
row[ver - 1][hor - 1] = "X"
print(f"{r1}\n{r2}\n{r3}")