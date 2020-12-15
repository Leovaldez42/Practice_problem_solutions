""" Ask the user for a string and print out whether this string is a palindrome or not. 
    (A palindrome is a string that reads the same forwards and backwards.) """
s = input()
if s == s[::-1]:
    print("palindrome")
else:
    print("not palindrome")
