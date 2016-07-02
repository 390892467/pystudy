'''
for i in range(1,10):
    if i % 2 == 1:
        print("0%d" %(i))

lst = ['I', 'love', 'Python']
ret = ''
for s in lst:
    ret += s
    ret += ' '
print(ret)

print(' '.join(lst))

s = 'URL:http://www.magedu.com'
URL1,_ = s.split(':',1)
print(URL1)
'''

f = open(r'C:\Users\zheng LM\Desktop\pystudy\passwd','r')     #加'r'转义，\U开始的字符被编译器认为是八进制
for line in f.readlines():
    line = line.strip()         #trip方法是不输出换行符
#   print(line)
    if line.startswith('root:'):
        _, shell = line.rsplit(':', 1)
        print(shell)
#help(line.startswith)

