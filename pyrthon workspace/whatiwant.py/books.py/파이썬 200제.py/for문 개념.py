scope = [1, 2, 3, 4, 5]
for i in scope:
    print(i)
    if i < 3:
        continue
    else:
        break
else:
    print("Perfect")