class Calc:
    def sum(self, a: float, b: float):
        return a + b
    
    def diff(self, a: float, b: float):
        return a - b
    
    def multiply(self, a: float, b: float):
        return a * b
    
    def division(self, a: float, b: float):
        if (b == 0): raise ZeroDivisionError()

        return a / b
