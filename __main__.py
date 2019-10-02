from setlx import Set


e = Set()
s = Set(["a", 2, e, [3, 2]])
s3 = Set(["a", 2, e, [3, 2], "b"])
b = s < s3

print(b)
print(s)

# TODO: fix linear complexity
