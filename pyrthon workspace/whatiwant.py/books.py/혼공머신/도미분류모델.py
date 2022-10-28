import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier()

# 도미 데이터
bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]

# 빙어 데이터 
smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

# 도미와 빙어의 길이와 무게에 관한 산점도 
plt.scatter(bream_length, bream_weight)
plt.scatter(smelt_length, smelt_weight)
plt.xlabel("length")
plt.ylabel("weight")
# plt.show()

# fish_data 만들기
fish_legnth = bream_length + smelt_length
fish_weight = bream_weight + smelt_weight
fish_data = [[l, w] for l, w in zip(fish_legnth, fish_weight)]
fish_target = [1] * 35 + [0] * 14

# 훈련세트와 테스트세트 만들기
train_input = fish_data[:35]
train_target = fish_target[:35]
test_input = fish_data[35:]
test_target = fish_target[35:]

# 훈련하고 score 함수로 확인
# kn = kn.fit(train_input, train_target)
# print(kn.score(test_input, test_target)) # -> 0.0

# 훈련셋과 테스트 셋이 전혀 다른것이 샘플링 편향 

# 넘파이 배열 생성
input_arr = np.array(fish_data)
target_arr = np.array(fish_target)

# print(input_arr)
# print(input_arr.shape)

np.random.seed(42)
index = np.arange(49)
# print(index)

# create train sets
train_input = input_arr[index[:35]]
train_target = target_arr[index[:35]]

# create test sets
test_input = input_arr[index[35:]]
test_target = target_arr[index[35:]]







