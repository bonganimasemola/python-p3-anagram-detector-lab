
class Anagram:
    def __init__(self, word):
        """
        Initializes the Anagram object with the given word.
        :param word: str, the word to be checked for anagrams.
        """
        self.word = word
        self.letters = {}
        for letter in word:
            if letter in self.letters:
                self.letters[letter] += 1
            else:
                self.letters[letter] = 1

    def match(self, words):
        """
        Checks the given list of words for anagrams of the initial word.
        :param words: list of str, the list of words to be checked.
        :return: list of str, the list of words that are anagrams of the initial word.
        """
        matched_words = []
        for word in words:
            if self.letters == {letter: word.count(letter) for letter in self.letters}:
                matched_words.append(word)
        return matched_words
#
#This code defines a class `Anagram` that can be used to find anagrams of a given word. The class has two methods:
#
#1. `__init__(self, word)`: This method initializes the `Anagram` object with the given word. It also creates a dictionary `self.letters` that maps each letter in the word to its frequency.
#
#2. `match(self, words)`: This method checks the given list of words for anagrams of the initial word. It does this by comparing the frequency of each letter in the initial word with the frequency of each letter in each word in the list. If the frequencies match for all letters, the word