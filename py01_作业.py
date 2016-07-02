#常量一般用大写命名，变量用小写字母表示，多个小写字母用下划线表示
#range函数的实现
def myrange(start,stop,step):
    ret = list()
    cur = start
    ret.append(cur)
    while cur < stop:
        cur += step
    return ret

#猜数字游戏
NUM = 35
for _ in range(3):            # “_”表示忽略输出
    cur = int(input("Enter your number:"))
    if cur == NUM:
        print("You win!")
        break
    elif cur < NUM:
        print("Less!")
    else:
        print("Bigger!")
else:
    print("You failed!")

#求结果
L = [1,3,2,4,3,2,5,7,7,2]
#[1,3,2,4,5,7]
 ret = list()
 for item in L:
    if item not in ret: #这种效率最低
        ret.append(itme)
print(ret)


 ret = list()
 tmp = set()
 for item in L:
    if item not in tmp: #这种效率高
        ret.append(item)
        tmp.add(item)
print(ret)

#求素数个数
import math
L = [2,3,5,7,10,12,6,8]
count = 0
for item in L:
    for i in range(2,math.ceil(math.sqrt(item))):
        if item % i == 0:
            break
    else:
        count += 1
print(count)






