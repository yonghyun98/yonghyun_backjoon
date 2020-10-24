from random import *

rand_num = randint(1,51)
my_num = -1

for i in range(0,5):
    my_num = int(input('1과 50사이의 숫자를 입력해주세요 >>'))
    if my_num == rand_num:
        print ('정답!')
        break
    elif my_num > rand_num:
        print ('Down!')
    else:
        print ('up!')

