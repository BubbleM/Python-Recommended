users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0,
						 "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill":     {"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, 
         				"Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Chan":     {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0,
         		 		"Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dan":      {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, 
         				"Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey":   {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0,
         				 "Vampire Weekend": 1.0},
         "Jordyn":   {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, 
         				"Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam":      {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0,
         		 		"Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5,
         		 		"The Strokes": 3.0}
        } # 用字典形式保存数据

#print(users["Veronica"]); # 获取某个用户的评分  *********************会发现每次输出的顺序都不一样

#计算曼哈顿距离
def manhattan(rating1,rating2):
	distance = 0;
	for key in rating1:
		if key in rating2: # 找到共同评分的乐队
			distance += abs(rating1[key] - rating2[key])
	return distance

#print(manhattan(users["Hailey"],users["Veronica"])) 
# 输出2.0 


#编写函数来找到距离最近的用户（返回一个用户列表，按距离排序）
def computeNearestNeighbor(username,users):
	"""计算所有用户至unername用户的距离，倒序排列并返回结果列表"""
	distances = []
	for user in users:
		if user != username:
			distance = manhattan(users[user],users[username])
			distances.append((distance,user))
	# 按距离排序——距离近的排在前面
	distances.sort()
	return distances

#print(computeNearestNeighbor("Hailey",users))
""" 
[(2.0, 'Veronica'), (4.0, 'Chan'), (4.0, 'Sam'), (4.5, 'Dan'), (5.0, 'Angelica'), 
(5.5, 'Bill'), (7.5, 'Jordyn')]
"""

#开始做推荐
def recommend(username,users):
	nearest = computeNearestNeighbor(username,users)[0][1] # 找到距离最近的用户
	recommendations = []
	neighborRatings = users[nearest] # 取得距离最近的用户的所有评价数据
	userRatings = users[username] # 当前用户的所有评价数据
	for artist in neighborRatings:
		if not artist in userRatings: #找到最近用户评价过而自己没有评价的乐队
			recommendations.append((artist,neighborRatings[artist]))
	return sorted(recommendations,
				key=lambda artistTuple:artistTuple[1],                                    #/**************/
				reverse=True) #按评分进行排序
print(recommend("Hailey",users)) 
''' 
[('Phoenix', 4.0), ('Blues Traveler', 3.0), ('Slightly Stoopid', 2.5)]
'''


#计算闵可夫斯基距离
def minkowski(rating1,rating2,r):
	distance = 0
	for key in rating1:
		if key in rating2:
			distance += pow(abs(rating1[key] - rating2[key]),r)
	return pow(distance,1.0/r)
distance = minkowski(users[user],users[username],2) #使用欧几里德距离 

