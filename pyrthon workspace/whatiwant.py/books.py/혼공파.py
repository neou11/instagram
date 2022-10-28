# print("Hello, World")
# def PrintMenu():
#     menu = ["coffee", "mini_cake", "cake"]
#     price = [1500, 2000, 3500]
#     order = [0, 1, 2]
#     for i in order:
#         print(menu[i] + ":", price[i])
# PrintMenu()

# def PlusOne(x):
#     print(x + 1)
# PlusOne(9)

# subject_list = []

# first = input("1교시 과목을 입력해주세요 ")
# second = input("2교시 과목을 입력해주세요 ")
# third = input("3교시 과목을 입력해주세요 ")

MyList = ["첫", "두", "세", "네", "다섯", "여섯", "일곱"]
Day = input("요일을 입력해주세요 ")
for orders in MyList:
    # print(orders)
    subjects = []
    subject = input((orders + "번째 과목을 입력해주세요 "))
    subjects.append(subject)
    if Day.find("월") >= 0 or Day.find("수") >= 0 or Day.find("금") >= 0:
        if orders == "여섯":
            break
    else:
        continue


