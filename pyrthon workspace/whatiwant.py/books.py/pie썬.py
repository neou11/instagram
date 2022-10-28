# 09 첫 번째 정수를 입력하시오: 300
# 첫 번째 정수를 입력하시오: 400
# 300과 400의 합은 700입니다.
# x = int(input("첫 번째 정수를 입력하시오: "))
# x = int(input("첫 번째 정수를 입력하시오: ")) 
# print(x) 



# 사용자로부터 2개의 정수를 받아서 사칙연산(+, -, *, /)을 한 후에 결과를 출력하는 프로그램을 작성해보자

# x = input(int("첫 번째 정수를 입력하시오: "))
# y = input(int("두 번째 정수를 입력하시오: "))


# CH.2 10 사용자로부터 문자열 입력받기

# name = input("이름을 입력하시오: ") 
# print(name + "씨, 안녕하세요?") 
# print("파이썬에 오신 것을 환영합니다.") 
# x = int(input("첫 번째 정수를 입력하시오: ")) 
# y = int(input("두 번째 정수를 입력하시오: ")) 
# sum = int(x + y) 
# print(x, "와", y, "의 합은", sum, "입니다.") 

# ===================================================

# 야구 기사 자동화

# stadium = input("경기장은 어딥니까? ")
# winner = input("이긴 팀은 어딥니까? ")
# looser = input("진 팀은 어딥니까? ")
# mvp = input("우수선수는 누구입니까? ")
# score = input("스코어는 몇대몇입니까? ")


# print("오늘", stadium, "에서 야구경기가 열렸습니다.")
# print(winner, "과",  looser, "은 치열한 공방전을 펼쳤습니다.")
# print(mvp, "이 맹활약을 하였습니다.")
# print("결국", winner, "가", looser, "를", score, "로 이겼습니다.")

# 연습문제

# 1.

# name = input("이름을 입력하시오: ")
# age = int(input("나이를 입력하시오: "))
# print(name + "씨는", str(100 - age + 2022) + "년도에 100살이시네요!")

# 2.

# x = int(input("첫 번째 정수를 입력하시오: "))
# y = int(input("두 번째 정수를 입력하시오: "))
# z = int(input("세 번째 정수를 입력하시오: "))
# print((str(x) + str(y) + str(z)), "의 평균은", ((x + y + z)/3), "입니다.")

# 3.

# x = int(input("원의 반지름을 입력하시오: "))
# print("반지름이", str(x), "인 원의 넓이 =", str(x**2*3.141592))

# 커피 가게 매출 계산하기

# a = 2000 # 아메리카노 금액
# b = 3000 # 카페라테 금액
# c = 3500 # 카푸치노 금액

# x = int(input("아메리카노의 판매 개수: "))
# y = int(input("카페라테의 판매 개수: "))
# z = int(input("카푸치노의 판매 개수: "))
# g = int(a*x + b*y + c*z)

# print("총 매출은", g,  "입니다.")

# k = int(input("총 재료비용: "))
# print(g - k)
# if((g - k) > 0): print("흑자")
# if((g - k) < 0): print("적자")

# 자동판매기 프로그램

# money = int(input("투입한 돈: "))
# price = int(input("물건값: "))

# change = int(money - price)
# coin500s = int(change//500)
# coin100s = int(change%500/100)

# print("500원 동전의 개수:", big)
# print("100원 동전의 개수:", small)

# 거북이와 인사해보자

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# s = turtle.textinput("", "이름을 입력하시오: ")
# t.write("안녕하세요? 터틀 인사드립니다.")

# CH.4 13 문자열에서 개별 문자들을 추출하려면?(인덱스)

# s = "montypython"
# print(s[6:10])
# print(s[0])
# t = "person"
# print(t[0:5])

# CH.4 14 특수문자열

# print("말 한마디로\n천 냥 빚을 갚는다")
# print("말 한마디로\\천 냥 빚을 갚는다")
# print("말 한마디로\t천 냥 빚을 갚는다")
# print("말 한마디로\"천 냥 빚을 갚는다")
# print("말 한마디로\'천 냥 빚을 갚는다")

# CH.4 LAB 친근하게 대화하는 프로그램

