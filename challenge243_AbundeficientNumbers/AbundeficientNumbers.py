import math

# Daily Programmer Challenge 243 (11/30/15): Abundant and Deficient Numbers
# https://www.reddit.com/r/dailyprogrammer/comments/3uuhdk/20151130_challenge_243_easy_abundant_and/

# In number theory, a deficient number is a number n for which the sum of divisors sigma(n) < 2n, or,
# equivalently, the sum of proper divisors (or aliquot sum) s(n) < n. The value 2n - sigma(n) (or n - s(n)) is called
# the number's deficiency. In contrast, an abundant number is a number for which the sum of its
# proper divisors is greater than the number itself. As an example, consider the number 21. Its divisors are 1, 3, 7
# and 21, and their sum is 32. Because 32 is less than 2 x 21, the number 21 is deficient. Its deficiency
# is 2 x 21 - 32 = 10. The integer 12 is the first abundant number. Its divisors are 1, 2, 3, 4, 6, and 12, and their
# sum is 28. Because 28 is greater than 2 x 12, the seed 12 is abundant. It's abundant by is 28 - 24 = 4.

# Examples:
#       get_result(220) -> 64
#       get_result(112) -> 24
#       get_result(12) -> 4
#       get_result(111) -> 0
#       get_result(69) -> -42
#       get_result(85) -> -62
#       get_result(134) -> -64

# NOTE: Author of this challenge had a mistaken initial spec, from reddit link at the top:
# "I had fouled up my implementation, 9 and 111 are deficient, not perfect.
# See http://sites.my.xs.edu.ph/connor-teh-14/aste/mathematics-asteroids/perfect-abundant-and-deficient-numbers-1-100."

class AbundeficientCalculator():

    @staticmethod
    def is_deficient(seed):
        return AbundeficientCalculator.get_result(seed) < 0

    @staticmethod
    def is_neither(seed):
        return AbundeficientCalculator.get_result(seed) == 0

    @staticmethod
    def is_abundant(seed):
        return AbundeficientCalculator.get_result(seed) > 0

    @staticmethod
    def get_result(seed):
        proper_divisors = AbundeficientCalculator.get_proper_divisors(seed)
        proper_divisor_sum = AbundeficientCalculator.sum_proper_divisors(proper_divisors)
        return proper_divisor_sum - seed

    # This makes use of the 'Direct Search Factorization' algorithm, see here:
    # http://mathworld.wolfram.com/DirectSearchFactorization.html
    @staticmethod
    def get_proper_divisors(seed):
        proper_divisors = []

        for natural_number in range(1, seed):

            # no values beyond floor(sqrt(seed)) are valid
            if natural_number > math.floor(math.sqrt(seed)):
                break

            if seed % natural_number == 0:
                proper_divisors.append(natural_number)

                # calculate the value and ensure we're not adding a duplicate
                result = (int)(seed / natural_number)
                if result != natural_number and result != seed:
                    proper_divisors.append(result)

        return proper_divisors

    @staticmethod
    def sum_proper_divisors(proper_divisors):
        sum_of_proper_divisors = 0
        for next_divisor in proper_divisors:
            sum_of_proper_divisors += next_divisor
        return sum_of_proper_divisors
