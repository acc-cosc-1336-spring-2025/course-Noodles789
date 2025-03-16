import unittest
from tests.homework.d_repetition import tests_repetition

class testrepetition(unittest.TestCase):
    def test_get_factorial(self):
        self.assertEqual(get_factorial(5),120)
        self.assertEqual(get_factorial(4),24)
        self.assertEqual(get_factorial(6),720)

suite = unittest.TestLoader().loadTestsFromModule(tests_repetition)
unittest.TextTestRunner(verbosity=2).run(suite)
