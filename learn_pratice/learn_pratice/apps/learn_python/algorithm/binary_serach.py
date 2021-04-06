


# data = [0, 1, 2, 8, 13, 17, 19, 32, 42]
data = [1, 2, 3, 6, 9, 9, 11, 22, 31, 45]

def binary_serach(data, item):
    first, last = 0, len(data) - 1

    while first <= last:
        mid = (first + last) // 2
        if data[mid] == item:
            return mid
        elif data[mid] > item:
            last = mid - 1
        else:
            first = mid + 1


# print(binary_serach(data[:], 3))
# print(binary_serach(data[:], 11))
# print(data[4])

#
# def binary_serach(data, item):
#     mid = len(data) // 2
#     if mid == 0:
#         return None
#     elif data[mid] == item:
#         return mid
#     elif data[mid] > item:
#         return binary_serach(data[:mid], item)
#     else:
#         return binary_serach(data[mid:], item)


def binary_serach_recursion(data, item, first, last):

    middle = (first + last)//2

    if data[-1] < item or data[0] > item or middle == 0:
        return None
    elif data[middle] == item:
        return middle
    elif data[middle] < item:
        first = middle + 1
    else:
        last = middle - 1
    return binary_serach_recursion(data,item, first, last)


print(binary_serach_recursion(data[:], 3, 0, len(data)-1))
print(binary_serach_recursion(data[:], 11, 0, len(data)-1))
