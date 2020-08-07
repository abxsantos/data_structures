import pytest

"""
Give the nth entry in the fibonacci series.
"""


def iterative_fibonacci(n):
    fib_array = [0, 1]
    i = 2
    while i <= n:
        last_value = fib_array[-1]
        prev_from_last_value = fib_array[-2]
        fib_array.append(last_value + prev_from_last_value)
        i += 1
    return fib_array[n]


def recursive_fibonacci(n):
    """WTF right?"""
    if n < 2:
        return n
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


class TestFibonacci(object):

    @pytest.mark.parametrize('given_index, expected_result', [
        (0, 0), (1, 1), (5, 5), (6, 8)
    ])
    def test_iterative_fibonacci(self, given_index, expected_result):
        assert iterative_fibonacci(given_index) == expected_result

    @pytest.mark.parametrize('given_index, expected_result', [
        (0, 0), (1, 1), (5, 5), (6, 8)
    ])
    def test_recursive_fibonacci(self, given_index, expected_result):
        assert recursive_fibonacci(given_index) == expected_result
