# b_mergeSort.py
"""
Title: Merge Sort
Author: Beatrix Bicomong
Date-created: 14-09-2022
"""
from myFunctions import *


def mergeSortedList(LIST_LEFT, LIST_RIGHT):
    """
    merge two sorted lists
    :param LIST_LEFT: list (int)
    :param LIST_RIGHT: list (int)
    :return: list (int)
    """

    # Special Case: one or both lists are empty
    if len(LIST_LEFT) == 0:
        return LIST_RIGHT
    elif len(LIST_RIGHT) == 0:
        return LIST_LEFT

    # General Case
    INDEX_LEFT = 0
    INDEX_RIGHT = 0
    LIST_MERGE = []  # List to build and return
    LIST_LEN_TOTAL = len(LIST_LEFT) + len(LIST_RIGHT)

    while len(LIST_MERGE) < LIST_LEN_TOTAL:
        if LIST_LEFT[INDEX_LEFT] <= LIST_RIGHT[INDEX_RIGHT]:
            LIST_MERGE.append(LIST_LEFT[INDEX_LEFT])
            INDEX_LEFT += 1
        else:
            LIST_MERGE.append(LIST_RIGHT[INDEX_RIGHT])
            INDEX_RIGHT += 1

        # if we are at the end of one of the lists, we can take a shortcut
        if INDEX_RIGHT == len(LIST_RIGHT):
            LIST_MERGED = LIST_MERGE + LIST_LEFT[INDEX_LEFT:]
            break
        elif INDEX_LEFT == len(LIST_LEFT):
            LIST_MERGED = LIST_MERGE + LIST_RIGHT[INDEX_RIGHT:]
            break

    return LIST_MERGED


def mergeSort(INPUT_LIST):
    if len(INPUT_LIST) <= 1:
        # base case
        return INPUT_LIST
    else:
        MIDPOINT = len(INPUT_LIST) // 2
        LEFT = INPUT_LIST[:MIDPOINT]
        RIGHT = INPUT_LIST[MIDPOINT:]
        return mergeSortedList(mergeSort(LEFT), mergeSort(RIGHT))


if __name__ == "__main__":
    TIMES = []
    for i in range(30):
        NUMBERS = getRandomList(10000)
        START = getTime()
        NUMBERS = mergeSort(NUMBERS)
        END = getTime()
        TIMES.append(END - START)
    print(getAverage(TIMES))
