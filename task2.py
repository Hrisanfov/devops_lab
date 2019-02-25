a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
d = int(input("d="))
x = range(-100, 101)
S = set()
for i in x:
    if a * i ** 3 + b * i ** 2 + c * i + d == 0:
        S.add(i)

print(" ".join([str(i) for i in S]))
