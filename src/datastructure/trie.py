'''
Trie AKA prefix tree
https://en.wikipedia.org/wiki/Suffix_tree

common usage - https://en.wikipedia.org/wiki/Suffix_tree#Applications
'''
import collections
import unittest


class Trie:
    def __init__(self):
        self.is_word = False
        self.children = {}

    def insert(self, word: str) -> None:
        node = self
        for letter in word:
            if not node.children.__contains__(letter):
                node.children[letter] = Trie()
            node = node.children[letter]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self
        for letter in word:
            if not node.children.__contains__(letter):
                return False
            node = node.children[letter]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        children = self.children
        for letter in prefix:
            if not children.__contains__(letter):
                return False
            children = children[letter].children
        return True


class Test(unittest.TestCase):
    def test1(self):
        t = Trie()
        t.insert("abc")

    def test2(self):
        t = Trie()
        t.insert("abc")
        self.assertTrue(t.startsWith('a'))
        self.assertFalse(t.startsWith('b'))

    def test3(self):
        t = Trie()
        t.insert("abc")
        self.assertTrue(t.search('abc'))
        self.assertFalse(t.search('a'))

    def test4(self):
        t = Trie()
        t.insert("a")
        self.assertTrue(t.startsWith('a'))
        self.assertTrue(t.search('a'))
