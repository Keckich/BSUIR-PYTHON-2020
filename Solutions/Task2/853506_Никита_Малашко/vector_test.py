import unittest
from vector import Vector


class TestVector(unittest.TestCase):
    def setUp(self):
        self.vector1 = Vector(4, 32, 1, 6, 10)
        self.vector2 = Vector(46, 2, 7, 9, 5)
        self.vector3 = Vector(4, 5, 1)
        self.vector4 = Vector()

    def test_sum(self):
        self.assertEqual(self.vector1 + self.vector2, Vector(50, 34, 8, 15, 15))
        self.assertEqual('ERROR: Vectors of different sizes', self.vector2 + self.vector3)

    def test_sub(self):
        self.assertEqual(self.vector2 - self.vector1, Vector(42, -30, 6, 3, -5))
        self.assertEqual('ERROR: Vectors of different sizes', self.vector2 - self.vector3)

    def test_mul(self):
        self.assertEqual(self.vector2 * 2, Vector(92, 4, 14, 18, 10))
        self.assertEqual(self.vector1 * self.vector2, Vector(184, 64, 7, 54, 50))
        self.assertEqual('ERROR: Vectors of different sizes', self.vector2 * self.vector3)

    def test_equal(self):
        self.assertFalse(self.vector1 == self.vector2)
        self.assertTrue(self.vector1 != self.vector2)
        self.assertEqual(self.vector1 == self.vector3, False)

    def test_len(self):
        self.assertEqual(len(self.vector2), 5)
        self.assertEqual(len(self.vector4), 0)

    def test_str(self):
        self.assertEqual(str(self.vector2), '46, 2, 7, 9, 5')
        self.assertEqual(str(self.vector4), '')

    def test_index(self):
        self.assertEqual(self.vector2[0], 46)



