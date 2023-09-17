#!/usr/bin/python3

from lib import *
import argparse
import sys
import unittest

class mytests(unittest.TestCase):
    """
    A Program, that given a text-file,
    counts the number of words and reports the top N words ordered by the number of times they appear in the file.
    Also consider that this code could be used by a suite of tests, not just usable as a standalone program.
    """

    if sys.argv[1] == '-h':
        pass
    elif len(sys.argv) < 3:
        print_line()
        raise Exception(''
                        '\n*** Invalid arguments provided ***'
                        '\nTest File Usage: ./mytest.py file_name Top_N_words'
                        '\n\n Eg: ./file.py somedata.txt 10\n\n')
    else:
        file_name = sys.argv[1]
        elements = sys.argv[2]

    # param initialisation.
    unordered_dict = {}
    sorted_dictionary = {}
    words = None

    def setUp(self):
        print('\n', unittest.TestCase.id(self).split('.')[2:])
        print('\n-->', unittest.TestCase.shortDescription(self))

    def tearDown(self):
        print_line()

    @staticmethod
    def test_01_check_file_exists():
        """ Test to check if file exists and the type is a file"""
        check_file_exist(mytests.file_name)

    @staticmethod
    def test_02_check_empty_file():
        """ Test to check if file is not empty"""
        is_empty(mytests.file_name)

    @staticmethod
    def test_03_check_if_text_file():
        """ Test to verify it is a text file """
        is_text_file(mytests.file_name)

    @staticmethod
    def test_04_check_file_size():
        """ Test to number of words in a text file """
        mytests.words = word_count(mytests.file_name)

    @staticmethod
    def test_05_check_word_repetition():
        """ Check how many words are repeated and report number of times
        they are repeated as a dictionary"""
        mytests.unordered_dict = check_repetition(mytests.words)
        print("\n unordered dict with count -- > ", mytests.unordered_dict)

    @staticmethod
    def test_06_arrange_words():
        """ Takes input as dictionary and sequence the keys as per their values"""
        mytests.sorted_dictionary = ordered_dictionary(mytests.unordered_dict)
        print("\n ordered dict with count -- > ", mytests.sorted_dictionary)

    @staticmethod
    def test_07_top_three_elements():
        """ Returns top N Words"""
        top_n_elements(mytests.sorted_dictionary, int(mytests.elements))


# ------------------------------------------------------------------------------------------------------#
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mytests.file_name', default='somedata.txt', type=str, help='filename of text file')
    parser.add_argument('mytests.elements', default=1, type=int, help='Top N words in the file')
    parser.add_argument('unittest_args', nargs='*')

    args = parser.parse_args()
    sys.argv[1:] = args.unittest_args
    unittest.main()
# ------------------------------------------------------------------------------------------------------#
