'''
冒泡排序（Bubble Sort）
时间复杂度：O(N^2)
空间复杂度：O(1)
算法稳定性：稳定的排序
'''


def buble_sort(data):
    flag = True
    while flag:
        print(data)
        flag = False
        for j in range(1, len(data)):
            if data[j-1] > data[j]:
                data[j-1], data[j] = data[j], data[j-1]
                flag = True


'''
选择排序selection_sort

选择排序和冒泡排序很类似，但是选择排序每轮比较只会有一次交换，
而冒泡排序会有多次交换，交换次数比冒泡排序少，就减少cpu的消耗，
所以在数据量小的时候可以用选择排序，实际适用的场合非常少。

比较性：因为排序时元素之间需要比较，所以是比较排序
稳定性：因为存在任意位置的两个元素交换，所以为不稳定排序。
时间复杂度：我们看到选择排序同样是双层循环n*(n-1))，所以时间复杂度也为：O(n^2)
空间复杂度：只需要常数个辅助单元，所以空间复杂度也为O(1)
'''

def selection_sort(data):
    for i in range(len(data)-1):
        min_index = i
        for j in range(i+1, len(data)):
            if data[min_index] > data[j]:
                min_index = j
        if min_index != i:
            data[i], data[min_index] = data[min_index], data[i]
        print(data)
    return data


'''
inner_sort
简单插入排序同样操作n-1轮，每轮将一个未排序树插入排好序列。
开始时默认第一个数有序，将剩余n-1个数逐个插入。插入操作具体包括：比较确定插入位置，数据移位腾出合适空位
每轮操作O(n)次，共O（n）轮，时间复杂度O(n^2)。
额外空间开销出在数据移位时那一个过渡空间，空间复杂度O(1)。
'''
def inner_sort(data):
    for i in range(1, len(data)):
        for j in range(i):
            if data[i] < data[j]:
                data[i], data[j] = data[j], data[i]
        print(data)


'''
quick_sort
稳定性：快排是一种不稳定排序，打乱了之前的相对顺序
比较性：因为排序时元素之间需要比较，所以是比较排序
时间复杂度：快排的时间复杂度为O(nlogn)
空间复杂度：排序时需要另外申请空间，并且随着数列规模增大而增大，其复杂度为：O(nlogn)

归并排序与快排 ：
    归并排序与快排两种排序思想都是分而治之，但是它们分解和合并的策略不一样：
    归并是从中间直接将数列分成两个，而快排是比较后将小的放左边大的放右边，
    所以在合并的时候归并排序还是需要将两个数列重新再次排序，
    而快排则是直接合并不再需要排序，所以快排比归并排序更高效一些，

快速排序有一个缺点就是对于小规模的数据集性能不是很好。
'''

def quick_sort(data):
    if data:
        mark = data[0]
        little = [m for m in data if m < mark]
        big = [x for x in data if x > mark]
        middle = [m for m in data if m == mark]
        return quick_sort(little) + middle + quick_sort(big)
    else:
        return []


'''
shell_sort
希尔排序(Shell Sort)是插入排序的一种。也称缩小增量排序，是直接插入排序算法的一种更高效的改进版本
最优时间复杂度：根据步长序列的不同而不同 
最坏时间复杂度：O(n^2) 
稳定性：不稳定
'''

def shell_sort(data):
    step = len(data) // 2
    print(data, step)
    while step > 0:
        for i in range(step, len(data)):
            j = i
            while j >= step and data[j - step] > data[j]:
                data[j - step], data[j] = data[j], data[j - step]
                print(data[j], data[j - step])
                print(data)
                j -= step
        print(data, step)
        step //= 2




'''
merge_sort
平均时间复杂度是 O(nlgn)，
最好情况下的时间复杂度是 O(nlgn)，
最坏情况下的时间复杂度也是 O(nlgn)。
它的空间复杂度是 O(1)。
另外，归并排序还是一个稳定的排序算法
'''


def merge(left, right):
    # 合并两个有序列表
    res = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    if left:
        res.extend(left)
    if right:
        res.extend(right)
    return res


def merge_sort(arr):
    # 归并函数
    n = len(arr)
    if n < 2:
        return arr
    middle = n // 2
    left = arr[:middle]     # 取序列左边部分
    right = arr[middle:]    # 取序列右边部分
    # 对左边部分序列递归调用归并函数
    left_sort = merge_sort(left)
    # 对右边部分序列递归调用归并函数
    right_sort = merge_sort(right)
    #
    return merge(left_sort, right_sort)


'''
如果 a+b+c=1000，且 a2+b2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?

start_time = time.time()

注意是三重循环
for a in range(0, 1001):
    for b in range(0, 1001):
        for c in range(0, 1001):
            if a**2 + b**2 == c**2 and a+b+c == 1000:
                print("a, b, c: %d, %d, %d" % (a, b, c))

end_time = time.time()
print("elapsed: %f" % (end_time - start_time))
print("complete!")

a, b, c: 0, 500, 500
a, b, c: 200, 375, 425
a, b, c: 375, 200, 425
a, b, c: 500, 200, 500
elapsed: 214.583347

start_time = time.time()

# 注意是两重循环
for a in range(0, 1001):
    for b in range(0, 1001-a):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print("a, b, c: %d, %d, %d" % (a, b, c))

end_time = time.time()
print("elapsed: %f" % (end_time - start_time))
print("complete!")

a, b, c: 0, 500, 500
a, b, c: 200, 375, 425
a, b, c: 375, 200, 425
a, b, c: 500, 0, 500
elapsed: 0.380109
complete!
'''



if __name__ == '__main__':
    data_sort = [9, 9, 1, 22, 31, 45, 3, 6, 2, 11]
    print('-------------------buble_sort----------------')
    buble_sort(data_sort[:])
    print('-------------------selection_sort----------------')
    selection_sort(data_sort[:])
    print('-------------------inner_sort----------------')
    inner_sort(data_sort[:])
    print('-------------------quick_sort----------------')
    back = quick_sort(data_sort[:])
    print(back)
    print('-------------------shell_sort----------------')
    shell_sort(data_sort[:])
    print('-------------------merge_sort----------------')
    merge_sort(data_sort[:])
