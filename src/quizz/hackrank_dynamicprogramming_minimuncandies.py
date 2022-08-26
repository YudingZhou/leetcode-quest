import unittest


def candies_to_give_at_index(index, arr, memo):
    if index < 0:
        return 0

    if memo[index] != -1:
        return memo[index]
    if index == len(arr) - 1:
        if arr[index] > arr[index - 1]:
            candies = candies_to_give_at_index(index - 1, arr, memo)
        else:
            candies = 1
    else:
        if arr[index] > arr[index - 1]:
            candies = candies_to_give_at_index(index - 1, arr, memo)
        else:
            pass

    memo[index] = candies

    return candies


def candies(n, arr):
    memo = [-1 for idx in range(len(arr))]
    total_candies = 0
    for idx, val in enumerate(arr):
        total_candies = total_candies + candies_to_give_at_index(idx, arr, memo)

    return total_candies


def candies3(n, arr):
    memo = [1 for idx in range(len(arr))]

    for index in range(len(arr) - 1):
        if arr[index + 1] > arr[index]:
            memo[index + 1] = memo[index] + 1

    for index in reversed(range(1,len(arr))):
        if arr[index - 1] > arr[index] and memo[index - 1] <= memo[index]:
            memo[index - 1] = memo[index] + 1

    print(memo)
    return sum(memo)


def canies2(n, arr):
    memo = [1 for idx in range(len(arr))]
    if len(arr) == 1:
        return 1
    for index in range(1, len(arr)):
        if arr[index] > arr[index - 1]:
            memo[index] = memo[index - 1] + 1
        else:  # arr[index] < arr[index - 1]:
            memo[index] = 1
            if memo[index - 1] == 1:
                for fallback_index in reversed(range(index)):
                    if arr[fallback_index] > arr[fallback_index + 1] and \
                            memo[fallback_index] <= memo[fallback_index + 1]:
                        memo[fallback_index] = memo[fallback_index + 1] + 1
                    else:
                        break
    print(memo)
    return sum(memo)


class Test(unittest.TestCase):
    def test1(self):
        given = [4, 6, 4, 5, 6, 2]
        cut = canies2(len(given), given)
        self.assertEqual(10, cut)

    def test2(self):
        given = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]
        cut = canies2(len(given), given)
        self.assertEqual(19, cut)


class Test2(unittest.TestCase):
    def test1(self):
        given = [4, 6, 4, 5, 6, 2]
        cut = candies3(len(given), given)
        self.assertEqual(10, cut)

    def test2(self):
        given = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]
        cut = candies3(len(given), given)
        self.assertEqual(19, cut)
