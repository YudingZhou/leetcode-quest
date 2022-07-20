"""
Top-down approach

Given a subset at index n as S(n) = {n, S(n-2)} or {n, S{n-3}}

e.g.  S(n) = {n, n-2, n-4, n-6, ... , 0}   or
      S(n) = {n, n-3, n-5, n-7, ... , 0}

Given, max_sum(S(n)) >= max_sum(S(n-2)) and max_sum(S(n-3))


so, max sum of S(n) = max(S(n-2) + n, S(n-3) + n)


0. let max_sum(S(n)) is the max sum amount all subsets of S(n); S(n) subsets is {n, S(n-2)} or {n, S(n-3)}

1. ending condition:
    idx = 0, val = arr[0]
    idx = 1, val = max(arr[0], arr[1])
    idx = 2, val = max_sum(arr[2] + idx[0])
2. recursive condition:
    idx > 2, val = max_sum(arr[idx] + max_sum(idx - 2), arr[idx] + max_sum(idx - 3))

"""

import unittest


def maxSubsetSum(arr):
    max_sum = 0
    for idx, val in enumerate(arr):
        max_sum = max(
            max_sum,
            maxSumOfSubsetAt(idx, arr)
        )
    return max_sum


def maxSubsetSumMemoization(arr):
    memo = [-1 for val in arr]
    max_sum = 0
    for idx, val in enumerate(arr):
        max_sum = max(
            max_sum,
            maxSumOfSubsetAt_memoization(idx, arr, memo)
        )
    return max_sum


def maxSumOfSubsetAt_memoization(idx: int, arr, memo):
    if idx < 0:
        return 0

    if memo[idx] > -1:
        return memo[idx]

    max_sum = 0
    if idx < 2:
        max_sum = arr[idx]
    else:
        potential_previous_index = idx - 2
        if arr[idx] > 0:
            potential_max_sum = max(maxSumOfSubsetAt_memoization(potential_previous_index, arr, memo) + arr[idx],
                                    maxSumOfSubsetAt_memoization(potential_previous_index - 1, arr, memo) + arr[idx])
        else:
            potential_max_sum = max(maxSumOfSubsetAt_memoization(potential_previous_index, arr, memo),
                                    maxSumOfSubsetAt_memoization(potential_previous_index - 1, arr, memo))

        max_sum = max(max_sum, potential_max_sum)

    max_sum = max(0, max_sum)

    memo[idx] = max_sum

    return max_sum


def maxSumOfSubsetAt(idx: int, arr):
    max_sum = 0
    if idx < 2:
        max_sum = arr[idx]
    else:
        for potential_previous_index in range(idx - 1):
            potential_max_sum = 0
            if arr[idx] > 0:
                potential_max_sum = maxSumOfSubsetAt(potential_previous_index, arr) + arr[idx]
            else:
                potential_max_sum = maxSumOfSubsetAt(potential_previous_index, arr)

            max_sum = max(max_sum, potential_max_sum)

    return max(0, max_sum)


class Test(unittest.TestCase):
    def test1(self):
        given = [-2, 1, 3, -4, 5]
        cut = maxSubsetSum(given)
        self.assertEqual(8, cut)

    def test2(self):
        given = [3, 7, 4, 6, 5]
        cut = maxSubsetSum(given)
        self.assertEqual(13, cut)

    def test3(self):
        given = [3, 5, -7, 8, 10]
        cut = maxSubsetSum(given)
        self.assertEqual(15, cut)

    def test4(self):
        given = [-2, -3, -1]
        cut = maxSubsetSum(given)
        self.assertEqual(0, cut)


class Test2(unittest.TestCase):
    def test1(self):
        given = [-2, 1, 3, -4, 5]
        cut = maxSubsetSumMemoization(given)
        self.assertEqual(8, cut)

    def test2(self):
        given = [3, 7, 4, 6, 5]
        cut = maxSubsetSumMemoization(given)
        self.assertEqual(13, cut)

    def test3(self):
        given = [3, 5, -7, 8, 10]
        cut = maxSubsetSumMemoization(given)
        self.assertEqual(15, cut)

    def test4(self):
        given = [-2, -3, -1]
        cut = maxSubsetSumMemoization(given)
        self.assertEqual(0, cut)
