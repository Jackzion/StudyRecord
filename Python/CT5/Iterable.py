from collections.abc import Iterable

print(isinstance('abc', Iterable))
print(isinstance([1,2,3], Iterable))

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
    
def findMinAndMax(L):
    if(not isinstance(L,Iterable)):
        raise TypeError
    if(L == []):
        return (None,None)
    min = L[0]
    max = L[0]
    for m in L:
        if min > m:
            min = m
        if max < m:
            max = m
    return (min, max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
    
print([x*x for x in range(1,11) if x%2==0])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1  if isinstance(s,str) ]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')