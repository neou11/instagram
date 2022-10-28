# print(abs(-5))
# print(pow(4, 2))
# print(max(5, 12))
# print(min(5, 12))
# print(round(3.14))


# from math import *
# print(floor(4.99)) #내림

# print(ceil(3.14))
# # print(sqrt(16)) #제곱근

# from random import *

# print(random()) #0.0 이상 1.0미만의 임의의 값 생성
# print(random() * 10) #0.0 ~ 10.0 미만의 임의의 값 생성
# print(int(random() * 10))
# print(int(random() * 10))
# print(int(random() * 10))
# print((int(random() * 10)) + 1)
# print((int(random() * 10)) + 1)
# print((int(random() * 10)) + 1)
# print((int(random() * 10)) + 1)
# print((int(random() * 10)) + 1)

# print(int(random() * 45) + 1) # 1~45 이하의 임의의 값 생성 
# print(int(random() * 45) + 1) # 1~45 이하의 임의의 값 생성 
# print(int(random() * 45) + 1) # 1~45 이하의 임의의 값 생성 
# print(int(random() * 45) + 1) # 1~45 이하의 임의의 값 생성 
# print(int(random() * 45) + 1) # 1~45 이하의 임의의 값 생성 
# print(int(random() * 45) + 1) # 1~45 이하의 임의의 값 생성 


# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성

# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성

# sentence = "나는 소년입니다"
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# # print(sentence2)
# # sentence3 = """
# # 나는 소년이고, 파이썬은 쉬워요
# # """
# # print(sentence3)

# jumin = "990120-1234567"

# print("성별: " + jumin[7])
# print("연: " + jumin[0:2]) #0번째 부터 2번째 직전 값까지
# print("월: " + jumin[2:4])
# print("일: " + jumin[4:6])
# print("생년월일: " + jumin[0:6])
# print("생년월일: " + jumin[:6]) # 처음부터 6 직전까지
# print("뒤 7자리: " + jumin[7:14])
# print("뒤 7자리: " + jumin[7:]) # 7번째 부터 끝까지
# print("뒤 7자리 (뒤에부터): " + jumin[-7:]) 
# # 맨 뒤에서 7번째부터 끝까지

# 문자열 처리 함수

# python = "Python is Amazing"
# print(python.lower()) # 모두 소문자로
# print(python.upper()) # 모두 대문자로
# print(python[0].isupper()) 
# print(len(python))
# print(python.replace("Python", "Java"))

# index = python.index("n")
# print(index)
# index = python.index("n", index + 1)
# print(index)

# print(python.find("Java")) # -1이 나옴
# # print(python.index("Java")) 
# # 오류 python이라는 변수에는 자바가 없음

# print(python.count("n"))

# 문자열 포맷

# print("a" + "b")
# print("a", "b")

# 방법 1
# # print("나는 %d살입니다." % 20)
# # print("나는 %s을 좋아해요." %"파이썬")
# # print("Apple 은 %c로 시작해요." %"A")
# # # %s 로는 정수건 실수건 문자여링건 모두 가능
# # print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# # # 방법 2
# # print("나는 {}살입니다.".format(20))
# # print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
# # print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
# # print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# # 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))

# # 방법 4
# age = 20 
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")

#탈출 문자

# print("백문이 불여일견\n백견이 불여일타")
# # 저는 "나도코딩"입니다
# print("저는 '나도코딩'입니다")
# print('저는 "나도코딩"입니다')
# print("저는 \"나도코딩\"입니다")
# print("저는 \'나도코딩\'입니다.")

# # \\ : 문장 내에서 \

# #\r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")

# # \b : 백스페이스 (한 글자 삭제)
# print("Redd\bApple")

# # \t : 탭
# print("Red\tApple")

# 리스트 []

# 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# # subway = 30


# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)
# print(subway.index("조세호"))

# # # 하하씨가 다음 정류장에서 다음칸에 탐
# # subway.append("하하")
# # print(subway)

# # # 정형돈씨를 우재석 / 조세호 사이에 태워봄
# # subway.insert(1, "정형돈")
# # print(subway)

# # # 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄

# # # print(subway.pop())
# # # print(subway)
# # # print(subway.pop())
# # # print(subway)
# # # print(subway.pop())
# # # print(subway)

# # #같은 이름의 사람이 몇 명 있는지 확인

# # subway.append("유재석")
# # print(subway)
# # print(subway.count("유재석"))

# # 정렬도 가능
# num_list = [5, 2, 4, 3, 1]
# num_list.sort()
# print(num_list)

# # 순서 뒤집기 가능
# num_list.reverse()
# print(num_list)

# # 모두 지우기
# num_list.clear()
# print(num_list)

# #다양한 자료형 함께 사용
# mix_list = ["조세호", 20, True]
# # print(mix_list)

# #리스트 확장
# num_list.extend(mix_list)
# print(num_list)

# # 사전
# cabinet = {3:"유재석", 100:"김태호"}
# # print(cabinet[3])
# # print(cabinet.get(3))
# # # print(cabinet[5]) <-- 오류
# # print(cabinet.get(5, "사용 가능")) 

# # print(3 in cabinet) # True
# # print(5 in cabinet) # false

# cabinet = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# # 새 손님
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["c-20"] = "조세호"
# print(cabinet)

# # 간 손님
# del cabinet["A-3"]
# print(cabinet)

# # key 들만 출력
# print(cabinet.keys())

# # value 들만 출력
# print(cabinet.values)

# #key, values 쌍으로 출력
# print(cabinet.items())

# # 목욕탕 폐점
# cabinet.clear()
# print(cabinet)

#튜플

# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# # menu.add("생선까스") 튜플은 변겨 ㅇ불가능

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)

# #집합(set)
# #중복 안됨, 순서 없음
# my_set = {1,2,3,3}
# print(my_set)

# Java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# # # 교집합 (Jave 와 python을 모두 할 수 있는 개발자)
# # print(Java & python)
# # print(Java.intersection(python))

# # #합집합 (Java 할 수 있거나 python 할 수 있는 개발자)
# # print(Java | python)
# # # print(Java,union(python))

# #차집합 (Java 할 수 있지만 python 은 할 줄 모르는 개발자)
# print(Java - python)
# print(Java.difference(python))

# # python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# # Java 를 잊었어요
# Java.remove("김태호")
# print(Java)

# 자료구조의 변경
# from tkinter import Menu


# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

# if

# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")

# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp and temp < 10:
#     print("외투를 챙기세요")
# else:
# #     print("너무 추워요. 나가지 마세요")

# # 반복문

# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")

# for waiting_no in range(1, 6):
# # 1, 2, 3, 4, 5
# print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for cutomer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))