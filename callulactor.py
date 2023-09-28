class Calculator:
    def __init__(self, a, b):  
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def mudulo(self):
        return self.a % self.b

    def divide(self):
        if self.b == 0:
            return "cannot not divide by zero"
        else:
            return self.a / self.b


    def __str__(self):
        return f"{self.a} { self.b}"

   
        num1, num2 = map(int, (input("enter values for num1, num2 separated by comma: ").split(", ")))



pp = Calculator(5, 10)
print(pp.sum())
print(pp.subtract())
print(pp.multiply())
print(pp.mudulo())
print(pp.divide())





