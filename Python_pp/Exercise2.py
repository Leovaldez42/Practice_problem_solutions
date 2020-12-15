"""Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
   Hint: how does an even / odd number react differently when divided by 2?

Extras:
1. If the number is a multiple of 4, print out a different message.

2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
   If check divides evenly into num, tell that to the user. If not, print a different appropriate message. """

n = int(input("Enter a number: "))
if n % 2 == 0:
    print(str(n) + ' is even')

    # Extra
    if n % 4 == 0:
        print(str(n) + ' is a multiple of 4 too!') 
    else:
        print(str(n) + ' is not a multiple of 4')
else:
    print(str(n) + ' is odd')

# Extra
x, y =[int(x) for x in input("Enter 2 numbers, first being the dividend and second being divisor: ").split()]
if x % y == 0:
    print(str(x) + ' is divisble by ' + str(y) )
else:
    print(str(x) + ' is not divisble by ' + str(y))