class Classifier:
	def __init__(self,filename):
		self.medianAndDeviation = []
		# 读取文件
		f = open(filename)
		lines = f.readlines()
		f.close()
		# print(lines[0]) #  comment class   num     num
		self.format = lines[0].strip().split('\t')
		# print(self.format) # ['comment', 'class', 'num', 'num']
		self.data = []
		for line in lines[1:]:
			fields = line.strip().split('\t')
			ignore = []
			vector = []
			for i in range(len(fields)):
				if self.format[i] == 'num':
					vector.append(int(fields[i]))
				elif self.format[i] == 'comment':
					ignore.append(fields[i])
				elif self.format[i] == 'class':
					classification = fields[i]
			self.data.append((classification,vector,ignore))
		# print(self.data)
# [('Gymnastics', [54, 66], ['Asuka Teramoto']), ('Basketball', [72, 162], ['Brittainey Raven']),
#  ('Basketball', [78, 204], ['Chen Nan']), ('Gymnastics', [49, 90], ['Gabby Douglas']),
#  ('Track', [65, 99], ['Helalia Johannes']), ('Track', [63, 106], ['Irina Miketenko']), 
#  ('Basketball', [75, 175], ['Jennifer Lacy']), ('Track', [67, 123], ['Kara Goucher']), 
#  ('Gymnastics', [54, 68], ['Linlin Deng']), ('Basketball', [76, 200], ['Nakia Sanford']), 
#  ('Basketball', [68, 163], ['Nikki Blue']), ('Gymnastics', [61, 95], ['Qiushuang Huang']), 
#  ('Gymnastics', [58, 77], ['Rebecca Tunney']), ('Track', [70, 108], ['Rene Kalmer']), 
#  ('Basketball', [70, 155], ['Shanna Crossley']), ('Basketball', [70, 155], ['Shavonte Zellous']), 
#  ('Track', [63, 108], ['Tatyana Petrova']), ('Track', [65, 106], ['Tiki Gelana']), 
#  ('Track', [66, 97], ['Valeria Straneo']), ('Gymnastics', [61, 76], ['Viktoria Komova'])]

		# 添加标准化的过程
		# 获取向量的长度
		self.vlen = len(self.data[0][1])
		# 标准化
		for i in range(self.vlen):
			# print(i) # 0,1
			self.normalizeColumn(i)


	def getMedian(self,alist):
		# 返回中位数
		if alist == []:
			return []
		blist = sorted(alist)
		length = len(alist)
		if length % 2 == 1:
			# 列表有奇数个元素，返回中间的元素
			return blist[int(((length+1)/2)-1)]
		else:
			# 列表中有偶数个元素，返回中间两个元素的均值
			v1 = blist[int(length/2)]
			v2 = blist[(int(length/2)-1)]
			return (v1+v2)/2.0

	def getAbsoluteStandardDeviation(self,alist,median):
		# 计算绝对偏差
		sum = 0;
		for item in alist:
			sum += abs(item-median)
		return sum/len(alist)


	def normalizeColumn(self,columnNumber):
		# 标准化self.data中第columnNumber列
		# 将该列的所有值提取到一个列表中
		# for v in self.data:
		# 	print(v) ('Gymnastics', [54, 66], ['Asuka Teramoto'])
		col = [v[1][columnNumber] for v in self.data]
# 		print(col) 
# [54, 72, 78, 49, 65, 63, 75, 67, 54, 76, 68, 61, 58, 70, 70, 70, 63, 65, 66, 61]
# [66, 162, 204, 90, 99, 106, 175, 123, 68, 200, 163, 95, 77, 108, 155, 155, 108, 106, 97, 76]
		median = self.getMedian(col)
		# print(median) # 65.5  107.0
		asd = self.getAbsoluteStandardDeviation(col,median)
		# print("Median:%f ASD=%f"%(median,asd))
# Median:65.500000 ASD=5.950000
# Median:107.000000 ASD=33.650000
		self.medianAndDeviation.append((median,asd))
		for v in self.data:
			v[1][columnNumber] = (v[1][columnNumber]-median)/asd


	def normalizeVector(self,v):
		# 我们已经保存了每列的中位数和绝对偏差，现用它来标准化向量v
		vector = list(v)
		for i in range(len(v)):
			(median,asd) = self.medianAndDeviation[i]
			vector[i] = (vector[i]-median)/asd
		return vector


	def manhanttan(self,vector1,vector2):
		return sum(map(lambda v1,v2:abs(v1-v2),vector1,vector2))

	def nearestNeighbor(self,itemVector):
		# 返回itemVector的近邻
		return min([(self.manhanttan(itemVector,item[1]),item) for item in self.data])

	def classify(self,itemVector):
		# 预测itemVector的分类
		return self.nearestNeighbor(self.normalizeVector(itemVector))[1][0]

classifier = Classifier('athletesTrainingSet.txt')
print(classifier.classify([70,140])) # Basketball


