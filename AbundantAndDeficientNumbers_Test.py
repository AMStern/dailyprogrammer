import unittest
from AbundeficientNumbers import AbundeficientCalculator

class AbundeficientNumbers_Test(unittest.TestCase):
    def test_IsAbundant(self):
        self.assertTrue(AbundeficientCalculator.is_abundant(220))
        self.assertTrue(AbundeficientCalculator.is_abundant(112))
        self.assertTrue(AbundeficientCalculator.is_abundant(12))

    def test_IsDeficient(self):
        self.assertTrue(AbundeficientCalculator.is_deficient(69))
        self.assertTrue(AbundeficientCalculator.is_deficient(85))
        self.assertTrue(AbundeficientCalculator.is_deficient(134))

    def test_IsNeither(self):
        self.assertTrue(AbundeficientCalculator.is_neither(111))

    def test_abundeficientType(self):
        # test ABUNDANT
        self.assertEqual(AbundeficientCalculator.get_type(220), "ABUNDANT")
        self.assertEqual(AbundeficientCalculator.get_type(112), "ABUNDANT")
        self.assertEqual(AbundeficientCalculator.get_type(12), "ABUNDANT")

        # test DEFICIENT
        self.assertEqual(AbundeficientCalculator.get_type(69), "DEFICIENT")
        self.assertEqual(AbundeficientCalculator.get_type(85), "DEFICIENT")
        self.assertEqual(AbundeficientCalculator.get_type(134), "DEFICIENT")

        # test NEITHER
        self.assertEqual(AbundeficientCalculator.get_type(111), "NEITHER")

    def test_abundeficientResult(self):
        # test ABUNDANT
        self.assertEqual(AbundeficientCalculator.get_result(220), 64)
        self.assertEqual(AbundeficientCalculator.get_result(112), 24)
        self.assertEqual(AbundeficientCalculator.get_result(12), 4)

        # test DEFICIENT
        self.assertEqual(AbundeficientCalculator.get_result(69), -42)
        self.assertEqual(AbundeficientCalculator.get_result(85), -62)
        self.assertEqual(AbundeficientCalculator.get_result(134), -64)

        # test NEITHER
        self.assertEqual(AbundeficientCalculator.get_result(111), 0)

        # test UNKNOWN
        self.assertEqual(AbundeficientCalculator.get_result(111), 0)

    def test_get_proper_divisors(self):
        self.assertEqual(AbundeficientCalculator.get_proper_divisors(1), [1])
        self.assertEqual(AbundeficientCalculator.get_proper_divisors(2), [1, 2]);
        self.assertEqual(AbundeficientCalculator.get_proper_divisors(3), [1, 3]);
        self.assertEqual(AbundeficientCalculator.get_proper_divisors(4), [1, 2, 4]);
        self.assertEqual(AbundeficientCalculator.get_proper_divisors(5), [1, 5]);
        self.assertEqual(AbundeficientCalculator.get_proper_divisors(6), [1, 2, 3, 6]);
        self.assertEqual(AbundeficientCalculator.get_proper_divisors(7), [1, 7]);
        self.assertEqual(AbundeficientCalculator.get_proper_divisors(8), [1, 2, 4, 8]);
        self.assertEqual(AbundeficientCalculator.get_proper_divisors(9), [1, 3, 9]);

if __name__ == '__main__':
    unittest.main()
