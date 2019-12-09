"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Extras:
1. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
   Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
"""

#  Date time function imported for finding current date and time
import datetime

name = input('Type your name: ')
age = input('Hi ' + name +  ' so how old are you? ')

# now gives cuurent date time and now.year will give the year
now = datetime.datetime.now()
print(now.year)

print('So ' + name + ' you will complete 100 years in ', (now.year + 100 - int(age)))

# Extras
n = int(input("How many copies of the message do you need? "))
for i in range(0, n):
    print('So ' + name + ' you will complete 100 years in ', (now.year + 100 - int(age)))
