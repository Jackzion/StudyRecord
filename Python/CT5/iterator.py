from collections.abc import Iterator

print(isinstance((x for x in range(10)),Iterator))
print(isinstance({},Iterator))

o = iter([1,2,5,6])
print(next(o))
print(next(o))
print(next(o))
print(next(o))

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break