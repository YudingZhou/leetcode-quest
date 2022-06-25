import unittest


def lcs(s1, s2, m, n, lcs_map):
    if m < 0 or n < 0:
        return 0

    if lcs_map[m][n] != -1:
        return lcs_map[m][n]

    if s1[m] == s2[n]:
        r = lcs(s1, s2, m - 1, n - 1, lcs_map) + 1

    else:
        r = max(
            lcs(s1, s2, m - 1, n, lcs_map),
            lcs(s1, s2, m, n - 1, lcs_map))

    lcs_map[m][n] = r

    return r


class Test(unittest.TestCase):
    def test1(self):
        s1 = '1'
        s2 = '0'
        l = lcs(s1, s2, len(s1) - 1, len(s2) - 1, [[-1 for y in range(len(s2))] for x in range(len(s1))])
        self.assertEqual(0, l)

    def test2(self):
        s1 = '1'
        s2 = '1'
        l = lcs(s1, s2, len(s1) - 1, len(s2) - 1, [[-1 for y in range(len(s2))] for x in range(len(s1))])
        self.assertEqual(1, l)

    def test3(self):
        s1 = '1234'
        s2 = '14'
        l = lcs(s1, s2, len(s1) - 1, len(s2) - 1, [[-1 for y in range(len(s2))] for x in range(len(s1))])
        self.assertEqual(2, l)

    def test4(self):
        s1 = '123'
        s2 = '23'
        l = lcs(s1, s2, len(s1) - 1, len(s2) - 1, [[-1 for y in range(len(s2))] for x in range(len(s1))])
        self.assertEqual(2, l)

    def test5(self):
        s1 = '123567890'
        s2 = 'x2x5x7x'
        l = lcs(s1, s2, len(s1) - 1, len(s2) - 1, [[-1 for y in range(len(s2))] for x in range(len(s1))])
        self.assertEqual(3, l)
