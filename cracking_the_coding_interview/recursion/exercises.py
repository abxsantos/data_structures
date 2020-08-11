import pytest


def sum_numbers(n):
    """
    Given a positive integer, compute the cumulative sum of 0 to that integer.
    """
    # Base case
    if n == 0:
        return 0
    # Recursion
    else:
        return n + sum_numbers(n - 1)


def sum_digits(number):
    # Base case
    if len(str(number)) == 1:
        return number
    # Recursion
    else:
        return number % 10 + sum_digits(number // 10)


def word_split(phrase, words_list, output=None):
    if output is None:
        output = []

    for word in words_list:
        # if phrase.startswith(word):
        if phrase[0:len(word)].lower() == word.lower():
            output.append(word)
            return word_split(phrase[1:], words_list, output)
    if output == words_list:
        return True
    return False


def reverse_string(string):
    """                          |-> base case
    "abc" => c ab => (cab) => cb a => cba
    """
    # Base case
    if len(string) == 1:
        return string
    # Recursion
    return reverse_string(string[1:]) + string[0]


def string_permutation(word):
    """
    Given a string, using recursion
    output a list with all possible permutations of it
    """
    # Set up
    permutations = []
    # Base case
    if len(word) == 1:
        permutations = [word]
    # Recursion
    else:
        for index, letter in enumerate(word):
            for permutation in string_permutation(word[:index] + word[index + 1:]):
                permutations += [letter + permutation]
    return permutations


def coin_change(target_amount, coins, known_results):
    """
    Given a target amount and an array with distinct coin values,
    return the fewest coins needed to achieve the target amount.
    10
    1+1+1+1+...+1 = 10
    1+1+1+1+1+5 = 10
    5+5 = 10
    10
    """
    # Setup
    minimum_amount = target_amount
    # Base case
    if target_amount in coins:
        known_results[target_amount] = 1
        return 1
    elif known_results[target_amount] > 0:
        return known_results[target_amount]
    else:
        for coin_value in [coin for coin in coins if coin <= target_amount]:
            coins_sum = 1 + coin_change(target_amount - coin_value, coins, known_results)
            if coins_sum < minimum_amount:
                minimum_amount = coins_sum
                known_results[target_amount] = minimum_amount
    return minimum_amount


def recursive_multiply(number1, number2):
    """
    Write a function that takes in two numbers and
    recursively multiplies them together.
    """
    if number1 < number2:
        return recursive_multiply(number2, number1)
    elif number2 != 0:
        return number1 + recursive_multiply(number1, number2 - 1)
    else:
        return 0


def recursive_exponential(base, exponential):
    """
    Write a function that takes in a base and an exp
    and recursively computes base**exp
    """
    if exponential == 1:
        return base
    else:
        return base * recursive_exponential(base, exponential - 1)


def recursive_prints(number, numbers_list=None):
    """
    Write a function using recursion
    to print numbers from n to 0.
    """
    if numbers_list is None:
        numbers_list = []
    if number >= 0:
        recursive_prints(number - 1, numbers_list)
        numbers_list.append(number)
        # print(number)
    return numbers_list


def check_if_prime(number, current_divisor=2):
    """
    Write a function using recursion
    to check if a number is prime
    """
    # Base cases
    if number <= 2:
        return True if number == 2 else False
    if number % current_divisor == 0:
        return False
    if current_divisor * current_divisor > number:
        return True
    # Recursion
    return check_if_prime(number, current_divisor + 1)


def recursive_fibonacci(number):
    """
    Write a recursive function that takes in one argument n and
    computes Fn, the nth value of the Fibonacci sequence.
    """
    # Base case
    if number == 0:
        return 0
    if number == 1:
        return 1
    return recursive_fibonacci(number - 1) + recursive_fibonacci(number - 2)


class TestRecursionExercises(object):

    @pytest.mark.parametrize("number, expected_result", [
        (4, 10), (0, 0)
    ])
    def test_sum_numbers(self, number, expected_result):
        assert sum_numbers(number) == expected_result

    def test_sum_digits(self):
        assert sum_digits(4321) == 10

    @pytest.mark.parametrize("param_phrase, param_words_list, expected_result", [
        ("abc", ["a", "b", "c"], True), ("abcd", ["ab", "c"], False)
    ])
    def test_word_split(self, param_phrase, param_words_list, expected_result):
        assert word_split(param_phrase, param_words_list) is expected_result

    def test_reverse_string(self):
        assert reverse_string("abc") == "cba"

    def test_string_permutation(self):
        assert string_permutation("abc") == ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    def test_coin_change(self):
        assert coin_change(74, [1, 5, 10, 25], [0] * (74 + 1)) == 8

    def test_recursive_multiplication(self):
        assert recursive_multiply(5, 2) == 10
        assert recursive_multiply(2, 3) == 6

    def test_recursive_exponential(self):
        assert recursive_exponential(2, 3) == 8
        assert recursive_exponential(3, 2) == 9

    def test_recursive_print(self):
        assert recursive_prints(4) == [0, 1, 2, 3, 4]
        assert recursive_prints(8) == [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def test_check_if_prime(self):
        assert check_if_prime(2) is True
        assert check_if_prime(7) is True
        assert check_if_prime(4) is False

    @pytest.mark.parametrize("param_number, expected_result", [
        (3, 2), (4, 3), (6, 8), (0, 0), (1, 1), (2, 1)
    ])
    def test_check_recursive_fibonacci(self, param_number, expected_result):
        assert recursive_fibonacci(param_number) == expected_result
