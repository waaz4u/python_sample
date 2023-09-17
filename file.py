#!/usr/bin/python3
import os
import argparse
import sys
import unittest


# ------------------------------------------------------------------------------------------------------#
def check_file_exist(file):
    """ Checks if provided path is file && it exists
        :param file : filename
        :type : str
    """
    assert (os.path.isfile(file))


def is_empty(file):
    """ Checks if file is empty
        :param file : filename
        :type : str
    """
    if os.path.getsize(file) == 0:
        raise "File is empty!"


def is_text_file(file):
    """Checks if file is a text file
        :param file : filename
        :type : str
    """
    # assert (os.path.splitext(file)[1] == ".txt")
    assert (file.endswith('.txt'))


def word_count(file):
    """ counts words in file.
        :param file: filename
        :type: str
        :returns: number of words in file.
        "rtype: int
    """
    with open(file, 'rt') as keyfile:
        data = keyfile.read()
        words = data.split()
        print('\n Number of words in text file :', len(words))
        return words


def check_repetition(words):
    """ returns a dictionary with words as keys and number of times they appear as values.
        :param words: strings
        :type: str
        :returns: dictionary of words as keys and their appearance in file as values.
        :rtype: dict
    """
    k = {}
    for j in words:
        if j in k:
            k[j] += 1
        else:
            k[j] = 1
    return k


def ordered_dictionary(unordered_dict):
    """ Returns a dictionary with descending order of words as per their appearance in file.
        :params unordered_dict: dictionary of words.
        :type: dict
        :returns: dictionary
        :rtype: dict
    """
    return dict(sorted(unordered_dict.items(), key=lambda x: x[1], reverse=True))


def top_n_elements(my_dict, top_words):
    """ prints a list of first N words from the dictionary.
        :param my_dict: dictionary
        :type: dict
        :param top_words: Number of words to be printed.
        :type: int
    """
    if top_words > len(list(my_dict.keys())):
        top_words = len(list(my_dict.keys()))
    print('\nTop {} words ordered by the number of times they appear in the file: {}'.format(
        top_words, list(my_dict.keys())[:top_words]))


def print_line():
    """ Prints '-' 50 times to make a line """
    for i in range(50):
        print('-', end="")


# ------------------------------------------------------------------------------------------------------#
class mytests(unittest.TestCase):
    """
    Write a program, preferably in Python, that given a text-file,
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
