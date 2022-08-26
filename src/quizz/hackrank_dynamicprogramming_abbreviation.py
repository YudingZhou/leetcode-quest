import unittest


def abbreviation(a, b):
    matched_indexes = []
    matched_result = lcs(a, len(a) - 1, b, len(b) - 1, [[None for b in b] for a in a], matched_indexes)

    if matched_result.lower() == b.lower():
        assert len(matched_result) == len(matched_indexes)

        idx_in_b = 0

        for idx_in_a, letter_in_a in enumerate(a):
            if not matched_indexes.__contains__(idx_in_a):
                if ord('Z') >= ord(a[idx_in_a]) >= ord('A'):
                    # letters except for matched ones in a are upper case which cannot be deleted.
                    return "NO"
            else:
                if ord(a[idx_in_a]) - ord(b[idx_in_b]) == -32:
                    # letter in a is upper case and letter in b is lower case
                    return "NO"
                idx_in_b = idx_in_b + 1

        return "YES"

    else:
        return "NO"


# connected upper case letters must be matched as a block


def lcs_block(a, a_idx, b, b_idx) -> str:
    length_of_upper_case_block = 0
    # get the upper letter block
    temp_index = a_idx
    while ord('A') <= ord(a[temp_index]) <= ord('Z') and temp_index > -1:
        length_of_upper_case_block = length_of_upper_case_block + 1
        temp_index = temp_index - 1
    b_start_idx = b_idx - length_of_upper_case_block
    a_start_idx = a_idx - length_of_upper_case_block
    if b_start_idx < 0:
        return ""

    if a[a_start_idx:a_idx + 1] == b[b_start_idx:b_idx + 1]:
        sub_lcs = lcs_block(a,
                            a_start_idx - 1,
                            b,
                            b_start_idx - 1)
        current_lcs = f"{sub_lcs}{a[a_idx - length_of_upper_case_block:a_idx + 1]}"

    else:
        current_lcs = lcs_block(a,
                                a_start_idx - 1,
                                b,
                                b_idx)

    return current_lcs


def lcs(a, idx_a, b, idx_b, memo, index_collector: list) -> str:
    if idx_a < 0 or idx_b < 0:
        return ""

    if memo[idx_a][idx_b] is not None:
        return memo[idx_a][idx_b]

    if a[idx_a] == b[idx_b]:
        index_collector.append(idx_a)
        sub_lcs = lcs(a, idx_a - 1, b, idx_b - 1, memo, index_collector)
        current_lcs = f"{sub_lcs}{a[idx_a]}"
    else:
        current_lcs = lcs(a, idx_a - 1, b, idx_b, memo, index_collector)

    memo[idx_a][idx_b] = current_lcs

    return current_lcs


class Test(unittest.TestCase):
    def test1(self):
        given_a = "1"
        given_b = "12"
        collector = []
        cut = lcs(given_a, len(given_a) - 1, given_b, len(given_b) - 1, [[None for b in given_b] for a in given_a],
                  collector)
        self.assertEqual("", cut)
        self.assertListEqual([], collector)

    def test2(self):
        given_a = "11"
        given_b = "11"
        collector = []
        cut = lcs(given_a, len(given_a) - 1, given_b, len(given_b) - 1, [[None for b in given_b] for a in given_a],
                  collector)
        self.assertEqual("11", cut)
        self.assertListEqual([1, 0], collector)

    def test3(self):
        given_a = "123"
        given_b = "13"
        collector = []
        cut = lcs(given_a, len(given_a) - 1, given_b, len(given_b) - 1, [[None for b in given_b] for a in given_a],
                  collector)
        self.assertEqual("13", cut)
        self.assertListEqual([2, 0], collector)

    def test4(self):
        given_a = "1234"
        given_b = "24"
        collector = []
        cut = lcs(given_a, len(given_a) - 1, given_b, len(given_b) - 1, [[None for b in given_b] for a in given_a],
                  collector)
        self.assertEqual("24", cut)
        self.assertListEqual([3, 1], collector)


