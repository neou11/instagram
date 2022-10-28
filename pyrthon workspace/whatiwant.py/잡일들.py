# subjects = []
# MyList = ["첫", "두", "세", "네", "다섯", "여섯", "일곱"]
# for orders in MyList:


#     MyList = ["첫", "두", "세", "네", "다섯", "여섯", "일곱"]
#     while True:
#         Day = input("요일을 입력해주세요: ")
#         if Day in "일월화수목금토":
#             break
# #end if while
#     subjects = []
#     for orders in MyList:
# # print(orders)
#         subject = input(orders + " 번째 과목을 입력해주세요: ")
#         subjects.append(subject)
#         if any(Day.find(_)>=0 for _ in "월수금"):
#             if orders == "여섯":
#                 break
# #end
#         else:
#             continue
# #end
# #end for
# print(subjects)

# from cmath import pi
# import math 
# print(pi)

# pow = lambda x, y: x * y
# print(pow(3, 4))
# f = lambda x: f(x)
# # print(f(4))
# try :
#     number_input_a = int(input("정수 입력> "))
#     print("원의 반지름:", number_input_a)
#     print("원의 둘레", number_input_a * 2 * 3.14)
#     print("원의 넓이:", number_input_a ** 2 * 3.14)
# except Exception as exception:
#     print("type(exception):", type(exception))
#     print("exceptinon:", exception)
# list = []
# list


import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier()

fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8, 
                10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7, 
                7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]
fish_data = [[l, w] for l, w in zip(fish_length, fish_weight)]










