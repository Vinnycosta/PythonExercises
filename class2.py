class Calculator():
    def __init__(self, num1, num2):
        self.value1 = num1
        self.value2 = num2
    def soma(self):
        return self.value1 + self.value2
    def subt(self):
        return self.value1 - self.value2
    def mult(self):
        return self.value1 * self.value2
    def divs(self):
        return self.value1 / self.value2

calculadora = Calculator(10,2)
