def rottenTime(grid, m, n):
    visited = []  # a list recording all nodes at the same depth
    for row_idx, row in enumerate(grid):  # initialize all cells with value as 2
        for col_idx, cell in enumerate(row):
            if grid[row_idx][col_idx] == 2:
                visited.append((row_idx, col_idx))

    depth = -1

    while len(visited) > 0:  # BFS search starts
        node_size_at_current_depth = len(visited)  # count amount of nodes at current depth
        depth = depth + 1  # increase depth by 1
        while node_size_at_current_depth > 0:  # visit all nodes at current depth
            current_cell = visited.pop()
            node_size_at_current_depth = node_size_at_current_depth - 1

            current_x = current_cell[0]
            current_y = current_cell[1]
            top = current_y + 1
            down = current_y - 1
            left = current_x - 1
            right = current_x + 1

            if top < n and grid[current_x][top] == 1:  # visit top
                grid[current_x][top] = 2               # if it is a fresh apple, mark it as rotten
                visited.append((current_x, top))       # and add it to the list as the nodes at next depth.
            if down >= 0 and grid[current_x][down] == 1:  # visit down
                grid[current_x][down] = 2
                visited.append((current_x, down))
            if left >= 0 and grid[left][current_y] == 1:  # visit left
                grid[left][current_y] = 2
                visited.append((left, current_y))
            if right < m and grid[right][current_y] == 1:  # visit right
                grid[right][current_y] = 2
                visited.append((right, current_y))

    if depth == 0:  # edge case handling, see test case 3.
        return -1
    else:
        return depth


from unittest import TestCase as tc


class Test(tc):
    def test1(self):
        given = [[0, 1, 0],
                 [1, 2, 1],
                 [0, 1, 0]]
        cut = rottenTime(given, 3, 3)
        self.assertEqual(1, cut)

    def test2(self):
        given = [[0, 1, 0],
                 [1, 2, 1],
                 [0, 1, 1]]
        cut = rottenTime(given, 3, 3)
        self.assertEqual(2, cut)

    def test3(self):
        given = [[1, 0, 1],
                 [0, 2, 0],
                 [1, 0, 1]]
        cut = rottenTime(given, 3, 3)
        self.assertEqual(-1, cut)
