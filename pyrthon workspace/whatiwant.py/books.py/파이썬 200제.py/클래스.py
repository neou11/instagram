# class MyClass:
#     var = "안녕하세요"
#     def sayHello(self):
#         print(self.var)
#     def PlusOne(i):
#         try:
#             int(i)
#             print(i + 1)
#         except:
#             print("정수를 입력하세요.")
# obj = MyClass()
# print(obj.var)
# obj.sayHello()

# int = MyClass()
# print(int.var)



class Player:
    def __init__(self, name, health, skill):
        self.name = name
        self.health = health
        self.skill = skill
        self.xp = 0
    def Intro(self):
        return f"Hi, my name is {self.name} and my skill is {self.skill}"
    def takehit(self):
        self.health -= 5



bill = Player("Bill Gates", 85, "Pfogrammer")
elon = Player("Elon Musk", 90, "Legend")
warren = Player("Warren Buffett", 100, "Investor")

print(warren.health)
print(warren.Intro())


class Human:
    def __init__(self, name):
        self.name = name
        self.arms = 2
        self.legs = 1
class Baby(Human):
     def __init__(self, name):
        self.cute = True
brother = Baby("brother")
print(brother.cute)

class Add:
    def add(self, n1, n2):
        return n1 + n2

class Calculator(Add):
    def sub(self, n1, n2):
        return n1 - n2

obj = Calculator()
print(obj.add(1, 2))
print(obj.sub(1, 2))






