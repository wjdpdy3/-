import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier # 최근접 이웃 (기본값 : 5)

# bream 데이터
bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7,
                31.0, 31.0, 31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5,
                34.0, 34.0, 34.5, 35.0, 35.0, 35.0, 35.0, 36.0, 36.0, 37.0,
                38.5, 38.5, 39.5, 41.0, 41.0]
bream_weigth = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0,
                450.0, 500.0, 475.0, 500.0, 500.0, 340.0, 600.0, 600.0,
                700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0,
                925.0, 975.0, 950.0]
# smelt 데이터
smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2,
                12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 
                12.2, 19.7, 19.9]

# 데이터 표로 출력
plt.scatter(bream_length, bream_weigth) # 1
plt.scatter(smelt_length, smelt_weight) # 0
plt.xlabel('length')
plt.ylabel('weigth')
plt.show()

# fish data 준비
length = bream_length + smelt_length
weigth = bream_weigth + smelt_weight
fish_data = [[l,w] for l,w in zip(length, weigth)]

# 정답 데이터 준비 / bream(도미) : 1 , smelt : 0
fish_target = [1] * 35 + [0] * 14

kn = KNeighborsClassifier() # model
kn.fit(fish_data, fish_target) # training
kn.score(fish_data, fish_target) # 얼만큼 잘 학습되었는지? (정확도) / 1.0 : 100%

# 새로운 생선 예측
kn.predict([[30, 600]]) # 2차원으로 입력해야함!

# K = 49 / 주변 sample의 개수
kn49 = KNeighborsClassifier(n_neighbors=49)
kn49.fit(fish_data, fish_target)
kn49.score(fish_data, fish_target) # 71 %