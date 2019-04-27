import setlx
from setlx.splayset import Set

s1 = Set()
s2 = Set()
j = 10
for i in range(1, 10):
    s1.insert(setlx.List([10 - i, j]))
    s2.insert(setlx.List([i, j]))