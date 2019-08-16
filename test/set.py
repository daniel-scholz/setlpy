import unittest
from setlx.set import Set, List


class TestSet(unittest.TestCase):

    def test_empty_set(self):
        s = Set()
        self.assertIsNotNone(s)

    def test_init_set_of_set(self):
        s = Set(Set())
        self.assertEqual(s.tree.root.key, Set())

    def test_init_builtin(self):
        for i in range(-5, 5):
            s = Set([i])
            with self.subTest(i=i):
                self.assertEqual(s.tree.root.key, i)

    def test_init_iterable_mixed(self):
        s = Set(["a", 1])
        self.assertEqual(s.first(), 1)
        self.assertEqual(s.last(), "a")

    def test_init_iterable(self):
        s = Set([2, 1])
        self.assertEqual(s.first(), 1)
        self.assertEqual(s.last(), 2)

    def test_iter(self):
        s = Set(range(10))
        self.new_set = iter(s)
        self.assertEqual(s, self.new_set)
        self.assertEqual(self.new_set, s)

    def test_next_empty(self):
        s = Set()
        self.assertRaises(StopIteration, s.__next__)
        try:
            # catch stopiteration to check for return value
            self.assertIsNone(next(s))
        except StopIteration:
            pass

    def test_next(self):
        r = range(-5, 5)
        s = Set(r)
        for i in range(-5, 5):
            with self.subTest(i=i):
                self.assertEqual(next(s), i)

        self.assertRaises(StopIteration, s.__next__)

    def test_arb_empty(self):
        s = Set()
        self.assertIsNone(s.__arb__())

    def test_arb(self):
        # also checks method first and last
        i = 2
        s = Set(i)
        self.assertEqual(s.__arb__(), i)
        s = Set([i, i + 1, i+2])
        self.assertEqual(s.__arb__(), i+2)

    def test_get_item(self):
        s = Set([List(["a", 1])])
        self.assertEqual(s["a"], 1)

    def test_get_item_double_value(self):
        s = Set([List(["a", 1]), List(["a", 2])])
        self.assertIsNone(s["a"])

    def test_set_item(self):
        s = Set()
        i = 2
        s["a"] = i
        self.assertEqual(s["a"], i)

    def test_set_item_overwrite(self):
        s = Set()
        i = 2
        s["a"] = i
        s["a"] = i + 1
        s[2] = i**2
        self.assertEqual(s["a"], i + 1)
        self.assertEqual(s[2], i**2)

    def test_add(self):
        l = [1, 2, 3, 23, [1, 23], Set(), "abc"]
        s = Set()
        s += Set([1, 2, 3])
        s += Set([23, 2, 3, Set(), "abc", [1, 23]])
        for i, x in enumerate(s):
            with self.subTest(i=i):
                self.assertEqual(x, l[i])

    def test_sub(self):
        s = Set([1, 2, 3, 23, 2, 3, Set(), "abc", [1, 23]])
        l = [1, 2, 3, 23, [1, 23], Set(), "abc"]
        for i, x in enumerate(s):
            with self.subTest(i=i, length=len(s)):
                self.assertEqual(x, l[i])
                old_length = len(s)
                s -= Set([l[i]])
                self.assertGreater(old_length, len(s))

    def test_intersect(self):
        i = 123
        s = Set([1, i, 2, 3, 23, 2, 3, Set(), "abc", [1, 23]])
        s2 = Set([i])
        self.assertEqual((s2*s).__arb__(), i)
        s2 = Set([i+1])
        self.assertIsNone((s2*s).__arb__())

    def test_powerset(self):
        s = Set([[5, "a"], 2, Set([17])])

        ps = Set([Set(), Set([[5, "a"]]), Set([2]), Set([Set([17])]), Set([[5, "a"], 2]),
                  Set([[5, "a"], Set([17])]), Set([2, Set([17])]), Set([[5, "a"], 2, Set([17])])])
        self.assertEqual(s.power_set(), ps)

        e = Set()
        pe = Set([Set()])
        self.assertEqual(e.power_set(), pe)

        e = Set(Set())
        pe = Set([Set(), Set(Set())])
        self.assertEqual(e.power_set(), pe)

    def test_cartesian(self):
        s = Set(["a", 2, Set()])
        s_cartesian = Set([["a", 2], [2, "a"], [Set(), "a"], ["a", Set()], [
                          Set(), 2], [2, Set()], ["a", "a"], [Set(), Set()], [2, 2]])
        self.assertEqual(s ** 2, s_cartesian)

        e = Set()
        e_cartesian = Set()
        self.assertEqual(e**2, e_cartesian)

        e = Set(Set())
        e_cartesian = Set([[Set(), Set()]])
        self.assertEqual(e**2, e_cartesian)

    def test_comparions(self):
        e = Set()

        s = Set(["a", 2, e, [3, 2]])
        self.assertTrue(e < s)
        self.assertTrue(e <= s)
        self.assertFalse(e == s)
        self.assertFalse(e >= s)
        s2 = Set(["a", 2])
        self.assertTrue(s2 < s)
        self.assertTrue(s2 <= s)
        self.assertFalse(s2 == s)
        self.assertFalse(s2 >= s)

        s3 = Set(["a", 2, e, [3, 2]])
        self.assertFalse(s3 < s)
        self.assertTrue(s3 <= s)
        self.assertTrue(s3 == s)
        self.assertTrue(s3 >= s)

        s3 = Set(["a", 2, e, [3, 2], "b"])
        self.assertFalse(s3 < s)
        self.assertFalse(s3 <= s)
        self.assertFalse(s3 == s)
        self.assertTrue(s3 >= s)
        self.assertTrue(s3 > s)

    def test_find(self):
        s = Set(["a", 2, Set(), [3, 2], "b"])
        self.assertIsNotNone(s.find("a"))
        self.assertIsNone(s.find(""))
        self.assertIsNotNone(s.find(Set()))

    def test_domain(self):
        s = Set([List(["a", 2]), List(["b", 2]), List(["c", 2]),
                 List(["a", 2]), 2, Set(), List([3, 2])])
        dom = Set([2, 3, Set(), 'a', 'b', 'c'])
        self.assertEqual(s.__domain__(), dom)

        s = Set()
        dom = Set()
        self.assertEqual(s.__domain__(), dom)

    def test_range(self):
        s = Set([List(["a", 2]),
                 List(["b", "pizza"]), List(["c", Set([42])]),
                 List(["a", 2]), List([3, 2])])
        rang = Set([2, "pizza", Set([42])])
        self.assertEqual(s.__range__(), rang)


if __name__ == "__main__":
    """Executes all unit tests, when the test package itself is called"""
    unittest.main()

# TODO: fix linear iterations
