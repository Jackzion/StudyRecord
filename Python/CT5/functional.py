from functools import reduce

list(map(str,[1,2,3,4,5]))
print(list)

def add(x,y):
    return x+y
print(reduce(add,[1,2,3]))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x,y:x*10+y , map(char2num,s))

print(str2int(['1','2']))

def normalize(name):
    return name[:1].upper() + name[1:].lower()
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(L):
    return reduce(lambda x,y:x*y,L)
        
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

from functools import reduce

def str2float(s):
    def char2num(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.':'.'}
        return digits[s]
    m = s[:s.index('.')]+s[s.index('.')+1:]
    l = list(map(char2num,m))
    def f(x,y):
        return x*10 + y
    return reduce(f,l)/10**(len(s)-s.index('.')-1)
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
    
def is_odd(x):
    return x%2==1
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty,[' ' , 'hello' , None])))

def _odd_iter():
    n = 1
    while(True):
        n = n+2
        yield n
def _not_divisible(n):
    return lambda x: x%n>0
def primes():
    yield 2 
    it = _odd_iter()
    while True :
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)
# 打印1000以内的素数:
for n in primes():
    if n < 100:
        print(n)
    else:
        break      

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

a = sorted([36, 5, -12, 9, -21], key=abs)
print(a)
a = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower , reverse=True)
print(a)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]
L2 = sorted(L, key=by_name)
print(L2)

def by_score(t):
    return t[1]
L2 = sorted(L, key=by_score)
print(L2)

def lazy_sum(*args):
    def sum():
        ax = 0
        for i in args:
            ax+=i
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
print(f())

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs
f1, f2, f3 = count()
print(f1(),f2())

def inc():
    x = 0
    def fn():
        nonlocal x
        x = x + 1
        return x
    return fn
f = inc()
print(f()) # 1
print(f()) # 2

def createCounter():
    count = 0
    def counter():
        nonlocal count
        count = count + 1
        return count
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
    
f = lambda x: x * x
print(f(5))
L = list(filter(lambda n : n % 2 == 1, range(1, 20)))
print(L)
    
