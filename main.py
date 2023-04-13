# Name: Anushka Purwar
# Roll no.: E22MCAG0036
from GreekPizza import *
from ChicagoPizza import *
from NewYorkStylePizza import *
from SicillianPizza import *
from MozzarellaChesse import *
from ParmesanChesse import *
from ProvoloneChesse import *
from RegiannoChesse import *
from PlumTomatoSause import *
from PumpkinSauce import *
from MarinaraSauce import *
from BarbecueSauce import *
from ThinCrustDough import *
from ThickCrustDough import *
from Pizza import *
from Cheese import *
from abc import ABC

total=0
dcost,ccost,pcost,scost=0,0,0,0
cost=0

def calculateCost(res1):
    global total
    total+=res1

def displayDetails(price):
    global cost
    cost=price
    print(f"The total cost for your selected Pizza is: {cost}")

def dough():
    global dcost
    print("Select a dough:")
    print("1. Thin Crust Dough")
    print("2. Thick Crust Dough")
    d=int(input("Enter your choice: "))
    if(d==1):
        dobj=ThinCrustDough(120)
        dcost=dobj.get_dough_price()
        calculateCost(dcost)
    elif(d==2):
        dobj=ThickCrustDough(150)
        dcost=dobj.get_dough_price()
        calculateCost(dcost)
    else:
        print("You entered wrong choice!!")

def sauce():
    global scost
    print("Select a sauce:")
    print("a. Plum Tomato Sause")
    print("b. Pumpkin Sause")
    print("c. Marinara Sauce")
    print("d. Barbecue Sauce")
    s=input("Enter your choice: ")
    if(s=='a'):
        sobj=PlumTomatoSauce(50)
        dough()
        scost=sobj.get_sauce_price()
        calculateCost(scost)
    elif(s=='b'):
        sobj=PumpkinSauce(100)
        dough()
        scost=sobj.get_sauce_price()
        calculateCost(scost)
    elif(s=='c'):
        sobj= MarinaraSause(150)
        dough()
        scost=sobj.get_sauce_price()
        calculateCost(scost)
    elif(s=='d'):
        sobj= BarbecueSauce(100)
        dough()
        scost=sobj.get_sauce_price()
        calculateCost(scost)
    else:
        print("You entered wrong choice!!")
 

def cheese():
    global ccost
    print("Select a cheese:")
    print("i. Mozzarella Chesse")
    print("ii. Provolone Chesse")
    print("iii. ParmesanChesse")
    print("iv. Regianno Chesse")
    ch=input("Enter your choice: ")
    if(ch=='i'):
        cobj= MozzarellaChesse(100)
        ccost=cobj.get_cheese_price()
        sauce()
        return calculateCost(ccost)
    elif(ch=='ii'):
        cobj= ParmesanChesse(150)
        ccost=cobj.get_cheese_price()
        sauce()
        return calculateCost(ccost)
    elif(ch=='iii'):
        cobj= ProvoloneChesse(180)
        ccost=cobj.get_cheese_price()
        sauce()
        return calculateCost(ccost)
    elif(ch=='iv'):
        cobj= RegiannoChesse(200)
        ccost=cobj.get_cheese_price()
        sauce()
        return calculateCost(ccost)
    else:
        print("You entered wrong choice!!")
    

def main():
    global pcost
    print("MENU")
    print("Select a pizza:")
    print("1. Greek Pizza")
    print("2. Chicago Pizza")
    print("3. New York Style Pizza")
    print("4. Sicillian Pizza")
    p=int(input("Enter your choice: "))
    if(p==1):
        pobj= GreekPizza(100)
        pcost=pobj.get_pizza_price()
        cheese()
        calculateCost(pcost)
    elif(p==2):
        pobj= ChicagoPizza(250)
        pcost=pobj.get_pizza_price()
        cheese()
        calculateCost(pcost)
    elif(p==3):
        pobj= NewYorkStylePizza(200)
        pcost=pobj.get_pizza_price()
        cheese()
        calculateCost(pcost)
    elif(p==4):
        pobj= SicillianPizza(300)
        pcost=pobj.get_pizza_price()
        cheese()
        calculateCost(pcost)
    else:
        print("You entered wrong choice!!")

main()
displayDetails(total)