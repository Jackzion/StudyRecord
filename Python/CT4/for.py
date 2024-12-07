names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print('name:',name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    if x>5:
        break
    sum = sum + x
print(sum)

sum = 0
for x in range(101):
    sum+=x
print(sum)

sum = 0
n = 99
while(n>0):
    sum+=n
    n = n-2
print(sum)