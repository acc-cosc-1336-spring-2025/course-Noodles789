
import unittest

def get_lowest_list_value(first):
    if not first:
        raise ValueError("there is no list, try again")
    lowest = first[0]
    for num in first[1:]:
        if num < lowest:
            lowest = num
            return lowest
        
def get_highest_list_value(first):
    if not first:
        raise ValueError("there is no list, try again")
    highest = first[0]
    for num in first[1:]:
        if num > highest:
            highest = num
        return highest
class TestListFunctions(unittest.TestCase):
    def test_get_lowest_list_value(self):
        self.assertEqual(get_lowest_list_value([8, 10, 1, 50, 20]), 1)

    def test_get_highest_list_value(self):
        self.assertEqual(get_highest_list_value([8, 10, 1, 50, 20]), 50)

unittest.main(exit=False)