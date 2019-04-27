import setlx
from setlx.splayset import Set

s1 = Set()
s2 = Set()
j = 10
n = 100
for i in range(1, n):
    s1.insert(setlx.List([10 - i, j]))
for i in range(1, n):
    s1[10 - i] = j + 1
    
print(s1)