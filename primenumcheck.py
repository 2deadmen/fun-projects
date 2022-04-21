def prime(n):
    found =0
    i=1
    while (i <= n):

        if (n % i == 0):
            found += 1
        i+=1

    if (found  > 2):
        print("its not a prime number")
    else:
        print("its a prime number")


number = int(input("enter the the number"))
prime(number)
