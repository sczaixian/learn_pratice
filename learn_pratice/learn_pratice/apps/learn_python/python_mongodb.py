
import pymongo
import os
import random


print('-------------------------mongodb----------------------------------')
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
print(myclient)

mydb = myclient['runoobdb']
print(mydb)
dblist = myclient.list_database_names()
print(dblist)
if 'runoobdb' in dblist:
    print('database is already exists!!')
else:
    print('is ok!!')
mycol = mydb["sites"]
print(mycol)

# INSERT INTO  Databases
mydict = { "name": "RUNOOB", "alexa": "100090", "url": "https://www.runoob.com" }
x = mycol.insert_one(mydict)
print(x)
print(x.inserted_id)

mylist = [
  { "name": "Taobao", "alexa": "100", "url": "https://www.taobao.com" },
  { "name": "QQ", "alexa": "101", "url": "https://www.qq.com" },
  { "name": "Facebook", "alexa": "10", "url": "https://www.facebook.com" },
  { "name": "知乎", "alexa": "103", "url": "https://www.zhihu.com" },
  { "name": "Github", "alexa": "109", "url": "https://www.github.com" }
]

y = mycol.insert_many(mylist)
print(y.inserted_ids)


# FIND DATA From Databases
x = mycol.find_one()
print(x)

for x in mycol.find({},{'_id':0, 'name':1, 'alexa':1}):
    print(x)

# myquery = {'name':'QQ'}
myquery = { "name": { "$regex": "^R" } }
# myquery = { "name": { "$gt": "H" } }
myresult = mycol.find(myquery).limit(1)
print(myresult)
for x in myresult:
#     print(x, end= ' ')
    print(x)

# UPDATE DATA  INTO Databases
myupdatequery = {'alexa':'10000'}
newvalue = {'$set':{'alexa':'123'}}
mycol.update_one(myupdatequery, newvalue)
for x in mycol.find():
    print(x)

myupdatequery = {'name':{'$regex':'^F'}}
newvalue = {'$set':{'alexa':'10086'}}
x = mycol.update_many(myupdatequery, newvalue)
print(x.modified_count, 'update ok!!')


# sort
mysortdata = mycol.find().sort('alexa', -1)
for x in mysortdata:
    print(x)

# # # delete data
# # # mydeletequery = {'name':'QQ'}
# # # mycol.delete_one(mydeletequery)
# # # # 删除后输出
# # # for x in mycol.find():
# # #   print(x)
# #
# # mydeletequery = { "name": {"$regex": "^F"} }
# # x = mycol.delete_many(mydeletequery)
# # print(x.deleted_count, "个文档已删除")
#
# x = mycol.delete_many({})
# print(x.deleted_count, "个文档已删除")

mycol.drop()





