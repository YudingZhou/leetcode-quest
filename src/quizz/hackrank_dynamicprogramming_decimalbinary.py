import unittest


def toInt(decibinary):
    digits = str(decibinary)
    int_val = 0
    for index in reversed(range(len(digits))):
        deci_digit = int(digits[index]) * pow(2, len(digits) - index - 1)
        int_val = int_val + deci_digit

    return int_val


class Test(unittest.TestCase):
    def test1(self):
        given = 1
        cut = toInt(given)
        self.assertEqual(1, cut)

    def test2(self):
        given = 0
        cut = toInt(given)
        self.assertEqual(0, cut)

    def test3(self):
        given = 10
        cut = toInt(given)
        self.assertEqual(2, cut)

    def test4(self):
        given = 110
        cut = toInt(given)
        self.assertEqual(6, cut)

    def test5(self):
        given = 12
        cut = toInt(given)
        self.assertEqual(4, cut)

    def test6(self):
        for i in range(1100):
            print(toInt(i))
