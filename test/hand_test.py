"""Testing hand states, eg. tenpai, furiten, fu, shanten, ukeire etc."""

import unittest

class TestTenpai(unittest.TestCase):

    def test_hand1(self):
        self.assertEqual('foo', 'foo')

class TestFuriten(unittest.TestCase):

    def test_hand1(self):
        self.assertEqual('foo', 'foo')

class TestFu(unittest.TestCase):

    def test_hand1(self):
        self.assertEqual('foo', 'foo')

class TestShanten(unittest.TestCase):
    
    def test_hand1(self):
        self.assertEqual('foo', 'foo')

class TestUkeIre(unittest.TestCase):

    def test_hand1(self):
        self.assertEqual('foo', 'foo')

if __name__ == '__main__':
    unittest.main()