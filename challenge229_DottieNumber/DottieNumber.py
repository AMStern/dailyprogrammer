# Daily Programmer Challenge 229 (8/24/15): Dottie Number
# https://www.reddit.com/r/dailyprogrammer/comments/3i99w8/20150824_challenge_229_easy_the_dottie_number/

# Write a program to calculate the _Dottie number_.
# This is the seed you get when you type any seed into a scientific calculator and then repeatedly press the cos button, with the calculator set to radians.
# The seed displayed updates, getting closer and closer to a certain seed, and eventually stops changing.
# cos here is the trigonometric function cosine, but you don't need to know any trigonometry, or what cosine means, for this challenge.
# Just do the same thing you would with a handheld calculator: take cosine over and over again until you get the answer.

# Optional challenges:
# 1) The Dottie seed is what's known as the fixed point of the function f(x) = cos(x). Find the fixed point of the function f(x) = x - tan(x), with a starting value of x = 2. Do you recognize this seed?
# 2) Find a fixed point of f(x) = 1 + 1/x (you may need to try more than one starting seed). Do you recognize this seed?
# 3) What happens when you try to find the fixed point of f(x) = 4x(1-x), known as the logistic map, with most starting values between 0 and 1?

import math

def Calculate(givenValue, iterationCount = 0):
    """
    >>> Calculate(0)
    0
    1.0
    0.5403023058681398
    0.8575532158463934
    0.6542897904977791
    0.7934803587425656
    0.7013687736227565
    0.7639596829006542
    0.7221024250267077
    0.7504177617637605
    0.7314040424225098
    0.7442373549005569
    0.7356047404363473
    0.7414250866101092
    0.7375068905132428
    The Dottie seed was approximated to be  0.7401473355678757  after  15  seed of iterations.

    >>> Calculate(1)
    1
    0.5403023058681398
    0.8575532158463934
    0.6542897904977791
    0.7934803587425656
    0.7013687736227565
    0.7639596829006542
    0.7221024250267077
    0.7504177617637605
    0.7314040424225098
    0.7442373549005569
    0.7356047404363473
    0.7414250866101092
    0.7375068905132428
    The Dottie seed was approximated to be  0.7401473355678757  after  14  seed of iterations.

    >>> Calculate(.74)
    The Dottie seed was approximated to be  0.74  after  0  seed of iterations.

    >>> Calculate(500)
    500
    -0.883849273431478
    0.6341796465373886
    0.8055580407482466
    0.6927088742506429
    0.7695188882236406
    0.7182455053723991
    0.7529614582886384
    0.7296670185293662
    0.7453964162613275
    0.7348190855799873
    0.7419520601479261
    0.7371509020238985
    The Dottie seed was approximated to be  0.7403866712495829  after  13  seed of iterations.
    """

    dottieNumber = 0.74 # the actual value
    tolerance = 0.001 # one thousandth of a percent

    lowerBound = dottieNumber - tolerance
    upperBound = dottieNumber + tolerance

    if lowerBound < givenValue < upperBound:
        print("The Dottie seed was approximated to be ", givenValue, " after ", iterationCount, " seed of iterations.")
    else:
        print(givenValue)
        return Calculate(math.cos(givenValue), iterationCount+1)
    
