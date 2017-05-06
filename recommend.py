import codecs #导入自然语言编码转换包
from math import sqrt
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
        } 
class recommender:
   def __init__(self,data,k=1,metric='pearson',n=5):
      """ 初始化推荐模块
      data 训练数据
      k    k邻近算法中的值
      metric  使用何种距离计算方式
      n  推荐结果的数量
      """
      self.k = k
      self.n = n
      self.username2id = {}
      self.userid2name = {}
      self.productid2name = {}
      #将距离计算方式保存下来
      self.metric = metric
      if self.metric == 'pearson':
         self.fn = self.pearson
      #
      # 如果data是一个字典类型，则保存下来，否则忽略
      #
      if type(data).__name__ == 'dict':
         self.data = data

   def convertProductID2name(self,id):
      '''通过产品ID获取名称'''
      




      