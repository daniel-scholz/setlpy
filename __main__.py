
import setlx
from setlx.splayset import Set
s1 = Set()
s2 = Set()
j = 10
for i in range(1, 10):
#     for j in range(1, 5):
        s1.insert(setlx.List([10-i, j]))
        s2.insert(setlx.List([i,j]))


print(s1)
print(s2)
print(s1==s2)