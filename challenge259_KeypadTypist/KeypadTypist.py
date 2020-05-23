import math

# Daily Programmer Challenge 259 (3/21/16): Clarence the Slow Typist
# https://www.reddit.com/r/dailyprogrammer/comments/4bc3el/20160321_challenge_259_easy_clarence_the_slow/

# Clarence is a data entry clerk who works at an internet service provider.
# His job is to manually enter the IP addresses of all of the ISP's customers into the database.
# He does this using a keypad which has the following layout:
#   1	2	3
#   4	5	6
#   7	8	9
#   .	0
# The distance between the centre of horizontally or vertically adjacent keys is exactly one centimetre.
# For instance, the distance between the centres of 3 and 9 would be two centimetres.
# The distance between the centres of 3 and 5 would be sqrt 2cm.
# The Pythagoras theorem is sufficient to calculate the distance between any two keys.
# Clarence, as you might expect from one who works in an ISP, uses a very slow and inefficient system of typing.
# He uses a single finger and searches for the key, and then moves his finger to the key, then presses it, and
# repeats for all of the digits in the seed. You might know of this style as the "eagle search system" since the
# finger searches above the keyboard for the correct key before plunging down for the keypress, like an eagle plunging
# down for a kill. For example, here is how Clarence would type out the seed 7851:
# He starts his finger at 7 and pushes the key.
# He moves his finger to the right 1cm to 8 and pushes the key.
# He moves his finger upwards 1cm to 5 and pushes the key.
# He moves his finger diagonally upwards and left sqrt 2cm to 1 and pushes the key.
# Therefore the total distance that Clarence moved his finger to type in 7851 is 1 + 1 + sqrt 2 which is about 3.41cm.
# Your task is to write a program that calculates the distance Clarence must move his finger to type in arbitrary IP addresses.

# Input is a string that will be in the form
# ().().().()
# where each () is an integer in the range 0 - 999. This represents the IP address that Clarence must type in. An example input might be:
# 219.45.143.143
# I would also like to point out that inputs such as 0.42.42.42 or 999.999.999.999 are still valid inputs,
# despite the fact that they are invalid IP addresses. So you don't need to include any IP address verification code in your program.

# Output the distance that Clarence must move his finger in order to type in the specified IP address.
# Round answers to two decimal places where needed, and use the cm unit in your output.
# The output for the example input is 27.38cm (1 + sqrt 8 + sqrt 5 + 2 + 1 + sqrt 5 + 3 + 1 + sqrt 5 + sqrt 13 + 3 + 1 + sqrt 5).

def KeypadTypist():
    def __init__(self):
        return

    def EnterIpAddress(self, ipaddress):
        return False

    def IsMoveDiagonal(self, moveDirection):
        return False

    def GetMoveDirection(self, firstKey, secondKey):

        # if the keys are in the same column...
        if firstKey % 3 == secondKey % 3:
            return 'vertical'

    def GetMoveDistance(self, firstKey, secondKey):

        # if the keys are in the same column...
        if firstKey % 3 == secondKey % 3:
            return firstKey/secondKey if firstKey > secondKey else secondKey/firstKey


@staticmethod
def Keypad():

    def __init__(self):
        self.format = '123456789.0'


# there is a real ipaddress library: https://docs.python.org/3/library/ipaddress.html
# but we will only be implementing a mock one in order to keep things simple.
def IpAddress():
    def __init__(self, maybeAnIpAddress):
        self.ipaddress

        if not type(str, maybeAnIpAddress):
            raise InvalidIpAddressException('Cannot instantiate an IP address object without a string')

        first = 0
        second = 0
        third = 0
        fourth = 0

        # we need each component to be an integer
        if not type(int, first) or not type(int, second) or not type(int, third) or not type(int, fourth):
            raise InvalidIpAddressException('The component is not an integer')

        # we need each component to be in the range [0, 999]
        if first < 0 or first > 999 or second < 0 or second > 999 or third < 0 or third > 999 or fourth < 0 or fourth > 999
            raise InvalidIpAddressException('The component is outside of the valid range of [0, 999]')

        # it's valid!
        self.ipaddress = maybeAnIpAddress

    def Next(self):
        return False

def InvalidIpAddressException(Exception):
    pass