# name = input("안녕하세요?\n이름이 어떻게 되시나요? ")
# print("만나서 반갑습니다." + name + "씨")
# length = len(name)
# print("이름의 길이는 다음과 같군요:", length)
# age = int(input("나이가 어떻게 되나요? "))
# after = (age + 1)
# print("내년이면", after, "이 되시는군요.")
# hobby = input("취미가 무엇인가요? ")
# print("네 저도", hobby, "좋아합니다.")

# CH.4 LAB 2050년에는 몇 살이 될까?

# import time
# now = time.time()
# thisYear = int(1970 + now//(365*24*3600))
# print("올해는 " + str(thisYear)+"입니다.")
# age = int(input("몇 살이신지요? "))
# print("2050년에는", str(age + (2050 - int(thisYear))), "살 이시군요.")

# CH.4 리스트란?
# gh = ['영어', '수학', '사회', '과학']
# print(gh)
# print(gh[0], end = " ")
# print(gh[2:4])

# CH.4 LAB 친구들의 리스트 생성하기

# friend_list = []
# friend = input("친구를 입력하시오: ")
# friend_list.append(friend)
# friend = input("친구를 입력하시오: ")
# friend_list.append(friend)
# friend = input("친구를 입력하시오: ")
# friend_list.append(friend)
# friend = input("친구를 입력하시오: ")
# friend_list.append(friend)
# friend = input("친구를 입력하시오: ")
# friend_list.append(friend)

# print(friend_list)

# CH.4 연습문제

# print("나는 " + str(12) + "개의 사과를 먹었다.")

# str = input("문자열을 입력하시오: ")
# print(str[:2] + str[-2:])

# whatimdoing = input("당신이 현재 하는것을 입력하시오: ")
# print(whatimdoing + "하는 중")

# str = [input("기호를 입력하시오: ")] 
# str_1 = input("중간에 삽입할 문자열을 입력하시오: ")
# prin = (str.append(str_1))
# print(prin)


# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# list = []
# color = input("색상 #1을 입력하시오: ")
# list.append(color)
# color = input("색상 #2를 입력하시오: ")
# list.append(color)
# color = input("색상 #3을 입력하시오: ")
# list.append(color)
# t.fillcolor(list[0])
# t.begin_fill()
# t.circle(50)
# t.end_fill()
# t.goto(50,50)
# t.fillcolor(list[1])
# t.begin_fill()
# t.circle(50)
# t.end_fill()
# t.goto(150,50)
# t.fillcolor(list[2])
# t.begin_fill()
# t.circle(50)
# t.end_fill()

# CH.5 6_if-else 문으로 예제를 작성해보자

# score = int(input("점수를 입력하시오: "))
# if score >= 60 :
#     print("합격입니다.")
# else :
#     print("불합격입니다.")

# num = int(input("정수를 입력하시오: "))
# if num % 2 == 0 :
#     print("짝수입니다.")
# else : 
#     print("홀수입니다.")

# score = int(input("점수를 입력하시오: "))
# if score >= 90 : 
#     print("합격입니다.")
#     print("장학금도 받을 수 있습니다.")
# else : 
#     print("불합격입니다.\n지원해주셔서 감사합니다.")

# CH.5 LAB 정수의 부호에 따라 거북이를 움직이자

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")

# t.penup()
# t.goto(100, 100)
# t.write("거북이가 여기로 오면 양수입니다.")
# t.goto(100, 0)
# t.write("거북이가 여기로 오면 0입니다.")
# t.goto(100, -100)
# t.write("거북이가 여기로 오면 음수입니다.")

# t.goto(0, 0)
# t.pendown()
# s = turtle.textinput("", "숫자를 입력하시오: ")
# n = int(s)
# if ( n > 0):
#     t.goto(100, 100)
# if ( n == 0):
#     t.goto(100, 0)
# if ( n < 0):
#     t.goto(100, -100)

# CH.5 LAB 영화 나이 제한 검사

age = int(input("나이를 입력하시오: "))
if ( age >= 15):
    print("이 영화를 보실 수 있습니다.")
    print("영화의 가격은 10,000원입니다.")
else:
    print("이 영화를 보실 수 없습니다.\n다른 영화를 보시겠어요?")