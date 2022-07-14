class SuffixTrieNode:
    def __str__(self):
        return f"{self.children}=>{self.positions}"

    def __init__(self):
        self.children = {}
        self.positions = []

    def build(self, S):
        for idx, val in reversed(list(enumerate(S))):
            self.insert(idx, S)

    def insert(self, suffix_position_idx, whole_string):
        node = self
        current_letter_idx = suffix_position_idx
        while len(node.children) > 0 and current_letter_idx < len(whole_string):
            if node.children.__contains__(whole_string[current_letter_idx]):
                node = node.children[whole_string[current_letter_idx]]
                current_letter_idx += 1

        if len(node.children) > 0:
            node.positions.append(suffix_position_idx)
        else:
            while current_letter_idx < len(whole_string):
                node.children[whole_string[current_letter_idx]] = SuffixTrieNode()
                node = node.children[whole_string[current_letter_idx]]
                current_letter_idx += 1
            node.positions.append(suffix_position_idx)


from unittest import TestCase as tc


class Test1(tc):
    def test1(self):
        S = "11"
        n = SuffixTrieNode()
        n.build(S)
        self.assertEqual(n.children.__len__(), 1)
        self.assertEqual(n.positions.__len__(), 0)
        self.assertIsNotNone(n.children["1"])
        n = n.children["1"]
        self.assertEqual(n.children.__len__(), 1)
        self.assertEqual(n.positions.__len__(), 1)
        self.assertEqual(n.positions[0], 1)
        n = n.children["1"]
        self.assertEqual(n.children.__len__(), 0)
        self.assertEqual(n.positions.__len__(), 1)
        self.assertEqual(n.positions[0], 0)

    def test2(self):
        S = "12"
        n = SuffixTrieNode()
        n.build(S)
        self.assertEqual(n.children.__len__(), 2)
        self.assertEqual(n.positions.__len__(), 0)
        self.assertIsNotNone(n.children["1"])
        self.assertEqual(n.children["1"].children.__len__(), 1)
        self.assertEqual(n.children["2"].children.__len__(), 1)
        self.assertEqual(n.children["1"].positions.__len__(), 1)
        self.assertEqual(n.children["2"].positions.__len__(), 0)
        self.assertEqual(n.children["1"].chilren.__len__(), 1)
        self.assertEqual(n.children["1"].chilren["2"].children.__len__(), 0)

