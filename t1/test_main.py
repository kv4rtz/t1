import unittest
import main

class TestCalc(unittest.TestCase):
    calc: main.Calc

    def setUp(self):
        self.calc = main.Calc()

    def test_sum(self):
        self.assertEqual(self.calc.sum(3, 3), 6)

    def test_diff(self):
        self.assertEqual(self.calc.diff(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 3), 9)
        
    def test_division(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.division(3, 0)
        
        self.assertEqual(self.calc.division(3, 3), 1)

if __name__ == '__main__':
    unittest.main()