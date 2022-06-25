"""
n : starting index
m : ending index
"""

import unittest


def binary_search(arr: list, n, m, x: int):
    if m == n: return arr[m] == x

    idx_mid = int(n + (m - n) / 2)
    val_mid = arr[idx_mid]
    if val_mid == x:
        return idx_mid
    elif val_mid > x:
        return binary_search(arr, n, idx_mid, x)
    else:
        return binary_search(arr, idx_mid + 1, m, x)




class TestCase(unittest.TestCase):
    def test1(self):
        arr = [1]
        binary_search(arr, 0, len(arr) - 1, 1)

    def test2(self):
        arr = [1, 2, 4, 5, 6, 7]
        binary_search(arr, 0, len(arr) - 1, 7)


