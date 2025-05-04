import unittest
from src.homework.j_classes.class_a import die

class TestDie(unittest.TestCase):
    def test_roll_values(self):
        d = die()
        for _ in range(3):
            value = d.roll()
            self.assertTrue(1 <= value <= 6)
            self.assertEqual(value, d.get_rolled_value())