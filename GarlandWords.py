# Daily Programmer Challenge 223 (7/13/15): Garland Words
# https://www.reddit.com/r/dailyprogrammer/comments/3d4fwj/20150713_challenge_223_easy_garland_words/

# A _garland word_ is one that starts and ends with the same N letters in the same order, for some N greater than 0, but less than the length of the word.
# I'll call the maximum N for which this works the garland word's _degree_.
# For instance, "onion" is a garland word of degree 2, because its first 2 letters "on" are the same as its last 2 letters.
# The name "garland word" comes from the fact that you can make chains of the word in this manner:
#       onionionionionionionionionionion...
# Today's challenge is to write a function garland that, given a lowercase word, returns the degree of the word if it's a garland word, and 0 otherwise.

# Examples:
#       garland("programmer") -> 0
#       garland("ceramic") -> 1
#       garland("onion") -> 2
#       garland("alfalfa") -> 4

# Optional challenges:
# 1) Given a garland word, print out the chain using that word, as with "onion" above. You can make it as long or short as you like, even infinite.
# 2) Find the largest degree of any garland word in the enable1 English word list.
# 3) Find a word list for some other language, and see if you can find a language with a garland word with a higher degree.

def GarlandWords(word):
    degree = 0

    # e.g., list(range(len("onion") - 1)) = [0, 1, 2, 3]
    for index in list(range(len(word) - 1)):

        # append the word to itself, and then remove the last N letters of the first copy, e.g.:
        # index = 0 => appended = "onio" + "onion" = "onioonion"; degree remains 0
        # index = 1 => appended = "oni" + "onion" = "onionion"; degree becomes 2
        # index = 2 => appended = "on" + "onion" = "ononion"; degree remains 2
        # index = 3 => appended = "o" + "onion" = "oonion"; degree remains 2
        appended = word[0:len(word) - (index+1)] + word

        if appended.startswith(word, 0, len(word)):
            degree = index + 1

    return degree

