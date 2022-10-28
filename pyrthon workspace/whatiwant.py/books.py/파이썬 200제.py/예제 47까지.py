i = 0
while i < 10:
    i += 1
    if i < 3:
        continue
    print(i)
    if i > 7:
        break
x = 1
total = 0
while 1:
    total = total + x
    if total > 100000:
        print(x)
        print(total)
        break
    x += 1
i = "true"; x = "false"
print(3, end=''); print(30)

cl = 1 + 7j
print(cl.real); print(cl.imag)
c2 = complex(2, 3)
print(c2)

# 순서를 가지고 나열되어 있는것을 시퀀스 자료형이라 칭함 
# 문자열, 리스트, 튜플이 시퀀서 자료형 

strdata = """
I love you
"""

print("나는 %d 보다 %d가 더 좋아"%(3, 5))
print("안녕 내 이름은 %s이야 너의 이름은 %s이니?"%("파이썬", "무엇"))

from time import sleep
for i in range(100):
    msg = "\r진행률 %d%%"%(i + 1)
    print(" " * len(msg), end='')
    print(msg, end='')
    sleep(0.01)

for i in range(100):
    msg = "\rHi %d%%"%(i + 1)
    print(" " * len(msg), end='')
    print(msg, end='')
    sleep(0.01)

for e in range(100):
    msg = "\rdownloading... %d%%"%(e + 1)
    print(" " * len(msg), end='')
    print(msg, end='')
    sleep(0.01)

def hello():
    return 0
list = [0, 1, hello]
print(type(list))
print(list[2]())

tuple = (1, 2, print)
print(tuple[2]("안녕하세요"))

from mypackage import mylib as ml
ret1 = ml.add_txt("대한민국", "1등")
ret2 = ml.reverse("a", "b", "c")
print(ret1)
print(ret2)








