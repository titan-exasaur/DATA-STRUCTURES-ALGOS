class calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):        
        return self.a/self.b
    
test_calc = calc(10,2)
print(test_calc.add())
print(test_calc.sub())
print(test_calc.mul())
print(test_calc.div())