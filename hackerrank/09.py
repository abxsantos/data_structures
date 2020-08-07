"""
Given numbers between 1 and n inclusive,
print Fizz if the number is divisible by 3,
buzz if by 5,
FizzBuzz if by 3 and 5,
otherwise print the number.
"""


def fizz_buzz(n):
    for number in range(1, n):
        if number % 3 == 0 and number % 5 == 0:
            print("FizBuzz")
        elif number % 5 == 0:
            print("Buzz")
        elif number % 3 == 0:
            print("Fizz")
        else:
            print(number)

