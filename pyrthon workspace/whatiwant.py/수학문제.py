# for i in range(1, 30):
#     x = (1/8**i)
#     intlist = []
#     intlist.append(x)
# key = sum(intlist)
# print(key)

def key(x):
    int = range(1, x)
    for i in int:
        y = ((1/8)**i)
        intlist = []
        intlist.append(y)
        print(intlist)
    key = sum(intlist)
    print(key)
key(30)


# # key(30)
# key(5)

list = []
list.append(1)
list.append(20)
print(list)