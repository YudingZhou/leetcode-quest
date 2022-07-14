"""
Given

[ "high", "way", "highway", "rock", "star", "rockstar"]

Find a list of words from the given list, forming compound words in the given list.

"""


def findParts(_input):
    listOfWords = [word for word in _input]
    part = ""
    ret = []
    for word in listOfWords:
        for letter in word:
            part = part + letter
            if listOfWords.__contains__(part) and word != part:
                ret.append(part)
                part = ""
        part = ""
    return ret


from unittest import TestCase as tc


class Test(tc):
    def test1(self):
        given = ["high", "way", "highway", "rock", "star", "rockstar"]
        found = findParts(given)
        self.assertListEqual(found, ["high", "way", "rock", "star"])
