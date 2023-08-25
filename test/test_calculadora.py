import unittest
from calculadora import *

class test_calculadora(unittest.TestCase):
    c = CalculadoraConsole()
    range_x_y = range(-10,10)
    
    def prepare_test(self, x, y, op):
        return str(x) + " " + op + " " + str(y)
    

    def test_division_by_0(self):
        #str_test = self.prepare_test(3, 0, 'dividido por')
        #returned = c.main_test(str_test)
        expected = 0
        self.assertRaises(ZeroDivisionError, self.c.main_test, self.prepare_test(3, 0, 'dividido por'))

    def test_power_0_to_negative(self):

        with self.assertRaises(ZeroDivisionError):
            self.c.main_test(self.prepare_test(0, -2, 'elevado a'))

    def test_add_multiple_values(self):
        for x in self.range_x_y:
            for y in self.range_x_y:
                result = self.c.main_test(self.prepare_test(x, y, 'mais '))
                expected = x + y
                self.assertEqual(expected, float(result.split()[-1]))

    def test_subtract_multiple_values(self):
        for x in self.range_x_y:
            for y in self.range_x_y:
                result = self.c.main_test(self.prepare_test(x, y, 'menos'))
                expected = x - y
                self.assertEqual(expected, float(result.split()[-1]))

    def test_multiply_multiple_values(self):
        for x in self.range_x_y:
            for y in self.range_x_y:
                result = self.c.main_test(self.prepare_test(x, y, 'vezes'))
                expected = x * y
                self.assertEqual(expected, float(result.split()[-1]))
    
    def test_division_multiple_values(self):
        for x in self.range_x_y:
            for y in self.range_x_y:
                if y == 0:
                    self.assertRaises(ZeroDivisionError, self.c.main_test, self.prepare_test(x, y, 'dividido por'))
                else: 
                    result = self.c.main_test(self.prepare_test(x, y, 'dividido por'))
                    expected = x / y
                    self.assertTrue(expected == float(result.split()[-1]))
    
    def test_power_multiple_values(self):
        for x in self.range_x_y:
            for y in self.range_x_y:
                if x == 0 and y < 0:
                    self.assertRaises(ZeroDivisionError, self.c.main_test, self.prepare_test(x, y, 'elevado a'))
                else: 
                    result = self.c.main_test(self.prepare_test(x, y, 'elevado a'))
                    expected = x ** y
                    self.assertTrue(expected == float(result.split()[-1]))       
 
    
    if __name__ == '__main__':
        unittest.main()
