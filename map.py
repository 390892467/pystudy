def left_fold(fn,*args):
#    print(args)
#    type(args)
    it = iter(args)
#    print(type(it))
    ret = next(it)
    for x in it:
        ret = fn(ret,x)
    return(ret)
def add(x,y):
    return x + y
print(left_fold(add,1,2,3,4,5))


def inc(x):
    return x + 1
print(filter(inc,[1,2,3,4]))
print(list(filter(inc,[1,2,3,4])))


