import unittest


def minimumBribes(q):
    # print(f"input {q}")
    minimum_bribes = 0
    for current_index in range(len(q)):
        original_index = q[current_index] - 1
        if original_index - 2 <= current_index < len(q):
            if current_index > original_index:
                if current_index + 1 < len(q) and q[current_index] > q[current_index + 1]:
                    minimum_bribes = minimum_bribes + 1
                if current_index + 2 < len(q) and q[current_index] > q[current_index + 2]:
                    minimum_bribes = minimum_bribes + 1
            elif current_index < original_index:
                minimum_bribes = minimum_bribes + (original_index - current_index)
        else:
            print("Too chaotic")
            return "Too chaotic"

    print(minimum_bribes)
    return minimum_bribes


class Test(unittest.TestCase):
    def test1(self):
        given = [1, 2, 5, 3, 7, 8, 6, 4]
        cut = minimumBribes(given)
        self.assertEqual(cut, 7)

    def test2(self):
        given = [5, 1, 2, 3, 7, 8, 6, 4]
        cut = minimumBribes(given)
        self.assertEqual("Too chaotic", cut)
