import functools , time
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kv):
        print('call %s():' % func.__name__)
        return func(*args,**kv)
    return wrapper

def log1(*text):
    def log(func):
        @functools.wraps(func)
        def wrapper(*args,**kv):
            if text:#添加一个判断是否为空即可
                print("%s"%text)
            print('%s call %s():' % (text , func.__name__))
            return func(*args,**kv)
        return wrapper
    return log

@log1("ziio")
def now():
    print('2024-6-1')
f = now
print(f.__name__)

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kv):
        print("begin call")
        start = time.perf_counter()
        fnc = fn(*args,**kv)
        end = time.perf_counter()
        print(f'{fn.__name__} executed in {end - start} ms')
        print("end call")
        return fnc
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
    
int2 = functools.partial(int,base=2)
print(int2('1010'))
max2 = functools.partial(max,10)
a = max2(5,6,7)
print(a)