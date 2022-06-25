"""
1. ending question
  - length(arr) == 0.
    -- if n > m, continue
    -- if n <= m, stop and return ENDING_RESULT (-1)
2. beginning question
    - if the middle value equals the given one
      -- return value is the middle index
3. recursion point
    - splitting the array into 2, each half will continue the routine
"""



def binary_search(arr, m, n, x) -> int:
    if n > m:
        mid = int((m + n) / 2)
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:

            return binary_search(arr, m, mid, x)
        else:
            return binary_search(arr, mid + 1, n, x)
    else:
        return -1


import unittest


class Test(unittest.TestCase):
    def test1(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        self.assertTrue(3, binary_search(arr, 0, len(arr) - 1, 4))

    def test1(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        self.assertTrue(-1, binary_search(arr, 0, len(arr) - 1, 0))
