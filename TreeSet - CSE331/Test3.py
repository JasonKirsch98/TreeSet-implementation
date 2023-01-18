#!/usr/bin/python3

import unittest

from TreeSet import TreeSet


def natural_order(x, y):
    if x == y:
        return 0
    elif x < y:
        return -1
    else:
        return 1


def reverse_order(x, y):
    return natural_order(y, x)

class TreeSetTests(unittest.TestCase):

    def test_is_empty(self):
        tree = TreeSet(natural_order)
        self.assertTrue(tree.is_empty())
        tree.insert(0)
        self.assertFalse(tree.is_empty())
        tree.remove(0)
        self.assertTrue(tree.is_empty())

    def test_len(self):
        tree = TreeSet(natural_order)
        self.assertEqual(0, len(tree))
        for i in range(0, 10):
            tree.insert(i)
            self.assertEqual(i + 1, len(tree))
        for i in range(0, 10):
            tree.insert(i)
            self.assertEqual(10, len(tree))

    def test_height(self):
        import math
        tree = TreeSet(natural_order)
        sequence = [5, 7, 3, 6, 4, 8, 9, 2, 1]
        x = tree.height()
        self.assertEqual(-1, tree.height())
        for index, item in enumerate(sequence):
            tree.insert(item)
            self.assertGreaterEqual(index, tree.height())
            self.assertLessEqual(math.floor(math.log(index + 1,2)), tree.height())

    def test_insert(self):
        tree = TreeSet(natural_order)
        sequence = [5, 7, 3, 6, 4, 8, 9, 2, 1]
        for item in sequence:
            self.assertFalse(item in tree)
            self.assertTrue(tree.insert(item))
            self.assertTrue(item in tree)
        for item in sequence:
            self.assertTrue(item in tree)
            self.assertFalse(tree.insert(item))
            self.assertTrue(item in tree)

    def test_remove(self):
        tree = TreeSet(natural_order)
        sequence = [5, 7, 3, 6, 4, 8, 9, 2, 1, 0]
        for item in sequence:
            tree.insert(item)
        for item in range(0, 10):
            self.assertTrue(item in tree)
            self.assertTrue(tree.remove(item))
            self.assertFalse(item in tree)
            self.assertFalse(tree.remove(item))
            self.assertFalse(item in tree)

    def test_contains(self):
        tree = TreeSet(natural_order)
        sequence = [5, 7, 3, 6, 4, 8, 9, 2, 1, 0]
        for item in sequence:
            self.assertFalse(item in tree)
            tree.insert(item)
            self.assertTrue(item in tree)
        for item in range(0, 10):
            self.assertTrue(item in tree)
            tree.remove(item)
            self.assertFalse(item in tree)

    def test_first(self):
        tree = TreeSet(natural_order)
        self.assertRaises(KeyError, tree.first)
        tree.insert(5)
        self.assertEqual(5, tree.first())
        tree.insert(7)
        self.assertEqual(5, tree.first())
        tree.insert(3)
        self.assertEqual(3, tree.first())
        tree.insert(6)
        self.assertEqual(3, tree.first())
        tree.insert(4)
        self.assertEqual(3, tree.first())
        tree.insert(8)
        self.assertEqual(3, tree.first())
        tree.insert(9)
        self.assertEqual(3, tree.first())
        tree.insert(2)
        self.assertEqual(2, tree.first())
        tree.insert(1)
        self.assertEqual(1, tree.first())
        tree.insert(0)
        self.assertEqual(0, tree.first())

    def test_last(self):
        tree = TreeSet(natural_order)
        self.assertRaises(KeyError, tree.last)
        tree.insert(5)
        self.assertEqual(5, tree.last())
        tree.insert(7)
        self.assertEqual(7, tree.last())
        tree.insert(3)
        self.assertEqual(7, tree.last())
        tree.insert(6)
        self.assertEqual(7, tree.last())
        tree.insert(4)
        self.assertEqual(7, tree.last())
        tree.insert(8)
        self.assertEqual(8, tree.last())
        tree.insert(9)
        self.assertEqual(9, tree.last())
        tree.insert(2)
        self.assertEqual(9, tree.last())
        tree.insert(1)
        self.assertEqual(9, tree.last())
        tree.insert(0)
        self.assertEqual(9, tree.last())

    def test_clear(self):
        tree = TreeSet(natural_order)
        sequence = [5, 7, 3, 6, 4, 8, 9, 2, 1, 0]
        for item in sequence:
            tree.insert(item)
        self.assertFalse(tree.is_empty())
        tree.clear()
        self.assertTrue(tree.is_empty())
        self.assertRaises(KeyError, tree.first)
        self.assertRaises(KeyError, tree.last)

    def test_iter(self):
        tree = TreeSet(natural_order)
        sequence = [5, 7, 3, 6, 4, 8, 9, 2, 1, 0]
        for i in sequence:
            tree.insert(i)
        for x, y in zip(range(0, 10), tree):
            self.assertEqual(x, y)

    def test_reverse(self):
        tree = TreeSet(reverse_order)
        sequence = [5, 7, 3, 6, 4, 8, 9, 2, 1, 0]
        for i in sequence:
            tree.insert(i)
        for x, y in zip(reversed(range(0, 10)), tree):
            self.assertEqual(x, y)


if __name__ == '__main__':
    unittest.main()
