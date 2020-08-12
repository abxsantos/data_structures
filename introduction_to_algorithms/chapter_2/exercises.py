import pytest


def insertion_sort_increasing(array):
    """
    Given an unordered array sort it in an increasing order.
    """
    # the current number starts at index 1
    # the previous number is equal to index of current - 1
    # if the current number < previous number, shift the indexes
    # else current umber[index + 1]
    i = 1
    while i < len(array):
        current_number = array[i]
        j = i - 1
        while array[j] > current_number and j >= 0:
            array[j + 1] = array[j]
            array[j] = current_number
            j -= 1
        i += 1

    return array


def insertion_sort_decreasing(array):
    """
    Sort the same array in a decreasing order.
    """
    current_index = 1
    while current_index < len(array):
        current_number = array[current_index]
        previous_index = current_index - 1
        while array[previous_index] < current_number and previous_index >= 0:
            array[previous_index + 1] = array[previous_index]
            array[previous_index] = current_number
            previous_index -= 1
        current_index += 1
    return array


def linear_search(value, array):
    """
    return the index of given value v if it exists in array a, NIL otherwise
    """
    index = 0
    for number in array:  # use enumerate in real world!
        if number == value:
            return index
        index += 1
    return "NIL"


def selection_sort(array):  # O(1) // O(n) // O(n**2)
    """
    Search for the smallest value in array and change it with array[1].
    Then find the second smallest value and change it with array[2].
    """
    current_index = 1
    while current_index < len(array):  # current_index, ... array[current_index, +1, +2,...]
        current_value = array[current_index]
        prev_index = current_index - 1
        while array[prev_index] > current_value and prev_index >= 0:
            array[prev_index + 1] = array[prev_index]
            array[prev_index] = current_value
            prev_index -= 1
        current_index += 1
    return array[-1:] + array[0:-1]


class TestChapter2Exercises(object):

    def test_insertion_sort_increasing(self):
        assert insertion_sort_increasing([31, 41, 59, 26, 41, 58]) == [26, 31, 41, 41, 58, 59]

    def test_insertion_sort_decreasing(self):
        assert insertion_sort_decreasing([31, 41, 59, 26, 41, 58]) == [59, 58, 41, 41, 31, 26]

    @pytest.mark.parametrize("param_value, param_array, expected_result", [
        (10, [1, 8, 3, 7, 10], 4), (10, [1, 8, 3, 7], "NIL")
    ])
    def test_linear_search(self, param_value, param_array, expected_result):
        assert linear_search(param_value, param_array) == expected_result

    def test_selection_sort(self):
        assert selection_sort([10, 2, 12, 3, 6]) == [12, 2, 3, 6, 10]
