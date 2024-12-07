age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')
    
s = input('birth:')
birth = int(s)
if(birth>=2000):
    print('00后')
else:
    print('00前')
    
height = 1.75
weight = 80.5

bmi = (weight/height)**2
print(bmi)
if bmi < 18.5:
	print('过轻')
elif 18.5 <= bmi <= 25:
	print('正常')
elif 25 < bmi <= 28:
	print('过重')
elif 28 < bmi <= 32:
	print('肥胖')
else:
	print('严重肥胖')