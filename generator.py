# -*- coding: utf-8 -*-

import random
import timeit
import os
import io
import json
import time
from datetime import datetime
from time import localtime, strftime

data = strftime("%Y%m%d", localtime())
data2 = strftime("%Y%m%d%H%M%S", localtime())
DIRNAME = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(DIRNAME, 'all.txt')
DATA_PATH2 = os.path.join(DIRNAME, data + '.txt')
DATA_PATH3 = os.path.join(DIRNAME, data2 + '.txt')

'''

def liczby():
    for i in range(111):
        yield i
        
for parzysta in liczby():
    print(parzysta)


var1 = random.randint(1, 6)
var2 = random.randrange(6) + 1
total = var1 + var2
print("Wyrzuciles", var1, "oraz", var2, "i uzyskałes sume", total)

def generate(Range, step, numOfSteps):
    lista =[]
    for a in range(numOfSteps):
        lista.append([])
        for x in range(step * (a+1)):
            lista[a].append(random.randint(0, Range))
    return lista

print (generate(1000, 10, 2))

print('test')

'''

w1 = int(input("Podaj wartość początkową listy: "))
w2 = int(input("Podaj wartość końcową listy: "))
w3 = int(input("Podaj ilość elementów listy: "))

listaa = [random.randint(w1, w2) for r in range(w3)]

with open(DATA_PATH3, 'w') as f:
    f.write('')
    with open(DATA_PATH3, 'a') as f:
        f.write('\n'.join([str(item) for item in listaa]))

print('\n'.join([str(item) for item in listaa]))
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
