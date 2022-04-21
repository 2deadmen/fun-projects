from replit import clear

def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return  n1-n2

def mult(n1,n2):
    return n1 *n2
def div(n1,n2):
    return n1/n2
again = False
while not again:
 sym = {
    '+':add,
    '-':sub,
    '*':mult,
    '/':div

 }

 n1 =int(input("enter the value of the first number"))
 n2 =int(input("enter the value of the second number"))
 op = input("enter the operation"
           "+"
           "-"
           "*"
           "/")
 function= sym[op]
 res = function(n1,n2)
 print(res)
 next = input("continue.???'yes' or 'no'").lower()
 if (next=="no"):
    clear()
    again = True
 elif (next=="yes"):

   againn=False
   while not againn:
       n1 = res
       n2 = int(input("enter the value of the second number"))
       op = input("enter the operation"
                  "+"
                  "-"
                  "*"
                  "/")
       function = sym[op]
       res = function(n1, n2)
       print(res)
       next = input("continue.???'yes' or 'no'").lower()
       if (next == "no"):
           print("\n"
                 "\n"
                 "\n"
                 "\n"
                 "\n"
                 "\n"
                 "")
           againn = True



