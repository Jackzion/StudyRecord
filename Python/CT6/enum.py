from enum import Enum,unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
    
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
print(Weekday.Sun)
print(Weekday.Sun.value)
for name, member in Weekday.__members__.items():
    print(name, '=>', member, ',', member.value)
    
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
    
def fn(self,name="world"):
    print("hello world")
Hello = type('Hello',(object,),dict(hello=fn))
h = Hello()
h.hello()

class ListMetaClass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
    
class MyList(list, metaclass=ListMetaClass):
    pass
L = MyList()
L.add(1)
print(L)
