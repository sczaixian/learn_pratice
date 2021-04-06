



# #列表
# a = ['a', 'b']
# b = [1, 2]
#
# print(dict(zip(a, b)))
# {'a': 1, 'b': 2}
# #元组
# fields = ('id', 'name', 'age')
# records = [['01', 'Bill', '20'], ['02', 'Mike', '30']]
# result = []
# '''
# [
# {'id': '01', 'name': 'Bill', 'age': '20'}
# {'id': '02', 'name': 'Mike', 'age': '30'}
# ]
# '''
#
# for record in records:
#     result.append(dict(zip(fields, record)))
# print(result)
# [{'id': '01', 'name': 'Bill', 'age': '20'}, {'id': '02', 'name': 'Mike', 'age': '30'}]


#排序列表的方法
a = [3, 2, 5, 8, 7, 9, 11]
a.sort()
print(a)	# [2, 3, 5, 6, 7, 9, 11]

b = [3, 2, 5, 8, 7, 9, 11]
c = sorted(b)
print(b)	# [2, 3, 5, 6, 7, 9, 11]
'''
区别：
1.sort属于列表方法，sorted是独立函数
2.sort改变列表本身，sorted返回一个排好序的列表副本
'''

#倒叙排列列表
a.sort(reverse= True)
print(a)

print(sorted(b, reverse= True))






