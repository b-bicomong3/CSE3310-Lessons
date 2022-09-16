# d_heapSort.py

"""
Title: Heap Sort
Author: Beatrix Bicomong
Date-created: 16-09-2022
"""
from myFunctions import *


def heapify(LIST, LEN_ARRAY, ROOT_INDEX):
    """
    heapify all subtrees in the binary tree
    :param LIST: list (int)
    :param LEN_ARRAY: int - length of the array
    :param ROOT_INDEX: int - Parent index
    :return:
    """

    LARGEST_INDEX = ROOT_INDEX
    LEFT_INDEX = 2 * ROOT_INDEX + 1
    RIGHT_INDEX = 2 * ROOT_INDEX + 2

    # Test if left child value is larger than largest index value
    if LEFT_INDEX < LEN_ARRAY and LIST[ROOT_INDEX] < LIST[LEFT_INDEX]:
        LARGEST_INDEX = LEFT_INDEX

    # Test if right child value is larger than largest index value
    if RIGHT_INDEX < LEN_ARRAY and LIST[LARGEST_INDEX] < LIST[RIGHT_INDEX]:
        LARGEST_INDEX = RIGHT_INDEX

    # Change ROOT if needed
    if LARGEST_INDEX != ROOT_INDEX:
        TEMP = LIST[ROOT_INDEX]
        LIST[ROOT_INDEX] = LIST[LARGEST_INDEX]
        LIST[LARGEST_INDEX] = TEMP

        # Heapify the ROOT
        heapify(LIST, LEN_ARRAY, LARGEST_INDEX)


def heapSort(LIST):
    """
    sorts the list
    :param LIST: list (int)
    :return: None
    """

    LEN_ARRAY = len(LIST)

    # Build a max heap
    for i in range(LEN_ARRAY, -1, -1):
        heapify(LIST, LEN_ARRAY, i)

    # One by one extract the elements
    for i in range(LEN_ARRAY - 1, 0, -1):
        LIST[i], LIST[0] = LIST[0], LIST[i]  # swaps values
        heapify(LIST, i, 0)

