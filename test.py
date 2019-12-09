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
x, y =[int(x) for x in input("Enter 2 numbers, first being the dividend and second being divisor seperated by space: ").split()]
try:
    if x % y == 0:
        print(str(x) + ' is divisble by ' + str(y) )
    else:
        print(str(x) + ' is not divisble by ' + str(y))
except ValueError:
    print("Both the numbers should be printed in same line seperated by a space.")