class Test2(unittest.TestCase):
    def test1(self):
        given_a = "AbcDE"
        given_b = "ABDE"
        cut = abbreviation(given_a, given_b)
        self.assertEqual("YES", cut)

    def test2(self):
        given_a = "AbcDE"
        given_b = "AFDE"
        cut = abbreviation(given_a, given_b)
        self.assertEqual("NO", cut)

    def test3(self):
        given_a = "daBcd"
        given_b = "ABC"
        cut = abbreviation(given_a, given_b)
        self.assertEqual("YES", cut)

    def test4(self):
        given_a = "KXzQ"
        given_b = "K"
        cut = abbreviation(given_a, given_b)
        self.assertEqual("NO", cut)

    def test5(self):
        given_a = "SYIHDDSMREKXOKRFDQAOZJQXRIDWXPYINFZCEFYyxu"
        given_b = "SYIHDDSMREKXOKRFDQAOZJQXRIDWXPYINFZCEFY"
        cut = abbreviation(given_a, given_b)
        self.assertEqual("YES", cut)


def convert_input(given_input, given_result):
    given_input = given_input.strip().split("\n")
    given_result = given_result.strip().split("\n")
    for idx, val in enumerate(given_result):
        yield (given_input[idx * 2], given_input[idx * 2 + 1], given_result[idx])


class Test3(unittest.TestCase):
    def test1(self):
        given_input = """
        XXVVnDEFYgYeMXzWINQYHAQKKOZEYgSRCzLZAmUYGUGILjMDET
XXVVDEFYYMXWINQYHAQKKOZEYSRCLZAUYGUGILMDETQVWU
PVJSNVBDXABZYYGIGFYDICWTFUEJMDXADhqcbzva
PVJSNVBDXABZYYGIGFYDICWTFUEJMDXAD
QOTLYiFECLAGIEWRQMWPSMWIOQSEBEOAuhuvo
QOTLYFECLAGIEWRQMWPSMWIOQSEBEOA
DRFNLZZVHLPZWIupjwdmqafmgkg
DRFNLZZVHLPZWI
SLIHGCUOXOPQYUNEPSYVDaEZKNEYZJUHFXUIL
SLIHCUOXOPQYNPSYVDEZKEZJUHFXUIHMGFP
RYASPJNZEFHEORROXWZFOVDWQCFGRZLWWXJVMTLGGnscruaa
RYASPJNZEFHEORROXWZFOVDWQCFGRZLWWXJVMTLGG
AVECtLVOXKPHIViTZViLKZCZAXZUZRYZDSTIHuCKNykdduywb
AVECLVOXKPHIVTZVLKZCZAXZUZRYZDSTIHCKN
wZPRSZwGIMUAKONSVAUBUgSVPBWRSTJZECxMTQXXA
ZPRSZGIMUAKONSVAUBUSVPBWRSTJZECMTQXXA
SYIHDDSMREKXOKRFDQAOZJQXRIDWXPYINFZCEFYyxu
SYIHDDSMREKXOKRFDQAOZJQXRIDWXPYINFZCEFY
EIZGAWWDCSJBBZPBYVNKRDEWVZnSSWZIw
EIZGAWWDCSJBBZPBYVNKRDEWVZSSWZI
        """
        given_result = """
        NO
YES
YES
YES
NO
YES
YES
YES
YES
YES"""

        for a, b, result in convert_input(given_input, given_result):
            cut = abbreviation(a, b)
            self.assertEqual(result, cut, msg=f"{a}\n{b}\n{result}")


class Test4(unittest.TestCase):
    def test1(self):
        a = "YYYYy"
        b = "YYYY"
        cut = lcs_block(a, len(a) - 1, b, len(b) - 1)
        self.assertEqual("YYYY", cut)
