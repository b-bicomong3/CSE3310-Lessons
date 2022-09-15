# CSE3310 Recursive Algorthm Notes

## Merge Sort

Merge sort follows a divide and conquer method of sorting, where the array is split into its base length and then
rebuilt by combining progressively larger sorted lists together. The recursive portion is the splitting of the list and
the iterative portion is the actual merging of the two smaller sorted lists into a single larger sorted list.

Often times, this function is separated into splitting and merging functions.

## Quick Sort

Quick sort (or quicksort) is another divide and conquer method of sorting. Quick sort uses an arbitrary value as its
pivot. That value will be placed in its correct position within the array. It does this by comparing and placing smaller
values on the left side of the array and larger values on the right side of the array. Then it switches the pivot with
the right-most less than value. Within the two unsorted halves of the array, the algorthm recurs until all values are
placed. 