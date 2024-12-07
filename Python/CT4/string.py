print('包含中文的str')
ord('A')
ord('中')
chr(66)
chr(25991)

'\u4e2d\u6587'
b'abc'
'abc'.encode('utf-8')
'中文'.encode('utf-8')
b'abc'.decode('utf-8')
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8' , errors='ignore')

len('abc')

'hello %s' % 'world'
'Age: %s. Gender: %s' % (25, True)
'hello {0}'.format('world')
s = "world"
f'hello {s}'

s1 = 72
s2 = 85
r = (s2-s1)/s1 * 100
print(f'{r:.1f}%')