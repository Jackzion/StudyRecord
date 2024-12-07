import math
n1 = 255
n2 = 1000
print(hex(n2))

def my_abs(x):
    if(not isinstance(x,(int,float))):
        raise TypeError('bad opeand type')
    if( x>=0):
        return x
    else :
        return -x

print(my_abs(99))

def nop():
    pass

def move(x,y,step,angle=0):
    nx = x + step - math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx , ny
print(move(100,100,60,math.pi/6))


import math

def quadratic(a, b, c):
    x1 = (-b + math.sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b - math.sqrt(b**2-4*a*c))/(2*a)
    return x1 , x2

# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
    
def power(x ,n=2):
    s = 1
    while(n>0):
        s*=x
        n-=1
    return s
print(power(power(2)))

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum
print(calc(1,561,5))
nums = [1,2,3]
print(calc(*nums))

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
extra = {'city':'foshan','aa': 111}
person('ziio',10,**extra)

def person1(name, age, *, city='Beijing', job):
    print(name, age, city, job)
person1('Jack', 24, job='Engineer')

def fact(n):
    if n==1:
        return 1
    else: return fact(n-1) + n
print(fact(3))

def fact1(n):
    return fact_iter(n,1)

def fact_iter(n,product):
    if n==1:
        return product
    return fact_iter(n-1,product+n)
print(fact1(3))

# a -> b by c
def move(n, a, b, c):
    if n == 1:
        print(a, ' --> ' , b)
    else:
        # a -> b by c
        move(n-1,a,b,c)
        # a -> c
        print(a,' --> ',c)
        # b -> c by a
        move(n-1,b,c,a)

# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
move(3, 'A', 'C', 'B')