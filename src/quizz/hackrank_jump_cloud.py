def jumpingOnClouds(c):
    steps = 0
    current_idx = 0
    while current_idx < len(c):
        if current_idx + 2 < len(c) and c[current_idx + 2] == 0:  # greedy for local maximum result 
            current_idx = current_idx + 2
        else:
            current_idx = current_idx + 1
        steps = steps + 1
    return steps - 1


from unittest import TestCase as tc


class Test1(tc):
    def test1(self):
        given = [0, 0, 1, 0, 0, 1, 0]
        cut = jumpingOnClouds(given)
        self.assertEqual(4, cut)

    def test2(self):
        given = [0, 0, 0, 1, 0, 0]
        cut = jumpingOnClouds(given)
        self.assertEqual(3, cut)
