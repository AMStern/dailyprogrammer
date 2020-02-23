import math

# Daily Programmer Challenge 243 (11/30/15): Abundant and Deficient Numbers
# https://www.reddit.com/r/dailyprogrammer/comments/3uuhdk/20151130_challenge_243_easy_abundant_and/

# In number theory, a deficient number is a number n for which the sum of divisors sigma(n) < 2n, or,
# equivalently, the sum of proper divisors (or aliquot sum) s(n) < n. The value 2n - sigma(n) (or n - s(n)) is called
# the number's deficiency. In contrast, an abundant number is a number for which the sum of its
# proper divisors is greater than the number itself. As an example, consider the number 21. Its divisors are 1, 3, 7
# and 21, and their sum is 32. Because 32 is less than 2 x 21, the number 21 is deficient. Its deficiency
# is 2 x 21 - 32 = 10. The integer 12 is the first abundant number. Its divisors are 1, 2, 3, 4, 6, and 12, and their
# sum is 28. Because 28 is greater than 2 x 12, the number 12 is abundant. It's abundant by is 28 - 24 = 4.

# Examples:
#       get_result(220) -> 64
#       get_result(112) -> 24
#       get_result(12) -> 4
#       get_result(111) -> 0
#       get_result(69) -> -42
#       get_result(85) -> -62
#       get_result(134) -> -64

class AbundeficientCalculator():

    @staticmethod
    def is_deficient(number):
        return AbundeficientCalculator.get_result(number) < 0

    @staticmethod
    def is_neither(number):
        return AbundeficientCalculator.get_result(number) == 0

    @staticmethod
    def is_abundant(number):
        return AbundeficientCalculator.get_result(number) > 0

    @staticmethod
    def get_result(number):
        try:
            properDivisorsList = AbundeficientCalculator.get_proper_divisors(number)
        except NotImplementedError:
            return 0

        sumOfDivisorsList = AbundeficientCalculator.sum_proper_divisors(properDivisorsList)
        return sumOfDivisorsList - 2 * number

    # This makes use of the 'Direct Search Factorization' algorithm, see here:
    # http://mathworld.wolfram.com/DirectSearchFactorization.html
    @staticmethod
    def get_proper_divisors(number):
        properDivisors = []

        for naturalNumber in range(number + 1):

            if naturalNumber == 0:
                continue

            # base case
            if number == 1:
                properDivisors.append(1)
                break

            # no values beyond floor(sqrt(number)) are valid
            if naturalNumber == math.floor(math.sqrt(number)):
                break

            if number % naturalNumber == 0:
                properDivisors.append([naturalNumber, number / naturalNumber])
                #properDivisors.append(AbundeficientCalculator.get_proper_divisors(naturalNumber))
                print(properDivisors)


        if len(properDivisors) == 0:
            raise NotImplementedError("Not able to calculate the list of proper divisors for: ", number)

        return properDivisors

    @staticmethod
    def sum_proper_divisors(properDivisorList):
        sumOfProperDivisors = 0
        for nextDivisor in properDivisorList:
            sumOfProperDivisors += nextDivisor[0]
        return sumOfProperDivisors

    @staticmethod
    def get_type(number):
        if AbundeficientCalculator.is_abundant(number):
            return "ABUNDANT"
        elif AbundeficientCalculator.is_deficient(number):
            return "DEFICIENT"
        elif AbundeficientCalculator.is_neither(number):
            return "NEITHER"
        else:
            return "UNKNOWN"

