
from functools import wraps

def xx(fun):
    print('------xx-----')
    @wraps(fun)
    def wp(*args, **kwargs):
        print('-----wp-----')
        # fun(*args, **kwargs)
        # return fun(*args, **kwargs)
    return wp


# @xx
def aa():
    print('-----aa------')


# aa()
b = [2,6,4,8,10]
for i in b:
    if i % 2 == 0:
        b.remove(i)
print(b)

