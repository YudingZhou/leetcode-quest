"""
a variant of longest common substring.

1.

s1 = 12345
s2 = 22344

expected_result = 234



2.

s1 = 12345
s2 = 125

expected_result = 12


the common string must be consecutive in its origin.

SOLUTION:

cue:
 - the answer is a subset of the question
 - the question can be divided into sub-questions
 - sub-questions have overlapping computation

strategy & implementation:

 - recursion : dividing the question into sub-questions
    1. set up the beginning sub-question and the ending sub-question
        - beginning condition is the extreme case at one end
        - the returning value of this beginning question is usually a constant
            e.g. in binary search, the beginning is that length of the array is 0;
              and the returning value is -1 as being not able to find given number
              when the length has become 0.
            e.g. in longest_common_substring question, the beginning question is when
                either one string's length becomes 0, and the returning value is 0.

    2. the ending question will be the ending point of recursive call
        - top-down approach
            1. imagine the last question is F(x)
            2. F(x) can be divided as F(Q(x)), e.g. F(x) = F(x-1) + F(x-2)
            3. Q(x) is the logic relationship between current question and its immediate sub-questions, namely the logic
             of recursion.
    3. the beginning question will be the entry of recursive call
        - at this point, try to draw a recursive call tree, this helps understand how sub-questions divide
            e.g.
                abc^ab
                 /  \
            ab^ab    abc^a
              |        / \
             a^a   ab^a  abc^
                   /  \
                a^a   ab^


 - memoization : avoid overlapping computation
    1. depends on the nature of the parameter of recursion, 1D array, 2D array etc., can be used for storing
        intermediate results
    2. the intermediate result is returned at the beginning before recursion logic
        - depends on the nature of the question, sometimes, the ending sub-question can be prior to the returning of
            the intermediate result.
    3. the intermediate result is stored at the end of the recursion logic.




Analysis
    1. factors for a context
       - if S1[m] == S2[n]
       - the longest result of the sub-question
       - the current consecutive common string
       * whether the current consecutive common string is longer than longest of the sub-question.
         If yes, replace the longest one with consecutive.
         if no, passing on both, current consecutive one and longest one.
            * this is extra requirement from "Longest Common Substring" question, which does not require the substring
            being consecutive


"""

import unittest


def lcs0(s1, s2, m, n, l):
    if m < 0 or n < 0:
        return l

    if s1[m] == s2[n]:
        # current position matched, shorten both strings and increase L by 1
        return lcs0(s1, s2, m - 1, n - 1, l + 1)
    else:
        # reset L as current position does not match
        return max(l,  # return previous length if previous one is longer, or either one runs out of length
                   max(lcs0(s1, s2, m, n - 1, 0),  # go further left
                       lcs0(s1, s2, m - 1, n, 0)))  # go further right


def lcs(s1, s2, m, n, l, lcs_map):
    if m < 0 or n < 0:
        return l

    else:
        r = -1
        if s1[m] == s2[n]:
            if lcs_map[m][n] > -1:
                r = lcs_map[m][n] + l
            else:
                r = lcs(s1, s2, m - 1, n - 1, l + 1, lcs_map)
                lcs_map[m][n] = r
        else:
            if lcs_map[m][n] > -1:
                r = lcs_map[m][n]
            else:
                r = max(lcs(s1, s2, m, n - 1, 0, lcs_map), lcs(s1, s2, m - 1, n, 0, lcs_map))
                lcs_map[m][n] = r

        return lcs_map[m][n]


def lcs2(s1, s2, m, n, lcs_map):
    if lcs_map[m][n] > -1:
        return lcs_map[m][n]

    if m < 0 or n < 0:
        return 0

    if s1[m] == s2[n]:
        lcs_map[m][n] = 1 + lcs2(s1, s2, m - 1, n - 1, lcs_map)
    else:
        lcs_map[m][n] = max(lcs2(s1, s2, m, n - 1, lcs_map), lcs2(s1, s2, m - 1, n, lcs_map))

    return lcs_map[m][n]


def lcs3(s1, s2, m, n, L, lcs_map):
    if m < 0 or n < 0:
        return 0
    # be very careful, index of python list can be negative, so always check the index before using it.
    if lcs_map[m][n] > -1:
        return lcs_map[m][n]

    if s1[m] == s2[n]:
        r = lcs3(s1, s2, m - 1, n - 1, L + 1, lcs_map) + 1
    else:
        r = max(L,
                max(lcs3(s1, s2, m - 1, n, 0, lcs_map),
                    lcs3(s1, s2, m, n - 1, 0, lcs_map)))

    lcs_map[m][n] = r
    return lcs_map[m][n]


