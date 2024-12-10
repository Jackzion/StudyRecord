d = dict(name='Bob', age=20, score=88)

import pickle
pickle.dumps(d)
print(pickle.dumps(d))

import json
print(json.dumps(d))

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
s = Student('Bob', 20, 88)
print(json.dumps(s , default=lambda s : s.__dict__))

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)