import random
n = random.randint(10,20)
l = []
for i in random.randint(0,n):
    l.append(random.randint(0,10))
print("This is original list: " + l)
a = []
for j in l:
    if j not in l:
        l.append(j)
print(a)