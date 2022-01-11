import random

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m,""n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["1","2","3","4","5","6","7","8","9"]
char = ["@","#","$","%","&","*"]
k_letter = int(input("enter the number of letters"))
k_numbers = int(input("enter the number of numbers to be in password"))
k_char = int(input("enter the number of number of characters in password"))
total = k_char + k_numbers + k_letter
c=0
j=0
d=0
password = ""
for i in range(1,total + 1):
    k = random.randint(1,3)
    if k==1:
        if c > k_letter:
            continue
        else:
          password += random.choice(letters)
          c += 1
    if k==2:
        if j > k_numbers:
            continue
        else:
            password += random.choice(numbers)
            j += 1
    if k==3:
        if d > k_char:
           continue
        else:
              password += random.choice(char)
              d += 1




print(password)
