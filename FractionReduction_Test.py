import unittest
from FractionReduction import RationalNumber, Simplify, MalformedExpression

class FractionReduction_Test(unittest.TestCase):

    def test_SumsToInteger(self):
        first = RationalNumber("1/2")
        second = RationalNumber("1/2")
        self.assertEqual("1", Simplify([first, second]))

    #def test_SumsToReducedRational(self):
    #    self.assertEqual("2/3", Simplify([1/3, 1/3]))

    #def test_SumsToUnreducedRational(self):
    #    self.assertEqual("3/2", Simplify([3/4, 3/4]))
    #    self.assertEqual(7/15, Simplify([1/6, 3/10]))

    def test_IntegerIsValid(self):
        pass

    def test_MissingNumeratorIsInvalid(self):
        self.assertRaises(MalformedExpression, RationalNumber("/2"))
            

    def test_MissingDenumeratorIsInvalid(self):
        pass

    def test_ComplexFractionIsInvalid(self):
        pass

if __name__ == '__main__':
    unittest.main()