def lcs4(s1, s2, m, n, lcs_map) -> (bool, int):
    if m < 0 or n < 0:
        return False, 0

    if lcs_map[m][n] is not None:
        return lcs_map[m][n]

    if s1[m] == s2[n]:
        branch, L = lcs4(s1, s2, m - 1, n - 1, lcs_map)
        if not branch:
            r = max(1, L)
        else:
            r = L + 1
        b = True
    else:
        x, L_left = lcs4(s1, s2, m - 1, n, lcs_map)
        x, L_right = lcs4(s1, s2, m, n - 1, lcs_map)

        r = max(L_left, L_right)
        b = False

    lcs_map[m][n] = b, r

    return b, r


def lcs5(s1, s2, m, n, lcs_map, S) -> (bool, int, str):
    if m < 0 or n < 0:
        return False, 0, ""

    if lcs_map[m][n] is not None:
        return lcs_map[m][n]

    if s1[m] == s2[n]:
        appendable, L, S = lcs5(s1, s2, m - 1, n - 1, lcs_map, s1[m])
        if not appendable:
            if L > 1:
                r = L
            else:
                S = s1[m]
                r = 1
        else:
            r = L + 1
            S = S + s1[m]
            print(S)
        b = True
    else:
        x, L_left, S1 = lcs5(s1, s2, m - 1, n, lcs_map, S)
        x, L_right, S2 = lcs5(s1, s2, m, n - 1, lcs_map, S)

        r = max(L_left, L_right)
        if L_left > L_right:
            S = S1
        else:
            S = S2
        b = False

    lcs_map[m][n] = b, r, S

    return b, r, S


def lcs6(s1, s2, m, n, lcs_map) -> (int, int):
    if m < 0 or n < 0:
        return 0, 0

    if lcs_map[m][n] is not None:
        return lcs_map[m][n]

    if s1[m] == s2[n]:
        longest, pending = lcs6(s1, s2, m - 1, n - 1, lcs_map)
        pending = pending + 1

    else:
        longest_l, pending_l = lcs6(s1, s2, m - 1, n, lcs_map)
        if longest_l < pending_l:
            longest_l = pending_l
        longest_r, pending_r = lcs6(s1, s2, m, n - 1, lcs_map)
        if longest_r < pending_r:
            longest_r = pending_r
        longest = max(longest_l, longest_r)
        pending = 0

    lcs_map[m][n] = longest, pending

    return longest, pending


def lcs7(s1, s2, m, n, lcs_map) -> (int, int, str, str):
    if m < 0 or n < 0:
        return 0, 0, "", ""

    if lcs_map[m][n] is not None:
        return lcs_map[m][n]

    if s1[m] == s2[n]:
        longest, pending, S_l, S_p = lcs7(s1, s2, m - 1, n - 1, lcs_map)
        pending = pending + 1
        S_p = S_p + s1[m]
    else:
        longest_l, pending_l, S_l_l, S_l_p = lcs7(s1, s2, m - 1, n, lcs_map)
        if longest_l < pending_l:
            longest_l = pending_l
            S_l_l = S_l_p

        longest_r, pending_r, S_r_l, S_r_p = lcs7(s1, s2, m, n - 1, lcs_map)
        if longest_r < pending_r:
            longest_r = pending_r
            S_r_l = S_r_p

        if longest_l < longest_r:
            longest = longest_r
            S_l = S_r_l
        else:
            longest = longest_l
            S_l = S_l_l

        pending = 0
        S_p = ""

    lcs_map[m][n] = longest, pending, S_l, S_p

    return longest, pending, S_l, S_p


def lcs8(s1, s2) -> (int, str):
    longest, pending, S_l, S_p = lcs7(s1, s2, len(s1) - 1, len(s2) - 1,
                                      [[None for i in range(0, len(s2))] for j in range(0, len(s1))])

    if longest < pending:
        longest = pending
        S_l = S_p

    return longest, S_l


