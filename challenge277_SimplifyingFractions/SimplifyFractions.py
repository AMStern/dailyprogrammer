import math

# Daily Programmer Challenge 277 (7/25/16): Simplifying Fractions
# https://www.reddit.com/r/dailyprogrammer/comments/4uhqdb/20160725_challenge_277_easy_simplifying_fractions/

def Simplify(rationalList):
    reduced = ""
    
    # gather all of the numerators and denominators
    for term in rationalList:
        #rational = RationalNumber()
        print(term)
            
    return reduced

class RationalNumber:
    def __init__(self, expression):
        # ensure that the fraction is of a valid form
        # e.g., can't have "/13" or "235/" or "4/5/6"
        divOpPos = str(expression).find('/')
        if divOpPos > 0 and divOpPos != len(expression) and str(expression).count('/') == 1:
            self.numerator = int(expression.split('/')[0])
            self.denominator = int(expression.split('/')[1])
        else:
            raise MalformedExpression("Woops")

class MalformedExpression(Exception):
    def __init__(self, message):
        print(message)
