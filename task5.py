words = "Hello", "Alaska", "Dad", "Peace"
s1 = "qwertyuiop"
s2 = "asdfghjkl"
s3 = "zxcvbnm"
b = 0
c = 0
d = 0
# w1 = (''.join(words[0])).lower()
for i in words:
    p = i.lower()
    for k in p:
        if k in s1:
            b = b+1
            if b == len(p):
                print(i)
                break
        elif k in s2:
            c = c+1
            if b == len(p):
                print(i)
                break
        elif k in s3:
            d = d + 1
            if d == len(p):
                print(i)
                break
