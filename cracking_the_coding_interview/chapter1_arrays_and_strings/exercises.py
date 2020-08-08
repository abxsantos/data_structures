import pytest


def is_unique(string_to_check):
    """
    Determine if string_to_check has all unique characters.
    """
    if len(string_to_check) > 128:
        return False
    characters = [False] * 128
    for index in range(0, len(string_to_check)):
        value = ord(string_to_check[index])
        if characters[value]:
            return False
        characters[value] = True
    return True


def check_permutation_helper(string):
    return [ord(letter) for letter in string]


def check_permutation(string1, string2):
    """
    Given two strings return True if one is a permutation of another.
    """
    if len(string1) != len(string2):
        return False
    characters1 = check_permutation_helper(string1)
    characters2 = check_permutation_helper(string2)

    if sorted(characters1) == sorted(characters2):
        return True
    return False


def urlify(string):
    """
    Given a string replace all spaces with '%20' without altering the initial size
    """
    blank_characters = [ord(character) for character in string if ord(character) == 32]
    if len(blank_characters) % 3 == 0:
        return True
    return False


def check_palindrome_permutation(string):
    """
    Given a string check if it's a permutation of a palindrome.
    """
    pass


def check_one_away(string1, string2):
    """
    There can be tree edits: insert a character, remove a character and replace a character.
    Given two strings check if they are one edit away.
    """
    pass


def string_comprehension(word):
    """
    Given a string with repeated letters, return another string
    without the repeated letters with it's count by the side
    """
    final_string = ""
    consecutive_letters = 0
    for letter_index in range(len(word)):
        consecutive_letters += 1
        if letter_index + 1 >= len(word) or word[letter_index] != word[letter_index + 1]:
            final_string += word[letter_index] + str(consecutive_letters)
            consecutive_letters = 0
    return final_string


def rotate_matrix(matrix):
    """
    Given an NxN matrix, rotate ir by 90 degrees.
    """
    rotated_matrix = [row[:] for row in matrix]
    matrix_size = len(matrix[0])

    for row in range(matrix_size):
        for column in range(matrix_size):
            rotated_matrix[column][matrix_size - 1 - row] = matrix[row][column]
    return rotated_matrix


def zero_matrix(matrix):
    """
    Given a NxN matrix, if an element is zero replace the entire row and column with zero
    """
    number_of_rows, number_of_columns = len(matrix), len(matrix[0])
    zero_row, zero_column = None, None
    for row in range(number_of_rows):
        for column in range(number_of_columns):
            if matrix[row][column] == 0:
                zero_row = row
                zero_column = column
    if zero_row is None or zero_column is None:
        return None
    for row in range(number_of_rows):
        matrix[row][zero_column] = 0
        if row == zero_row:
            matrix[row] = [0]*number_of_columns
    return matrix


def is_substring(string1, string2):
    """
    Check if string2 is a substring of string1
    """
    pass


class TestExercises(object):

    @pytest.mark.parametrize("string_to_check, expected_result", [
        ("ABC", True), ("AAA", False)
    ])
    def test_is_unique(self, string_to_check, expected_result):
        assert is_unique(string_to_check) is expected_result

    @pytest.mark.parametrize("string1, string2, expected_result", [
        ("ABC", "BCA", True), ("AAA", "DDD", False)
    ])
    def test_check_permutation(self, string1, string2, expected_result):
        assert check_permutation(string1, string2) is expected_result

    @pytest.mark.parametrize("string, expected_result", [
        ("abc ", False), ("abc   ", True), ("Mr John Smith    ", True)
    ])
    def test_check_urlify(self, string, expected_result):
        assert urlify(string) is expected_result

    def test_check_palindrome_permutation(self):
        assert check_palindrome_permutation("Tact Coa") is True

    @pytest.mark.parametrize("string1, string2, expected_result", [
        ("pale", "ple", True), ("pales", "pale", True), ("pale", "bale", True), ("pale", "bake", False)
    ])
    def test_check_one_away(self, string1, string2, expected_result):
        assert check_one_away(string1, string2) is expected_result

    def test_string_comprehension(self):
        assert string_comprehension("aabcccccaaa") == "a2b1c5a3"

    def test_rotate_matrix(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected_matrix = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
        assert rotate_matrix(matrix) == expected_matrix

    def test_zero_matrix_when_there_is_a_zero_value(self):
        matrix = [
            [1, 0, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected_matrix = [
            [0, 0, 0],
            [4, 0, 6],
            [7, 0, 9]
        ]
        assert zero_matrix(matrix) == expected_matrix

    def test_zero_matrix_when_there_is_more_than_one_zero_value(self):
        matrix = [
            [1, 0, 3],
            [0, 5, 6],
            [7, 8, 9]
        ]
        expected_matrix = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 9]
        ]
        assert zero_matrix(matrix) == expected_matrix

    def test_zero_matrix_when_there_is_no_zero_value(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        assert zero_matrix(matrix) is None
