from collections import OrderedDict

class LastUpdatedOrderdDict(OrderedDict):
    def __init__(self,capacity):
        super(LastUpdatedOrderdDict,self).__init__()
        self._capacity = capacity
        
    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=True)
            print('remove' , last)
        if containsKey:
            del self[key]
            print('set:',(key,value))
        else:
            print('add' , (key,value))
        OrderedDict.__setitem__(self,key,value)

d = LastUpdatedOrderdDict(2)
d.__setitem__('a','1')
d.__setitem__('b','2')
d.__setitem__('c','2')

from collections import ChainMap
import os , argparse

# 默认参数
defaults = {
    'color':'red',
    'user':'guest'
}
# 构造命令行参数
parser = argparse.ArgumentParser()
parser.add_argument('-u','--user')
parser.add_argument('-c','--color')
namespace = parser.parse_args()
command_line_args = {k : v for k,v in vars(namespace).items() if v }
# 组合成 chainMap
combined = ChainMap(command_line_args,os.environ,defaults)
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])

from collections import Counter
c = Counter('programming')
print(c)
c.update('hello')