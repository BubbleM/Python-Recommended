users = {"Amy": {"Taylor Swift": 4, "PSY": 3, "Whitney Houston": 4},
          "Ben": {"Taylor Swift": 5, "PSY": 2},
          "Clara": {"PSY": 3.5, "Whitney Houston": 4},
          "Daisy": {"Taylor Swift": 5, "Whitney Houston": 3}}

# 首先计算两两物品间的差异
def computeDeviations(self):
	# 获取每位用户的评分数据
	for ratings in self.data.values():
		# 对于该用户的每个评分项（歌手，分数）
		for(item,rating) in ratings.items():
			# setdefault()接受两个参数，如果字典中不包含指定的键，则将其设置为默认值；若存在，则返回其对应的值
			self.frequencies.setdefault(item,{})
			self.deviations.setdefault(item,{})
			
			# 再次遍历该用户的每个评分项
			for(item2,rating2) in ratings.items():
				if item != item2:
					# 将评分的差异保存在变量中
					self.frequencies[item].setdefault(item2,0)
					self.deviations[item].setdefault(item2,0.0)
					self.deviations[item][item2] += 1
					self.deviations[item][item2] += rating - rating2

	# 计算出差异值
	for(item,ratings) in self.deviations.items():
		for item2 in ratings:
			ratings[item2] /= self.frequencies[item][item2]


