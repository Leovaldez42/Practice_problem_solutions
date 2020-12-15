import random

print(""" You have to guess the 4 digit number
The number does not contain 0 in it although you can use 0 to guess the number.
The numbers are not repeated/
All the best.
TYpe 'exit' to exit the game.
""")
def generate_number():
    global number
    number = int(''.join(random.sample("123456789", 4)))
    return(int(number))

generate_number()
def ask_user():
    return input("Enter a number to guess: ")

def validate_number(user_num, rand_num):
    cows, bulls = 0, 0
    for x in range(0, len(rand_num)):
        if user_num[x] == rand_num[x]:
            cows += 1
        elif user_num[x] in rand_num:
            bulls += 1
    
    print('{}: {} cows, {} bulls'.format(user_num,cows,bulls))


if __name__ == '__main__':
    count = 0
    while(True):
        count += 1
        user_num = ask_user()
        if user_num == 'exit':
            break
        elif int(user_num) == number:
            print('Congratulations! \nYou guessed the right number!\n{} 4 cows, 0 bulls\nGAME OVER'.format(number))
            print("it took you " +str(count) + ' tries')
            break
        else:
            validate_number(user_num,str(number))
