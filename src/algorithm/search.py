"""

array as a binary tree

let, arr[x] is the parent

then, arr[2*x + 1] and arr[2*x +2] are the children

[1,2,3,4,5,6,7,8]

             1
           /  \
          2    3
        / \   / \
       4   5 6   7
      /
     8
"""

import unittest


def visit(val):
    print(val)


# given list as a binary tree, search over the tree for x

def dfs(arr: list, idx: int):
    if idx < len(arr):
        idx_left = 2 * idx + 1
        idx_right = 2 * idx + 2

        visit(arr[idx])
        dfs(arr, idx_left)
        dfs(arr, idx_right)


def bfs(arr: list):
    # casl, AKA., Children At the Same Level
    casl = [0]
    for idx in casl:
        visit(arr[idx])
        idx_left = idx * 2 + 1
        if idx_left < len(arr):
            casl.append(idx_left)

        idx_right = idx * 2 + 2
        if idx_right < len(arr):
            casl.append(idx_right)


class Test(unittest.TestCase):
    def test1(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8]
        dfs(arr, 0)

    def test2(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8]
        bfs(arr)
