from  random import randint
p = list([randint(1,100) for i in range(20)])
h = []
for i in p:
    if i % 2 == 0:
        h.append(i)
print(h)