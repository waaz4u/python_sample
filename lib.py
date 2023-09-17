#!/usr/bin/python3

import os

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