class Test(unittest.TestCase):

    @staticmethod
    def init_lcs_map(s1, s2):
        return [[None for i in range(0, len(s2))] for j in range(0, len(s1))]

    def test1(self):
        s1 = '112123'
        s2 = '212124'
        l = lcs7(s1, s2, len(s1) - 1, len(s2) - 1, self.init_lcs_map(s1, s2))
        self.assertEqual(l[0], 4)

    def test2(self):
        s1 = "qpe"
        s2 = "qpg"
        l = lcs7(s1, s2, len(s1) - 1, len(s2) - 1, self.init_lcs_map(s1, s2))
        self.assertEqual(l[0], 2)

    def test2_1(self):
        s1 = "ylqpejqbalahwr"
        s2 = "yrkzavgdmdgtqpg"
        l = lcs7(s1, s2, len(s1) - 1, len(s2) - 1, self.init_lcs_map(s1, s2))
        self.assertEqual(l[0], 2)

    def test3(self):
        s1 = '123'
        s2 = '124'
        l = lcs7(s1, s2, len(s1) - 1, len(s2) - 1, self.init_lcs_map(s1, s2))
        self.assertEqual(l[0], 2)

    def test3_1(self):
        s1 = '11'
        s2 = '21'
        longest, S = lcs8(s1, s2)
        self.assertEqual(1, longest)
        self.assertEqual("1", S)

    def test3_2(self):
        s1 = '1'
        s2 = '1'
        longest, S = lcs8(s1, s2)
        self.assertEqual(1, longest)
        self.assertEqual("1", S)

    def test4(self):
        s1 = "abcde"
        s2 = "ace"
        l = lcs7(s1, s2, len(s1) - 1, len(s2) - 1, self.init_lcs_map(s1, s2))
        self.assertEqual(l[0], 1)

    def test5(self):
        s1 = "abcd"
        s2 = "ace"
        l = lcs7(s1, s2, len(s1) - 1, len(s2) - 1, self.init_lcs_map(s1, s2))
        self.assertEqual(l[0], 1)

    def test6(self):
        s1 = "abcde"
        s2 = "ace"
        l, s = lcs8(s1, s2)
        self.assertEqual(l, 1)

    def test6_2(self):
        s1 = "abc"
        s2 = "ace"
        l = lcs7(s1, s2, len(s1) - 1, len(s2) - 1, self.init_lcs_map(s1, s2))
        self.assertEqual(l[0], 1)

    def test8(self):
        s1 = "abcde"
        s2 = "ace"
        l, s = lcs8(s1, s2)
        self.assertEqual(l, 1)

    def test9(self):
        s1 = '123'
        s2 = '124'
        l, s = lcs8(s1, s2)
        self.assertEqual(l, 2)

    def test9_1(self):
        s1 = '112123'
        s2 = '212124'
        l, s = lcs8(s1, s2)
        self.assertEqual(l, 4)

    def test12(self):
        s1 = "ashdasjduwwdjsabwysbdbxjhfdyeb"
        s2 = "dsaufybdjbdabcuwhdfogoqjsau"
        l, s = lcs8(s1, s2)
        self.assertEqual(3, l)

    def test13(self):
        s1 = "abcdefg"
        s2 = "fbce"
        l, s = lcs8(s1, s2)
        self.assertEqual(2, l)

    def test14(self):
        s1 = "qwe123qwe"
        s2 = "as12sa"
        l, s = lcs8(s1, s2)
        self.assertEqual(2, l)

    def test15(self):
        s1 = "2"
        s2 = "123"
        l, s = lcs8(s1, s2)
        self.assertEqual(1, l)

    def test16(self):
        s1 = "ashdasjduwwdjsabwysbdbxjhfdyeb"
        s2 = "dsaufybdjbdabcuwhdfogoqjsau"
        lcs_map = [[None for i in range(0, len(s2))] for j in range(0, len(s1))]
        l = lcs7(s1, s2, len(s1) - 1, len(s2) - 1, lcs_map)
        self.assertEqual(3, l[0])
        self.assertEqual("jsa", l[2])

    def test17(self):
        s1 = "4847653456484135132156484sada5sd46aw8d12d1ag68ds41g5fas46g6s4df84hd98tr4jku4u564kl1659871k678drts5gd1651vc65zs1c65W1AD6 CS8E16FG68R1BG5FD1T6HDRT5SY4TFD65S4G1A65WEFEA6GF5165561fa65df1a83f "
        s2 = "654S8D5645a648fg46654GS65AD465F465g4s65df48g948rg16s5fd1b658y16hf5d1b681s9e86f1awz5d1v6z5df1b6gnd165ng6fjh4s8ad4f98a6wer5b4n6t5y1m6,5jh46889kj4sh86d4f55a6se4g5as6d5fa6sd45f6a8wefa84"
        lcs_map = [[None for i in range(0, len(s2))] for j in range(0, len(s1))]
        l = lcs7(s1, s2, len(s1) - 1, len(s2) - 1, lcs_map)
        self.assertEqual(4, l[0])
        self.assertEqual("d165", l[2])
