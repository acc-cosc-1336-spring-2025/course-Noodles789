import unittest

from tests.homework.j_classes import tests_classes

def main():

    suite = unittest.TestLoader().loadTestsFromModule(tests_classes)
    
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    main()