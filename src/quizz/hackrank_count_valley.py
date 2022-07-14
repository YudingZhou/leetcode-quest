def countingValleys(steps, path):
    level = 0
    val = 0
    for step in path:
        if level == 0 and step == "D":
            val = val + 1

        if step == "D":
            level = level - 1
        else:
            level = level + 1

    return val


from unittest import TestCase as tc


class Test1(tc):
    def test1(self):
        given = "DDUUDDUDUUUD"
        cut = countingValleys(12, given)
        self.assertEqual(2, cut)
