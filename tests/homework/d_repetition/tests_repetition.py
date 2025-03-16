def get_factorial(num):
    factorial = 1 
    for i in range (1, num + 1):
        #factorial *= i
        factorial = factorial * i
    return factorial

import unittest

class TestFactorial(unittest.TestCase):
    def test_get_factorial(self):
        self.assertEqual(get_factorial(4),24)
        self.assertEqual(get_factorial(5),120)
        self.assertEqual(get_factorial(6),720)

def sum_odd_numbers(num):
    total = 0 
    i = 1
    while i <= num:
        total += i
        i += 2
    return total

class TestSumOddNumbers(unittest.TestCase):
    def test_sum_odd_numbers(self):
        self.assertEqual(sum_odd_numbers(7),16)
        self.assertEqual(sum_odd_numbers(9),25)
        self.assertEqual(sum_odd_numbers(10),25)