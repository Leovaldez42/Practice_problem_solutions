def isPrime(n):
    if n <= 1:
        return "Not prime"
    for i in range(2,n):
        if n%i == 0:
            return "Not prime"

    return "Prime"


num = int(input("Enter a number : "))
print(isPrime(num))