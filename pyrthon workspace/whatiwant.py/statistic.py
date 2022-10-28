print("-" * 8)
print("")
print("사용방법")
print("")
print("정수를 입력 한 후 모든 정수를 입력하였으면, enter를 눌러 자료 기입을 완료하세요.")
print("")
print("-" * 8)
i = 0
final_list = []
while 0 == 0:
    x = input("실수를 입력하시오> ")
    if x == "":
        break
    elif x[0] == ".":
        print("=" * 8)
        print("")
        print("제대로 된 실수를 입력해주세요!!")
        print("")
        print("=" * 8)
        continue
    try:
        x = float(x)
        final_list.append(x)
    except:
        print("=" * 8)
        print("")
        print("문자열은 입력이 안됩니다!!")
        print("")
        print("=" * 8)
        continue
print(f"평균은 {sum(final_list) / len(final_list)} 입니다")
