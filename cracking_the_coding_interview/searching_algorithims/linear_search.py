"""
Given an array search for an specific item.
"""


def linear_search(array, value_to_search):
    """
    Search for a specific value inside an UNSORTED array.
    """
    for index in range(len(array)):  # O(n) // O(1)
        if array[index] == value_to_search:
            return index
    return -1


def binary_search(array, value_to_search):
    """
    Search for a specific value in a SORTED array.
    """
    start, end = 0, len(array) - 1
    index = -1
    while start <= end and index == -1:  # O(log2 n) // O(1)
        middle = (start + end)//2
        if array[middle] == value_to_search:
            index = middle
        else:
            if array[middle] > value_to_search:
                end = middle - 1
            else:
                start = middle + 1
    return index


def naive_search(string1, string2):
    """
    Find is one of given strings is a substring of another.
    """
    longer_string, shorter_string = string1, string2
    if len(string1) < len(string2):
        longer_string, shorter_string = string2, string1
    longer_string_size, shorter_string_size = len(longer_string), len(shorter_string)
    for index in range(longer_string_size):
        for second_index in range(shorter_string_size):
            if longer_string[index + second_index] != shorter_string[second_index]:
                break
            elif second_index == shorter_string_size - 1:
                return True
    return False


class TestSearchAlgorithms(object):

    def test_linear_search_must_return_index_of_value_if_found_on_given_array(self):
        assert linear_search([1, 5, 3, 2, 10], 3) == 2

    def test_linear_search_must_return_minus_one_if_value_not_found_on_given_array(self):
        assert linear_search([1, 5, 3, 2, 10], 100000) == -1

    def test_binary_search_must_return_index_of_value(self):
        assert binary_search([1, 2, 3, 5, 10], 3) == 2

    def test_binary_search_must_return_minus_one_when_no_values_found(self):
        assert binary_search([1, 2, 3, 5, 10], 1000000) == -1

    def test_naive_search_must_return_true_if_found_substring(self):
        assert naive_search("abcde", "abc") is True

    def test_naive_search_must_return_false_if_not_found_substring(self):
        assert naive_search("abcde", "fgh") is False
