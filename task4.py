c = 0
p = 1
str = "-5 1 2 3 4 5 6 7 8 -3"
ar = [int(s) for s in str.split(' ')]
ar2 = sorted(ar)
for i in ar2:
    if i > 0:
        c = c + i
print(c)
armax = ar.index(max(ar))
armin = ar.index(min(ar))
for index, item in enumerate(ar):
    if (armax < index < armin or armin < index < armax):
        p=p*ar[index]
print(p)
