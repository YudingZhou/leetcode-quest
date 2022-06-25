"""
A heap is a tree data structure, that value of parent is always larger(or less) than its children.


A common representation of a heap is an arr forming a binary heap.
the children of node at index N are nodes at index 2N+1 and 2N+2.

The values of those nodes meet the following
    A max heap
     - Val(n) > Val(2n+1)
     - Val(n) > Val(2n+2)



    A min heap
     - Val(n) < Val(2n+1)
     - Val(n) < Val(2n+2)



ref : https://en.wikipedia.org/wiki/Heapsort
ref : https://en.wikipedia.org/wiki/Heap_(data_structure)


Example :

     [8,4,7,1,2,3,5]

n = 6 swap root and tail
              8
            /   \
           4     7
         / \    / \
        1  2   3   5

    re-create max heap
              5
            /   \
           4     7
         / \    / \
        1  2   3  [8]


n = 5 swap root and tail
              7
            /   \
           4     5
         / \    / \
        1  2   3   8

     re-create max heap
              3
            /   \
           4     5
         / \    / \
        1  2  [7   8]


n = 4 swap root and tail

              5
            /   \
           4     3
         / \    / \
        1  2   7   8

    re-create max heap
              2
            /   \
           4     3
         / \    / \
        1  [5  7  8]




n = 4 swap root and tail
              4
            /   \
           2     3
         / \    / \
        1  5   7   8

      recreate maxheap
              1
            /   \
           2     3
         / \    / \
       [4  5   7   8]

n = 3
              3
            /   \
           2     1
         / \    / \
        4  5   7   8
       recreate max heap
              1
            /   \
           2    [3
         / \    / \
        4  5   7   8]

n = 2
              2
            /   \
           1     3
         / \    / \
        4  5   7   8

n = 1
              1
            /   \
          [2     3
         / \    / \
        4  5   7   8]

n = 0
             [1
            /   \
           2     3
         / \    / \
        4  5   7   8]

"""

import unittest


def heapify(arr, n, m):
    # append a new element at the end(m) of the arr
    # the parent index is idx_parent
    idx_parent = int((m - 1) / 2)

    # if idx_parent is valid(larger than 0), and new element is larger(max heap) than its parent
    # switch parent and the new element
    # Bottom to the top, keep doing so and checking so with the next parent until idx_parent is not valid.
    while idx_parent >= n and arr[idx_parent] < arr[m]:
        tmp = arr[idx_parent]
        arr[idx_parent] = arr[m]
        arr[m] = tmp
        m = idx_parent
        idx_parent = int((idx_parent - 1) / 2)


def heap_sort(arr: list):
    for idx, val in enumerate(arr):
        heapify(arr, 0, idx)

    n = len(arr) - 1
    while n >= 0:

        # swap the root of heap and the last node
        tmp = arr[0]
        arr[0] = arr[n]
        arr[n] = tmp
        n = n - 1

        idx = 0

        # from top to bottom, re-generate a heap by checking over all parents
        # n is the last index
        # idx is the parent index
        # because, max n is 2*idx+2, min n is 2*idx+1
        # so, idx * 2 + 1 <= n (the minimum n value)
        while idx * 2 + 1 <= n:
            if idx * 2 + 2 <= n:  # there are 2 children
                if (arr[idx] < arr[idx * 2 + 1] or arr[idx] < arr[idx * 2 + 2]) and arr[idx * 2 + 1] < arr[idx * 2 + 2]:
                    tmp = arr[idx]
                    arr[idx] = arr[idx * 2 + 2]
                    arr[idx * 2 + 2] = tmp
                    idx = idx * 2 + 2
                elif (arr[idx] < arr[idx * 2 + 1] or arr[idx] < arr[idx * 2 + 2]) and arr[idx * 2 + 1] > arr[
                    idx * 2 + 2]:
                    tmp = arr[idx]
                    arr[idx] = arr[idx * 2 + 1]
                    arr[idx * 2 + 1] = tmp
                    idx = idx * 2 + 1
                else:
                    break
            elif idx * 2 + 1 <= n:  # there is only left child
                if arr[idx] < arr[idx * 2 + 1]:
                    tmp = arr[idx]
                    arr[idx] = arr[idx * 2 + 1]
                    arr[idx * 2 + 1] = tmp
                    idx = idx * 2 + 1
                else:
                    break


class Test(unittest.TestCase):
    def test1(self):
        arr = [1, 4, 3, 2, 5, 8, 7]
        heapify(arr, 0, 0)
        self.assertListEqual([1, 4, 3, 2, 5, 8, 7], arr)
        heapify(arr, 0, 1)
        self.assertListEqual([4, 1, 3, 2, 5, 8, 7], arr)
        heapify(arr, 0, 2)
        self.assertListEqual([4, 1, 3, 2, 5, 8, 7], arr)
        heapify(arr, 0, 3)
        self.assertListEqual([4, 2, 3, 1, 5, 8, 7], arr)
        heapify(arr, 0, 4)
        self.assertListEqual([5, 4, 3, 1, 2, 8, 7], arr)
        heapify(arr, 0, 5)
        self.assertListEqual([8, 4, 5, 1, 2, 3, 7], arr)
        heapify(arr, 0, 6)
        self.assertListEqual([8, 4, 7, 1, 2, 3, 5], arr)

    def test2(self):
        arr = [1, 4, 3, 2, 5, 8, 7]
        heap_sort(arr)
        self.assertListEqual([1, 2, 3, 4, 5, 7, 8], arr)
