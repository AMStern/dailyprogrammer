import unittest
from challenge259_KeypadTypist.KeypadTypist import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.HomeAddress = '128.0.0.1'
        self.OutsideUpperBound = '1000.0.0.0'
        self.BelowLowerBound = '-1.0.0.0'

    def test_InvalidIpAddressRaisesException(self):
        with self.assertRaises(InvalidIpAddressException):
            ipaddress = IpAddress(self.HomeAddress)


if __name__ == '__main__':
    unittest.main()
