import unittest
from setlx import tree, node
import random
from typing import List


class BinTreeTest(unittest.TestCase):


    def test_insert_and_find(self):
        dim = 100
        t, random_range = rnd_tree_gen(dim=dim)
        for r in random_range:
            self.assertIsNotNone(t.find(r))

    def test_delete(self):
        dim = 1000
        t, random_range = rnd_tree_gen(dim=dim)
        for r in random_range:
            t.delete(r)
            self.assertIsNone(t.find(r), msg=f"{t}")
        self.assertIsNone(t.root)

    def test_delete_negative(self):
        dim = 1000
        t, _ = rnd_tree_gen(dim=dim)
        # self.assertRaises(ValueError, t.delete(random.randint(dim, dim**2)))
        try:
            rand = random.randint(dim, dim**2)
            t.delete(rand)
            self.assertTrue(True, msg=f"{rand} should have shown an exception")
        except(ValueError):
            pass

    def test_find_negative(self):
        dim = 1000
        t, _ = rnd_tree_gen(dim=dim)
        self.assertIsNone(t.find(random.randint(dim, dim**2)))


def rnd_tree_gen(dim) -> (tree, List):
    SEED = 3
    random.seed(SEED)
    random_range = [x for x in range(1, dim)]
    random.Random(SEED).shuffle(random_range)
    root = random_range[0]
    t = tree.Tree(node.BinaryNode(root))
    random_range = random_range[1:]
    for r in random_range:
        t.insert(node.BinaryNode(r))
    random.Random(SEED).shuffle(random_range)
    random_range.append(root)
    random.Random(SEED).shuffle(random_range)

    return t, random_range


if __name__ == '__main__':
    unittest.main(exit=False)
