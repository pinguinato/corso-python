class calculator:
    def add(self, a, b):
        return a + b
    def sub(self, a, b):
        return a -b
    def prod(self, a, b):
        return a * b
    def div(self, a, b):
        return a / b

clac = calculator()

print(clac.add(5,6))
print(clac.sub(10,5))
print(clac.prod(5,5))
print(clac.div(100,10))