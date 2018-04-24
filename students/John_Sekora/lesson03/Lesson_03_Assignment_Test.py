import unittest
import Lesson_03_Assignment as z


class Factorial(unittest.TestCase):

    def test_fac(self):
        self.f0 = z.fac(0)
        self.f1 = z.fac(1)
        self.f2 = z.fac(2)
        self.f3 = z.fac(3)
        self.f4 = z.fac(4)
        self.f5 = z.fac(5)
        self.f6 = z.fac(6)
        self.f7 = z.fac(7)

        self.assertEqual(self.f0, 1)
        self.assertEqual(self.f1, 1)
        self.assertEqual(self.f2, 2)
        self.assertEqual(self.f3, 6)
        self.assertEqual(self.f4, 24)
        self.assertEqual(self.f5, 120)
        self.assertEqual(self.f6, 720)
        self.assertEqual(self.f7, 5040)

    def test_fac_recursive(self):
        self.fr0 = z.fac_recursive(0)
        self.fr1 = z.fac_recursive(1)
        self.fr2 = z.fac_recursive(2)
        self.fr3 = z.fac_recursive(3)
        self.fr4 = z.fac_recursive(4)
        self.fr5 = z.fac_recursive(5)
        self.fr6 = z.fac_recursive(6)
        self.fr7 = z.fac_recursive(7)

        self.assertEqual(self.fr0, 1)
        self.assertEqual(self.fr1, 1)
        self.assertEqual(self.fr2, 2)
        self.assertEqual(self.fr3, 6)
        self.assertEqual(self.fr4, 24)
        self.assertEqual(self.fr5, 120)
        self.assertEqual(self.fr6, 720)
        self.assertEqual(self.fr7, 5040)


if __name__ == '__main__':
    unittest.main()

