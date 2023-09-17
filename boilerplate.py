#!/usr/bin/python3
import unittest

def sample_function(sample_param):
    if isinstance(sample_param, int):
        return sample_param
    else:
        TypeError("Not an integer")

class mytests(unittest.TestCase):
    # def setUpClass(cls) -> None:
    def setUp(self):
        test_title = unittest.TestCase.id(self).split('.')[2:]
        print('\n', test_title)
    # def tearDown(self) -> None:
    # def tearDownClass(cls) -> None:

    def test_01(self):
        """
            Sample Test
            Args:
                None
            Returns:
                int: value of sample_function
                Raises:
                    TypeError: If input is not an int
            """
        return sample_function(1)

    def test_02(self):
        pass


if __name__ == '__main__':
    unittest.main()
