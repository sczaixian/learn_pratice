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
        return quick_sort(little) + [mark] + quick_sort(big)
    else:
        return []


'''
shell_sort
'''

def shell_sort(data):
    pass








if __name__ == '__main__':
    data_sort = [9, 1, 22, 31, 45, 3, 6, 2, 11]
    print('-------------------buble_sort----------------')
    buble_sort(data_sort[:])
    print('-------------------selection_sort----------------')
    selection_sort(data_sort[:])
    print('-------------------inner_sort----------------')
    inner_sort(data_sort[:])
    print('-------------------quick_sort----------------')
    quick_sort(data_sort[:])


