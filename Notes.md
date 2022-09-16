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

## Heap Sort

Heap Sort uses a binary tree organization of an array to sort higher values to the top of the binary tree. The process
of
moving larger values in the binary tree is called __heapifying__ (or heapify). The _max heap_ is when the entire
binary tree has the larger value be the parent value of two child values.

To heapify the binary tree the value of the parent index must be higher than the two children. Therefore, the process
starts at the bottom of the tree and works its way to the top. If the parent value is smaller than one of the child
values, the two swap positions. As the process continues higher values progressively more to the top of the binary
tree (closer to the head of the array).

When the max heap is formed, the highest values is at index and swaps with the value ar the highest index, removing that
index from the unsorted array.

To build the binary tree, each index (starting at 0), will have a left child and right child (hence binary) index. The
index values can be calculated from the following:

```
[5, 17, 13, 11, 1, 7, 3]

// SAMPLE TREE

        5[0]
        /   \
    17[1]    13[2]
   /   \     /   \
 11[3] 1[4] 7[5] 3[6]
 
// Caculate index of a child index
left_child_index = 2 * parent_index + 1
right_child_index = 2 * parent_index + 2
```