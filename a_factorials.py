# a_factorials
"""
Title: Factorial Recursion
Author: Beatrix Bicomong
Date: 12-09-2022
"""


def recursiveFactorial(NUMBER):
    """
    calculates the factorial of the given number (recursive)
    :param NUMBER: int
    :return: int
    """
    if NUMBER == 0:
        # base case
        return 1
    else:
        return NUMBER * recursiveFactorial(NUMBER - 1)


def iterativeFactorial(NUMBER):
    """
    calculates the factorial of the given number (iterative)
    :param NUMBER:
    :return:
    """
    NUM = 1

    for i in range(1, NUMBER+1):
        NUM *= i
    return NUM


if __name__ == "__main__":
    NUM = int(input("Enter a number: "))

    if NUM < 0:
        print("Sorry, factorials don't exist for negative numbers")
    else:
        FACTORIAL = iterativeFactorial(NUM)

    print(f"The factorial of {NUM} is {FACTORIAL}.")
