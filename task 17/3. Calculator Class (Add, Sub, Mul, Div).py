class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Division by zero not allowed"


c = Calculator()

print("Add:", c.add(10, 5))
print("Sub:", c.sub(10, 5))
print("Mul:", c.mul(10, 5))
print("Div:", c.div(10, 5))
