import sys
from typing import List
from unittest import TestCase as tc


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_size = 0
        for i in range(0, len(height)):
            for j in range(i + 1, len(height)):
                current_size = (j - i) * min(height[i], height[j])
                max_size = max(max_size, current_size)
        return max_size


class Solution2:
    def maxArea(self, heights: List[int]) -> int:
        max_size = 0
        index, max_height = self.max_height_and_index(sys.maxsize, heights)
        for i in range(0, len(heights)):
            if index > -1:
                size = self.max_size(index, heights)
                max_size = max(size, max_size)
                index, max_height = self.max_height_and_index(max_height, heights)

        return max_size

    @staticmethod
    def max_height_and_index(ceiling: int, vals: List[int]) -> (int, int):
        current_max_height = 0
        current_index = -1
        for index, height in enumerate(vals):
            if ceiling > height > current_max_height:
                current_index = index
                current_max_height = height
        return current_index, current_max_height

    @staticmethod
    def max_size(index, heights: List[int]):
        max_size = 0
        for i in range(0, len(heights)):
            max_size = max(max_size, abs(index - i) * min(heights[i], heights[index]))
        return max_size


class Solution3:
    def maxArea(self, heights: List[int]) -> int:
        index_left = 0
        index_right = heights.__len__() - 1
        max_size = 0
        while index_right > index_left:
            current_size = min(heights[index_left], heights[index_right]) * (index_right - index_left)
            max_size = max(current_size, max_size)
            if heights[index_left] < heights[index_right]:
                index_left = index_left + 1
            else:
                index_right = index_right - 1
        return max_size


class Test(tc):
    def test1(self):
        given = [2, 3, 1, 2, 1]
        result = Solution().maxArea(given)
        self.assertEqual(6, result)

    def test2(self):
        given = [2, 3, 1, 2, 1]
        result = Solution2().maxArea(given)
        self.assertEqual(6, result)

    def test3(self):
        given = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        result = Solution2().maxArea(given)
        self.assertEqual(49, result)

    def test4(self):
        given = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        result = Solution3().maxArea(given)
        self.assertEqual(49, result)
