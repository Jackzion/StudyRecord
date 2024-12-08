class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
        
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
        
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
        
bart = Student('Bart Simpson', 59)
bart.print_score()
print(bart.get_name())

class Student02(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
        
    def get_gender(self):
        return self.__gender  
      
    def set_gender(self,gender):
        self.__gender = gender
    
# 测试:
bart = Student02('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
        
class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    def run(self):
        print('Dog is running...')
class Cat(Animal):
    pass

dog = Dog()
dog.run()

import types

def fn():
    pass

print(type(fn))
print(type(abs))
print(type(lambda x : x))
print(type((x for x in range(10))))

print(isinstance(dog,Animal))
print(isinstance([1,2],(tuple,list)))

class MyObject(object):
     def __init__(self):
         self.x = 9
     def power(self):
         return self.x * self.x
ob = MyObject()

hasattr(ob,'x')
setattr(ob,'y',100)
getattr(ob,'y',404)
print(getattr(ob,'y'))


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count+=1

# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')