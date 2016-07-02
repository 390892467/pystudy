'''
str = 'magedu.com'
l1 = str.split('.')
print(type(l1))
l1.append('.cn')
print(l1)
print(' '.join(l1))


l2 = [str(i) for i in range(10)]
print(type(l2))
print(':'.join(l2))
'''
# 8 * 7 * 6 ....1
def fact(x):
    if x <= 1:
        return 1
    else:
       return x * fact(x-1)
if __name__ == '__main__':
    print(fact(3))