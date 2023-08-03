import random

Matriz = [ [], [], [] ]

for i in range(len(Matriz)):
    for j in range(len(Matriz)):
       Matriz[i].append(random.randint(0,10))


for i in range(len(Matriz)):
    print(Matriz[i])