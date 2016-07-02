#列表全排列
lst = [1,2,3]
print([(x,y,z) for x in lst for y in lst for z in lst if x != y if y != z if x != z])


def add(num):
    if len(str(num)) == 1:
        return num
    ret = 0
    for i in str(num):
        ret += int(i)
        return ret
    return(add(ret))
print(add(8))

def add(num):
    ret = 0
    for i in str(num):
        ret += (int(i) ** 2)
def happy_number(num):
    results = {num}
    ret = num
    while ret >= 10:
        ret = add(ret)
        if ret in results:
            return false
        results.add(ret)
    return ret == 1
for i in range(1,10000):
    if happy_number(i):
        print('{0} i happy number'.format(i))
    else:
        print('{0} is not happy number'.format(i))
