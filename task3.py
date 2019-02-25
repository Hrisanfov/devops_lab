friends1 = "vasya-pupkin", "bill-hates", "ivan-ivanov"
friends2 = "vasya-pupkin", "destroyer"
print("Friends:", friends1)
for i in friends1:
    if i in friends2:
        print("Mutual Friends:", i)
for k in friends2:
    if k not in friends1:
        print("Also Friend of:", k)