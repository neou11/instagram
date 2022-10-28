# 방역프로그램(메세지 자동응답)
name = input("격리자의 성함을 입력하세요: ")
birth = input("확진자의 생년월일을 입력하세요\n(YY.MM.DD): ")
gender = input("격리자의 성별을 입력하세요\n(예: 남/여): ")
print(name + "님", "(" + (birth + "/" + gender) + ")" + "\n다음 물음에 O, X 만으로 사실을 답하여 주시길 바랍니다.")
anslist = []
print("기침과 가래가 섞여 나온다.")
ans = input("")
anslist.append(ans)
print("37.5도 이상의 고열이 지속된다")
ans = input("")
anslist.append(ans)
print("두통이 심하다")
ans = input("")
anslist.append(ans)

if (ans[0:4] == "O"): 
    print("댁으로 구급차를 보내는 중입니다. 협조 부탁드립니다.")
else: 
    print("적극적 협조에 감사드립니다.")