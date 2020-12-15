'''# Exercise 16 (and Solution)
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.
Extra:
Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.'''
import random

#function to create a strong password with uppercase letter, lowercase Letter, number and special characters
def generateStrongPassword():
    charsUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    charsLow = "abcdefghijklmnopqrstuvwxyz"
    charsNumber = "0123456789"
    charsSpecial = "!@#$%&*()[]{}"
    password = ''
    password += random.choice(charsUpper)
    password += random.choice(charsLow)
    password += random.choice(charsNumber)
    password += random.choice(charsSpecial)
    password += random.choice(charsUpper)
    password += random.choice(charsLow)
    password += random.choice(charsNumber)
    password += random.choice(charsSpecial)
    return password

#function to create a weak password from a default list
def generateWeakPassword():
    defaultPass = ['0123456','123456','abcdef','qawseedrf']
    return random.choice(defaultPass)

print('Generating password 1',generateStrongPassword())
print('Generating password 2',generateStrongPassword())
print('Generating password 3',generateStrongPassword())
print('Generating password 4',generateStrongPassword())

#Extra:
answer = input('Do you want strong or weak password?')
if answer == 'strong':
    print('Your strong password is ',generateStrongPassword())
elif answer == 'weak':
    print('Your weak password is ',generateWeakPassword())
else:
    print('ERROR, you have typed a wrong word, please try again typing "strong" or "weak"')