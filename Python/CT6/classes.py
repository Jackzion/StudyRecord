class Student(object):
    __slots__ = ('name', 'age')
    pass
s = Student()
s.age = 25
print(s.age)

class Student1(object):
    @property
    def score(self):
         return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
a = Student1()
a.score = 100

class Screen(object):
    @property
    def width(self):
        return self._width    
    @property
    def resolution(self):
        return 786432
    @width.setter
    def width(self , value):
        self._width = value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self , value):
        self._height = value
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')
class Animal(object):
    pass
# 大类:
class Mammal(Animal):
    pass
class Dog(Mammal, Runnable):
    pass

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

    def __getitem__(self,n):
        if isinstance(n,int):
            a,b=1,1
            for x in range(n):
                a,b = b,a+b
            return a
        if isinstance(n,slice):
            start = n.start
            stop = n.stop
            if(start is None):
                start = 0
            a,b = 1,1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b = b , a+b
            return L
print(Fib()[5])
print(Fib()[:10])

class Student02(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
        else :
            raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
    def __call__(self):
            print('My name is %s.' % self.name)
s = Student02()
print(s.score)
s()

class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__
    

print(Chain().status.user)

