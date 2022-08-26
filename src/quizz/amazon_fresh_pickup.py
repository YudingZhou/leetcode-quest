import unittest


def findMaxProducts(products):
    sum_arr = [[] for val in products]

    max_ = 0
    for index in reversed(range(len(products))):
        threshold = products[index]
        currentIndex = index
        currentSum = threshold
        while threshold > 1 and currentIndex > 0:
            threshold = min(threshold - 1, products[currentIndex - 1])
            currentSum = currentSum + threshold
            currentIndex = currentIndex - 1

        max_ = max(currentSum, max_)

    return max_


class Test(unittest.TestCase):
    def test1(self):
        given = [7, 4, 5, 2, 6, 5]
        self.assertEqual(findMaxProducts(given), 12)

    def test2(self):
        given = [2, 9, 4, 7, 5, 2]
        self.assertEqual(findMaxProducts(given), 16)

    def test3(self):
        given = [2, 5, 6, 7]
        self.assertEqual(findMaxProducts(given), 20)
