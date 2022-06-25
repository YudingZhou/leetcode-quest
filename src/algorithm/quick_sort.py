"""
 1. recursive level 1, choose 5 as the pivot, splitting
 S = [5, 4, 7, 6, 2, 1, 3]
 P = 5
      S = [4, 2, 1, 3, (5), 7, 6]

          2.1 recursive level 2
          S1 = [4, 2, 1, 3]
          P = 4
                    3.1 recursive level 3
                    S = [2, 1, 3, (4)]
                    S1 = [2, 1 ,3]
                        P = 2
                            S = [1, (2), 3]
                            S1 = [1]
                            S2 = [3]

                    S2 = []

          2.2 recursive level 2
          S2 = [7, 6]
          P = 7
                    S = [6, (7)]
                    S1 = [6]
                    S2 = []

recursive tree level - 1
    S = [4, 2, 1, 3, (5), 7, 6]

recursive tree level - 2
    S = [ 2, 1, 3, ((4)), (5), 6, ((7))]

recursive tree level - 3
    S = [ 1, (((2))), 3, ((4)), (5), 6, ((7))]
"""


def pivot(arr, m, n, pivot_idx) -> int:
    for idx in range(m, n + 1):
        if arr[idx] < arr[pivot_idx]:
            arr[idx], arr[pivot_idx] = arr[pivot_idx], arr[idx]
            pivot_idx = idx
    return pivot_idx


def quick_sort(arr, m, n):
    if n > m:
        pivot_idx = pivot(arr, m, n, m)
        """
        caveat, shall the pivot not be included in the subroutine
        previously, implementation is as the following
            quick_sort(arr, m, pivot_idx )
        the pivot gets included in one of the sub-routine which is wrong.
        """
        quick_sort(arr, m, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, n)
    return arr


from unittest import TestCase as tc


class Test(tc):
    def test1(self):
        arr = [5, 4, 2, 1, 3, 7, 6]
        pivot(arr, 0, len(arr) - 1, 0)
        self.assertListEqual([4, 2, 1, 3, 5, 7, 6], arr)

    def test2(self):
        arr = [2, 1]
        pivot(arr, 0, len(arr) - 1, 0)
        self.assertListEqual([1, 2], arr)

    def test3(self):
        arr = [1]
        pivot(arr, 0, len(arr) - 1, 0)
        self.assertListEqual([1], arr)

    def test4(self):
        arr = [1, 1]
        pivot(arr, 0, len(arr) - 1, 0)
        self.assertListEqual([1, 1], arr)


class Test2(tc):
    def test1(self):
        arr = [5, 4, 2, 1, 3, 7, 6]
        self.assertListEqual([1, 2, 3, 4, 5, 6, 7], quick_sort(arr, 0, len(arr) - 1))

    def test2(self):
        arr = [2, 1]
        self.assertListEqual([1, 2], quick_sort(arr, 0, len(arr) - 1))

    def test3(self):
        arr = [1]
        self.assertListEqual([1], quick_sort(arr, 0, len(arr) - 1))

    def test4(self):
        arr = [1, 1]
        self.assertListEqual([1, 1], quick_sort(arr, 0, len(arr) - 1))
