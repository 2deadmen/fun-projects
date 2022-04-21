
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
w = resources["water"]
m = resources["milk"]
c = resources["coffee"]
ew = MENU["espresso"]["ingredients"]["water"]
ec = MENU["espresso"]["ingredients"]["coffee"]
cw = MENU["cappuccino"]["ingredients"]["water"]
cm = MENU["cappuccino"]["ingredients"]["milk"]
cc = MENU["cappuccino"]["ingredients"]["coffee"]
lw = MENU["latte"]["ingredients"]["water"]
lm = MENU["latte"]["ingredients"]["milk"]
lc = MENU["latte"]["ingredients"]["coffee"]
run = True
totalmoney =0
def askmoney(a):
    total =0
    q = int(input("enter the number of quarter"))
    d = int(input("enter the  number of dimes"))
    n = int(input("enter the number of nickel"))
    p = int(input("enter the number of penny"))
    total = q*0.25 + d*0.10 + n*0.5 + p*0.01
    if a == 1:
      e = MENU["espresso"]["cost"]
      if total < e:
          print("not enough money...money refunded")
      else:

          change = total -e
          print(f" enjoy your espresso...here's your change {change}")
          return e
    elif a == 2:
        f = MENU["cappuccino"]["cost"]
        if total < f:
            print("not enough money...money refunded")
        else:

            change = total -f
            print(f"enjoy your cappuccino...here's your change {change}")
            return  f
    elif a==3:
        l = MENU["latte"]["cost"]
        if total < l:
            print("not enough money...money refunded")
        else:

            change = total -l
            print(f"enjoy your latte...here's your change {change}")
            return l




while run == True:

 ask = input("which coffee do u like(espresso/cappuccino/latte)")

 if ask == "espresso":


    if w > ew  and c > ec:
        money = askmoney(1)
        w = w - ew
        c = c - ec
        totalmoney += money
    else :
        print("not enough ingredients")
 elif   ask =="cappuccino":
    if w > cw and m > cm and c > cc:
        money = askmoney(2)
        w = w - cw
        m = m - cm
        c = c - cc
        totalmoney += money
    else:
        print("not enough ingredients")
 elif ask == "latte":
    if w > lw and m > lm and c > lc:
        w = w - lw
        m = m - lm
        c = c - lc
        money = askmoney(3)
        totalmoney += money
    else:
        print("not enough ingredients")
 elif ask == "off":
    run = False

 elif ask == "report":
    print(f"milk :{m},water:{w},coffee:{c},total money:{totalmoney}")
