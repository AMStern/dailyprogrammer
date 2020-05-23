# Daily Programmer Challenge 228 (8/17/15): Letters in Alphabetical Order
# https://www.reddit.com/r/dailyprogrammer/comments/3h9pde/20150817_challenge_228_easy_letters_in/

class AlphabeticalOrderizer():
    @staticmethod
    def IsAlphabeticalOrder(word):
        for charIndex in range(len(word) - 1):
            if word[charIndex] > word[charIndex+1]:
                return False

        return True

    @staticmethod
    def IsReverseAlphabeticalOrder(word):
        return AlphabeticalOrderizer.IsAlphabeticalOrder(word[::-1])

