from db import db_douguo_mongo
import pandas as pd

### 分析那种菜谱做的人最多:
df = pd.read_csv('./douguo_table.csv')

# df2 = df.recipe_title.value_counts()

# print(df2)
### 结果是：
# 可乐鸡翅         257
# 西红柿炒鸡蛋       256
# 糖醋排骨         254
# 红烧茄子         252
# 酸辣土豆丝        250

print(df.practiced. max())

print(df[df['practiced'].isin([df.practiced. max()])])

# 120  206667   stta小铭  可乐鸡翅[简单到没下过厨也会做]      17001   642417   切墩(初级)   10~30分钟   4.8



####################test Python API for mongodb####################### 
# df=db_douguo_mongo.db_douguo
# result=df.find_one({"username":"美国厨娘"})

# result1=df.find({"username":"美国厨娘"})
# print(result)

# result2=df.find({},"username")

# for i in result1:
#     print(i)

# for i in result2:
#     print(i)    





