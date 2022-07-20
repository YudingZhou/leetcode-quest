import unittest
import re
import sys


def hourglassSum(arr):
    bound = 4
    max_sum = - sys.maxsize - 1
    for r in range(bound):
        for c in range(bound):
            current_sum = arr[r][c] + arr[r][c + 1] + arr[r][c + 2] + arr[r + 1][c + 1] + arr[r + 2][c] + arr[r + 2][
                c + 1] + arr[r + 2][c + 2]
            if current_sum > max_sum:
                max_sum = current_sum
                print(f"new max_sum: {max_sum}")

    return max_sum


def convertGridTo2DList(grid: str, converter=lambda val: val) -> list:
    spaces = re.compile("\\s+")
    rows = grid.split("\n")
    twoD_list = []
    for row in rows:
        row = row.strip()
        if len(row) > 0:
            row = spaces.split(row)
            row_list = []
            for val in row:
                converted_val = converter(val)
                row_list.append(converted_val)
            twoD_list.append(row_list)
    return twoD_list


class Test(unittest.TestCase):
    def test1(self):
        given = """
        -9 -9 -9  1 1 1 
         0 -9  0  4 3 2
        -9 -9 -9  1 2 3
         0  0  8  6 6 0
         0  0  0 -2 0 0
         0  0  1  2 4 0
         """
        given = convertGridTo2DList(given, lambda val: int(val))
        cut = hourglassSum(given)
        self.assertEqual(cut, 28)
