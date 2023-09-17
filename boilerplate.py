#!/usr/bin/python3
import unittest

def sample_function():
    pass

class mytests(unittest.TestCase):
    # def setUpClass(cls) -> None:
    def setUp(self):
        test_title = unittest.TestCase.id(self).split('.')[2:]
        print('\n', test_title)
    # def tearDown(self) -> None:
    # def tearDownClass(cls) -> None:

    @staticmethod
    def test_01():
        """
            Sample Test
            Args:
                None
            Returns:
                int: value of sample_function
                Raises:
                    TypeError: If input is not an int
            """
        pass


if __name__ == '__main__':
    unittest.main()
