import time

def test1(n):
    lst = []
    t1 = time.time()
    for i in range(n * 10000):
        lst = lst + [i]
    t2 = time.time()
    return t2 - t1

def test2(n):
    lst = []
    t1 = time.time()
    for i in range(n * 10000):
        lst.append(i)
    t2 = time.time()
    return t2 - t1

def test3(n):
    t1 = time.time()
    [i for i in range(n * 10000)]
    t2 = time.time()
    return t2 - t1

def test4(n):
    t1 = time.time()
    list(range(n * 10000))
    t2 = time.time()
    return t2 - t1

print(test1(10))
print(test2(10))
print(test3(10))
print(test4(10))


def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()