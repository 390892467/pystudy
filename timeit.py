#测试time.sleep(5)执行的时间，装饰器
import time
def timeit(fn):
    def wrap(*args,**kwargs):
        start = time.time()
        ret = fn(*args,**kwargs)
        print(time.time() - start)
#       return ret
    return wrap
'''
def sleep(x):
    time.sleep(x)
timeit(sleep)(3)
'''
@timeit
def sleep(x):
    time.sleep(x)
sleep(5)
