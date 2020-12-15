import random

def list1():
    a = []
    i = 0
    while i < random.randint(0,25):
        a.append(random.randint(0,100))

    return a
a = list1()
print(a)
print(a[0], a[-1])
