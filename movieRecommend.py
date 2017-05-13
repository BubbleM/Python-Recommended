import csv

fileurl = "./BX-Dump/Movie_Ratings.csv"
users = {}
bands = {}
with open(fileurl) as f:
    reader = csv.reader(f)
    header_row = next(reader) # 电影数组
    del header_row[0] # 删除电影中第一个空字段

    rows = [row for row in reader]
# print(rows[24][25])

for i in range(0,25):
  for j in range(1,26):
    if rows[i][j] == '':
      rows[i][j] = 0
    else:
      rows[i][j] = int(rows[i][j])

for i in range(0,25):
  for j in range(1,26):
    users[rows[i][0]] = bands
    bands[header_row[i]] = rows[i][j]
# print(users['Jaws'])

#计算曼哈顿距离
def manhattan(rating1,rating2):
  distance = 0;
  for key in rating1:
    if key in rating2: # 找到共同评分的乐队
      distance += abs(rating1[key] - rating2[key])
  return distance
# print(manhattan(users["Avatar"],users["Kazaam"])) 
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
# print(recommend("Hailey",users)) 
''' 
[('Phoenix', 4.0), ('Blues Traveler', 3.0), ('Slightly Stoopid', 2.5)]
'''

print(recommend('Star Wars',users))
