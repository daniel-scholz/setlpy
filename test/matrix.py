import unittest

from setlx import Matrix


class MatrixTest(unittest.TestCase):

    def test_to_str(self):
        v = Matrix([[1, 2], [2, 1]])
        self.assertEqual(str(v), "<< <<1 2>> <<2 1>> >>")

    def test_add(self):
        v1 = Matrix([[1, 2, 3], [2, 3, 1], [3, 2, 1]])
        v2 = Matrix([[0, 5, 1], [1, 1, 1], [12, 10, 0]])
        result = Matrix([[1, 7, 4], [3, 4, 2], [15, 12, 1]])
        self.assertEqual(v1+v2, result)

    def test_sub(self):
        v1 = Matrix([[1, 7, 4], [3, 4, 2], [15, 12, 1]])
        v2 = Matrix([[1, 2, 3], [2, 3, 1], [3, 2, 1]])
        result = Matrix([[0, 5, 1], [1, 1, 1], [12, 10, 0]])
        self.assertEqual(v1-v2, result)

    def test_scalar_mult(self):
        v = Matrix([[1, 2], [2, 1]])
        a = 2
        result = Matrix([[2, 4], [4, 2]])
        self.assertEqual(a * v, result)

    def test_product(self):
        v1 = Matrix([[1, 2], [2, 1]])
        v2 = Matrix([[3, 5], [2, 1]])
        result = Matrix([[7, 7], [8, 11]])
        self.assertEqual(v1*v2, result)

    def test_pow(self):
        v1 = Matrix([[1, 2], [2, 1]])
        result = Matrix([[4, 8], [8, 4]])
        print(result)
        self.assertEqual(v1**4, result)


if __name__ == '__main__':
    unittest.main()
