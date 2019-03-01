cost=float(input("How much does the item cost"))
amount=float(input("How much did you pay"))
change=amount-cost
print("Your change is ",change)
#how much 100s
num100=change//100
if num100>0:
    print( num100, "x $100")
change=change%100
#how many 50s
num50=change//50
if num50>0:
    print( num50, "x $50")
change=change%50
#how many 20s
num20=change//20
if num20>0:
    print( num20, "x $20")
change=change%20
#how many 10s
num10=change//10
if num10>0:
    print( num10, "x $10")
change=change%10
#how many 5s
num5=change//5
if num5>0:
    print( num5, "x $5")
change=change%5
#how many 2s
num2=change//2
if num2>0:
    print( num2, "x $2")
change=change%2
#how many 1s
num1=change//1
if num1>0:
    print( num1, "x $1")
change=change%1
#how many 0.25s
num0_25=change//0.25
if num0_25>0:
    if num0_25>0.03:
        change=change%0.25 +0.05
change=change%0.25
#how many 0.10s
num0_10=change//0.10
if num0_10>0:
    if num0_10>0.03:
        change=change%0.10 +0.05
change=change%0.10
#how many 10s
num0_05=change//0.05
change=change%0.05
if change>0.03:
    num0_05=num0_05+1
    if num0_05==2:
        num0_05=0
        num0_10=num0_10+1
print( num0_10, "x $0.10")
print( num0_05, "x $0.05")
print( num0_25, "x $0.25")


#Only print if you have a non-zero value
#Round your change.If you get to the end and there is three cent or more,give
#them another nickel. If there are two nickels, change it for a dime.
