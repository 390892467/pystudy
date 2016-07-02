def iteror(x):
    i = 1
    while i < x:
        yield i ** 2
        i += 1
g1 = iteror(5)
print(type(g1))
for i in g1:
    print(i)
