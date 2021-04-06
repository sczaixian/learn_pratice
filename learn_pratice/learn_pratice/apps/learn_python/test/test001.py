

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
        yield a

for i in fib(10):
    print(i, end=' ')


class Fib(object):
    def __init__(self, n):
        self.a = 0
        self.b = 1
        self.current = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n >= self.current:
            self.a, self.b = self.b, self.a + self.b
            return self.a
        else:
            return "stop_itr"


f = Fib(10)
for i in range(5):
    print(next(f))


def bin_sersch(data, item):
    left, right = 0, len(data)-1
    if (data[0] > item) and (data[-1] < item):
        return None
    while left <= right:
        middle = (left + right) // 2
        if data[middle] == item:
            return middle
        elif data[middle] < item:
            left = middle + 1
        else:
            right = middle - 1


data_serach = [1, 2, 3, 6, 9, 9, 11, 22, 31, 45]
print(bin_sersch(data_serach[:], 11))