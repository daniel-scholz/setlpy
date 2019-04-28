import setlx
from setlx.splayset import Set

s1 = Set()
j = 10
n = 100
for i in range(1, n):
    # bug in squaring the
    s1.insert(setlx.List([(10 - i), j]))

print(s1)
