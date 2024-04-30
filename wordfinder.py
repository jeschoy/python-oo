"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """To find and return random words in a dictionary.
    
    >>> words = WordFinder("words.txt")
    235886 words read
    
    >>> words.random() in ["disuse", "tung", "option"]
    True
    
    >>> words.random() in ["disuse", "tung", "option"]
    True
    """

    def __init__(self, path):
        """To read file and return the number of items within the file."""

        file = open(path)
        self.words = self.parse(file)
        print(f"{len(self.words)} words read")

    def parse(self, file):
        """To parse the file into a list of words."""

        return [w.strip() for w in file]

    def random(self):
        """To return a random word."""

        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):
    """Special Word Finder to exclude blank lines and comments.
    >>> words = WordFinder("words.txt")
    235886 words read
    
    >>> words.random() in ["disuse", "tung", "option"]
    True
    
    >>> words.random() in ["disuse", "tung", "option"]
    True
    """
    def parse(self, file):
        return [w.strip() for w in file if w.strip() and not w.startswith("#")]