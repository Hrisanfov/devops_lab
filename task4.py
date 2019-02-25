c = 0
p = 1
str = "-7 5 -1 3 9"
ar = [int(s) for s in str.split(' ')]
ar = sorted(ar)
for i in ar:
    if i > 0:
        c = c + i
print(c)
for k in ar[:-1]:
    if (k != ar[-1] and k != ar[0]):
        p = p * k
print(p)
