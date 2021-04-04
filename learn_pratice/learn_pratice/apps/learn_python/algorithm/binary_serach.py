

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


data = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_serach(data, 3))
print(binary_serach(data, 13))
print(data[4])


def binary_serach(data, item):
    mid = len(data) // 2
    if data[mid] == item:
        return mid
    elif data[mid] > item:
        return binary_serach(data[:mid], item)
    else:
        return binary_serach(data[mid+1:], item)
