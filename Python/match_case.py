score = 'B'

match score:
    case 'A':
        print('score is A.')
    case 'B':
        print('score is B.')
    case 'C':
        print('score is C.')
    case _: # _表示匹配到其他任何情况
        print('score is ???.')

age = 15

match age:
    case x if x < 10:
        print(f'<10')
    case 10:
        print('10')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('11-18')
    case _:
        print('not sure.')
        
args = ['gcc','hello.c']

match args:
    case ['gcc']:
        print('error no args')
    case ['clean']:
        print('clean')
    case ['gcc',file1]:
        print('gcc comlplie ' + file1)
    case _:
        print('invalid command')