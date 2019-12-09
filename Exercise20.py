import random
my_randoms = [set([random.randrange(1,101, 1) for _ in range(50)])]
print(my_randoms)
n = int(input("Enter the number you want to check: "))
is_num = True if n in my_randoms else False
print(is_num)