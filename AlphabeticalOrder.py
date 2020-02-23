# Daily Programmer Challenge 228 (8/17/15): Letters in Alphabetical Order
# https://www.reddit.com/r/dailyprogrammer/comments/3h9pde/20150817_challenge_228_easy_letters_in/

def IsAlphabeticalOrder(word):
    """
    >>> IsAlphabeticalOrder('billowy')
    billowy is in alphabetical order.
    >>> IsAlphabeticalOrder('biopsy')
    biopsy is in alphabetical order.
    >>> IsAlphabeticalOrder('chinos')
    chinos is in alphabetical order.
    >>> IsAlphabeticalOrder('defaced')
    defaced is NOT in alphabetical order.
    >>> IsAlphabeticalOrder('chintz')
    chintz is in alphabetical order.
    >>> IsAlphabeticalOrder('sponged')
    sponged is NOT in alphabetical order.
    >>> IsAlphabeticalOrder('bijoux')
    bijoux is in alphabetical order.
    >>> IsAlphabeticalOrder('abhors')
    abhors is in alphabetical order.
    >>> IsAlphabeticalOrder('fiddle')
    fiddle is NOT in alphabetical order.
    >>> IsAlphabeticalOrder('begins')
    begins is in alphabetical order.
    >>> IsAlphabeticalOrder('chimps')
    chimps is in alphabetical order.
    >>> IsAlphabeticalOrder('wronged')
    wronged is NOT in alphabetical order.
    """

    for charIndex in range(len(word) - 1):
        if word[charIndex] > word[charIndex+1]:
            print(word, "is NOT in alphabetical order.")
            return

    print(word, "is in alphabetical order.")
    return

def IsReverseAlphabeticalOrder(word):
    return True

