# Python-Recommended

> a simple Recommended by Python

## 任务描述
- 实现一个简单的基于用户的推荐系统类

### 实现细节
- 协调过滤：利用他人的喜好累进行推荐
主要需要解决问题：求出相似度最近的用户，即求最近距离的用户
- 曼哈顿距离
- 欧几里得距离
- 闵可夫斯基距离
- 皮尔逊相关系数
- 余弦相似度
- K最邻近算法

### 总结
如果数据存在“分数膨胀”，即数据贬值问题（很多用户的评定标准不同产生），就用皮尔逊相关系数 
如果数据比较“密集”，变量之间基本都有公有值，且这些距离数据是非常重要的，那就使用欧几里德或曼哈顿距离 
如果数据是稀疏的，即数据集的缺失值较多的情况下，则使用余弦相似度