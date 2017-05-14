import csv

fileurl = "./BX-Dump/Movie_Ratings.csv"
with open(fileurl) as f:
    reader = csv.reader(f)
    header_row = next(reader) # 电影数组
    # del header_row[0] # 删除电影中第一个空字段
    rows = [row for row in reader]
# print(header_row)
# print(rows[2])

# 将分数从字符串转换为数值
for row in range(0,25):
  for col in range(1,26):
    if rows[row][col] != '':
      rows[row][col] = int(rows[row][col])
    else:
      rows[row][col] = 0
# print(rows)

# 查找到所有用户并将其保存在一个用户列表users中
users = []
def user():
  for i in range(0,25):
    users.append(rows[i][0])
    # print(rows[i][0])
user()
# print(users)


# 根据用户名查找   并返回该用户所在的行的数据
def findUser(username):
  for row in range(0,25):
      if rows[row][0] == username:
        return  rows[row]
# print(findUser('Old School'))

# 曼哈顿实现计算两个用户之间的距离 并返回距离
def manhattan(username1,username2):
  rating1 = findUser(username1)
  rating2 = findUser(username2)
  distance = 0
  for i in range(1,26):
    if rating1[i] != 0 and rating2[i] != 0:
      distance += abs(rating1[i] - rating2[i])
  return distance
# print(manhattan("Jaws","Gladiator"))


# 编写函数来找到距离最近的用户（返回一个用户列表，按距离排序）
def computeNearestNeighbor(username,users):
  distances = []
  for user in users:
    if user != username:
      distance = manhattan(username,user)
      distances.append((distance,user))
  distances.sort()
  return distances
# print(computeNearestNeighbor("Jaws",users))

# 开始做推荐啦
def recommend(username,users):
  # 找到距离最近的用户
  nearest = computeNearestNeighbor(username,users)[0][1] 
  recommendations = []
  neighborRatings = findUser(nearest) # 取得距离最近的用户的数据
  userRatings = findUser(username) # 取得当前用户的数据
  for i in range(1,26):
    if neighborRatings[i] != 0 and userRatings[i] == 0:
      recommendations.append((header_row[i],neighborRatings[i]))
  return sorted(recommendations,
        key=lambda artistTuple:artistTuple[1],
        reverse=True)


# 输出测试

# print(recommend("Old School",users))
# 输出[('Stephen', 5), ('aaron', 4), ('Josh', 3)]

# print(recommend("Jaws",users))
# 输出[('Patrick C', 1), ('Zak', 1)]

# print(recommend("Village",users))
# 输出[('aaron', 3), ('Jonathan', 2), ('Amy', 2), ('Patrick C', 1), ('Gary', 1)]

print(recommend("Alien",users))
# 输出[('Heather', 4), ('vanessa', 4), ('greg', 4), ('ben', 4), ('Jonathan', 4), ('Valerie', 4), ('Zak', 3)]
