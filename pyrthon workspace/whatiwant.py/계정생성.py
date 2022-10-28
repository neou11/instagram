aname = input("생성할 계정의 이름을 입력하세요> ")

while True:
    ajob = input("""
    직업을 선택하세요. (검사, 궁수)> 
    """)
    if ajob != "검사" or ajob != "궁수":
        print("검사, 궁수 중 하나만 선택하세요.")
    elif ajob == "검사" or ajob == "궁수":
        break
class Account:
    def __init__(self, name, job):
        self.name = name
        self.job = job



account = Account(aname, ajob)
print(account.name)
print(account.job)

