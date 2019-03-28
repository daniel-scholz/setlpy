import random
import string
import time
from setlx.splayset import Set

random = random.Random(27121998)
start = time.perf_counter()
j = random.randint(1, 100000000)
a = Set(j)

for i in range(1, 10000):
    a.insert(random.randint(1, 100000000))
a.find(j)
stop = time.perf_counter()
print(stop-start)
# print(a)
