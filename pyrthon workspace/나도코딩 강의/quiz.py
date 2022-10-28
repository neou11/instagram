# Quiz 2
#스터디 모임 오프라인으로 하는 날짜 정하기 """

# from random import *


# day = randint(4, 28)
# print(f"오프라인 스터디 모임 날짜는 매월 {day} 일로")

#Quiz 3
#사이트별로 비밀번호를 만들어 주는 프로그램 작성


#규칙1 : http:// 부분은 제외 => naver.com
#규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
# """
# url = "http://naver.com"
# my_str = url.replace("http://", "")
# my_str = my_str[:my_str.index(".")]
# # print(my_str)
# pwd = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0} 의 비밀번호는 {1} 입니다.".format(url, pwd))

#Quiz 4
# from random import *

# users = range(1, 21)
# users = list(users)

# print(users)
# shuffle(users)
# print(users)

# winners = sample(users, 4)
# print(" --당첨자 발표 --")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print(" -- 축하합니다 -- ")
# names = ["나도코딩", "너도코딩", "우리도 코딩"]
# for i in names:
#     file = open(names[i] + ".txt")
# names = ["아이언맨", "토르", "헐크", "아이엠 디버깅"]
# for name in names:
#     with open("{}.txt".format(name), "w", encoding = "utf8") as email_file:
#         email_file.write(f"""안녕하세요? {name}님.

# (주)나도출판 편집자 나코입니다.
# 현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.
# {name}님의 유튜브 영상을 보고 연락을 드리게 되었습니다.
# 자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.

# 좋은 하루 보내세요 ^^
# 감사합니다.

# - 나코 드림.
# """)

