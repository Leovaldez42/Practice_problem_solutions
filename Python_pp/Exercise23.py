primeNumbers = []
happyNumbers = [] 

overlappingNumbers = []
   
open_prime_file = open('prime_numbers.txt', 'r')
open_happy_file = open('happy_numbers.txt', 'r')

primeNumbers = open_prime_file.readlines()
happyNumbers = open_happy_file.readlines()

for prime in primeNumbers:
    for happy in happyNumbers:
        if prime == happy:
            overlappingNumbers.append(prime.rstrip());

for x in overlappingNumbers:
    print(x)

print('Number of overlapping numbers: ' + str(len(overlappingNumbers)))
