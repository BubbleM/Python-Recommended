from math import sqrt

users = {"David": {"Imagine Dragons": 3, "Daft Punk": 5,
                    "Lorde": 4, "Fall Out Boy": 1},
          "Matt": {"Imagine Dragons": 3, "Daft Punk": 4,
                   "Lorde": 4, "Fall Out Boy": 1},
          "Ben": {"Kacey Musgraves": 4, "Imagine Dragons": 3,
                  "Lorde": 3, "Fall Out Boy": 1},
          "Chris": {"Kacey Musgraves": 4, "Imagine Dragons": 4,
                    "Daft Punk": 4, "Lorde": 3, "Fall Out Boy": 1},
          "Tori": {"Kacey Musgraves": 5, "Imagine Dragons": 4,
                   "Daft Punk": 5, "Fall Out Boy": 3}}

def computeSimilarity(band1,band2,userRatings):
	averages = {}
	# 获得每个用户的平均打分情况
	for (key,ratings) in userRatings.items():
		averages[key] = (float(sum(ratings.values())) / len(ratings.values()))

	num = 0 # 分子
	dem1 = 0 #分母的前部分
	dem2 = 0
	for(user,ratings) in userRatings.items():
		# 找到对band1和band2两支乐队都打分的用户
		if band1 in ratings and band2 in ratings:
			avg = averages[user]  # 取得该用户的评价打分数
			num += (ratings[band1] - avg) * (ratings[band2] - avg)
			dem1 += (ratings[band1] - avg) ** 2
			dem2 += (ratings[band2] - avg) ** 2
	return num / (sqrt(dem1) * sqrt(dem2))

print(computeSimilarity('Kacey Musgraves', 'Lorde', users))
# 输出 0.320959291340884

