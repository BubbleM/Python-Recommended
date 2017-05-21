import codecs 
from math import sqrt

users2 = {"Amy": {"Taylor Swift": 4, "PSY": 3, "Whitney Houston": 4},
          "Ben": {"Taylor Swift": 5, "PSY": 2},
          "Clara": {"PSY": 3.5, "Whitney Houston": 4},
          "Daisy": {"Taylor Swift": 5, "Whitney Houston": 3}}

class recommender:
   def __init__(self, data):

      self.productid2name = {}

      self.frequencies = {} 
      # 同时评价乐队i和j的用户数 嵌套的字典
      # {
      # 'Taylor Swift': {'PSY': 2, 'Whitney Houston': 2}, 
      # 'PSY': {'Taylor Swift': 2, 'Whitney Houston': 2}, 
      # 'Whitney Houston': {'Taylor Swift': 2, 'PSY': 2}
      # }

      self.deviations = {}
      # 乐队i与乐队j之间的偏差 嵌套的字典
      # {
      # 'Taylor Swift': {'PSY': 2.0, 'Whitney Houston': 1.0}, 
      # 'PSY': {'Taylor Swift': -2.0, 'Whitney Houston': -0.75},
      # 'Whitney Houston': {'Taylor Swift': -1.0, 'PSY': 0.75}
      # }

   
      if type(data).__name__ == 'dict':
         self.data = data

   def convertProductID2name(self, id):
      """Given product id number return product name"""
      if id in self.productid2name:
         return self.productid2name[id]
      else:
         return id

   # 计算所有物品对之间的偏差
   def computeDeviations(self):
     # 获取每位用户的评分数据
      for ratings in self.data.values():
# print(ratings)
# print("-----------")

# {'Taylor Swift': 5, 'Whitney Houston': 3}
# -----------
# {'Taylor Swift': 5, 'PSY': 2}
# -----------
# {'Taylor Swift': 4, 'PSY': 3, 'Whitney Houston': 4}
# -----------
# {'PSY': 3.5, 'Whitney Houston': 4}
# -----------
         # 遍历该用户的每个评分项
         for (item, rating) in ratings.items():
            self.frequencies.setdefault(item, {})
            self.deviations.setdefault(item, {})                    
          # 再次遍历该用户的每个评分项
            for (item2, rating2) in ratings.items():
               if item != item2:
                  self.frequencies[item].setdefault(item2, 0)
                  self.deviations[item].setdefault(item2, 0.0)
                  # 如果该用户同时对item和item2乐队都评分了  频数+1
                  self.frequencies[item][item2] += 1
                  # 计算评分的差异保存在变量中
                  self.deviations[item][item2] += rating - rating2
      
      # 计算差异总和除以频数并保存在变量中
      for (item, ratings) in self.deviations.items():
         for item2 in ratings:
            ratings[item2] /= self.frequencies[item][item2]

   # 推荐逻辑的实现
   def slopeOneRecommendations(self, userRatings):
      recommendations = {}
      frequencies = {}

      # 遍历目标用户的评分项 userItem是乐队 userRating是该用户对乐队的打分
      for (userItem, userRating) in userRatings.items():

         # 对目标用户未评价的歌手进行计算
         # deviations现在存的是所有物品对之间的偏差
         for (diffItem, diffRatings) in self.deviations.items():

            # 用户没有对diffItem打分  所以diffItem是潜在的可以推荐给该用户的乐队
            # diffItem为j  userItem是i 偏差就是deviations[diffItem][userItem]
            if diffItem not in userRatings and \
               userItem in self.deviations[diffItem]:
               freq = self.frequencies[diffItem][userItem] # 共同对diffItem和userItem打分的用户数
               recommendations.setdefault(diffItem, 0.0) # 推荐预测
               frequencies.setdefault(diffItem, 0) # 频数
               # 计算分子
               recommendations[diffItem] += (diffRatings[userItem] +
                                             userRating) * freq
               # 计算分母
               frequencies[diffItem] += freq

      recommendations =  [(self.convertProductID2name(k),
                           v / frequencies[k])
                          for (k, v) in recommendations.items()]
      # 排序并返回
      recommendations.sort(key=lambda artistTuple: artistTuple[1],
                           reverse = True)
      # I am only going to return the first 50 recommendations
      return recommendations[:50]

r = recommender(users2)
r.computeDeviations()
# print(r.deviations)
print(r.slopeOneRecommendations(users2['Ben']))
