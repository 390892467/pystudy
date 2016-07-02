class Test(object):
    number = 1
    def count(self,num1):
        self.num1 = num1
        return self.number * self.num1

test = Test()
print(test.number + 1)
print(Test.number)
print(test.number + 1)
print(test.count(2))
