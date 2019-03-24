import unittest

from setlx import Vector


class VectorTest(unittest.TestCase):

    def test_to_str(self):
        v = Vector(1, 2, 3)
        self.assertEqual(str(v), "<<1 2 3>>")

    def test_add(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector(5, 2, 3)
        result = Vector(6, 4, 6)
        self.assertEqual(v1+v2, result)

    def test_sub(self):
        v1 = Vector(5, 2, 3)
        v2 = Vector(1, 2, 3)
        result = Vector(4, 0, 0)
        self.assertEqual(v1-v2, result)

    def test_scalar_mult(self):
        v1 = Vector(5, 2, 3)
        a = 2
        result = Vector(10, 4, 6)
        self.assertEqual(a * v1, result)

    def test_dot_product(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector(3, 2, 1)
        result = 1*3+2*2+3*1
        self.assertEqual(v1*v2, result)

    def test_index_assignment(self):
        v1 = Vector(1, 2, 3)
        v1[0] = 0
        result = Vector(0, 2, 3)
        self.assertEqual(v1, result)


if __name__ == '__main__':
    unittest.main()
