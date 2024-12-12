import itertools
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x : x<=10 , natuals)
for n in ns:
    print(n)

cs = itertools.cycle("hello ziio")
for n in range(20):
    print(cs.__next__())

re = itertools.repeat('ziio',3)
for n in re:
    print(n)
    
for c in itertools.chain('hello' , 'ziio'):
    print(c)

for key , group in itertools.groupby('aaabbzziio'):
    print(key , list(group))

def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    odds = itertools.count(2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    oddss = itertools.islice(odds,N)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    terms = (4/(i if j%2 == 0 else -i) for j , i in enumerate(odds))
    # step 4: 求和:
    return sum(terms)

# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')