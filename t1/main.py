class Calc:
    def sum(self, a: float | int, b: float | int):
        return a + b
    
    def diff(self, a: float | int, b: float | int):
        return a - b
    
    def multiply(self, a: float | int, b: float | int):
        return a * b
    
    def division(self, a: float | int, b: float | int):
        if (b == 0): raise ZeroDivisionError()

        return a / b