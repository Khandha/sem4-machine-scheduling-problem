# -*- coding: utf-8 -*-

import random
import timeit
import os
import io
import json
import time
from datetime import datetime
from time import localtime, strftime

data2 = strftime("%Y%m%d%H%M%S", localtime())
DIRNAME = os.path.dirname(os.path.abspath(__file__))
DATA_PATH3 = os.path.join(DIRNAME, data2 + '.txt')

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
