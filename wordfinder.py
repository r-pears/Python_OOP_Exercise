"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """
    Returns a way to find random words from a dictionary.

    >>> wf = WordFinder("./three.txt")
    3 words read

    >>> wf.random()
    'dog'

    >>> wf.random()
    'axe'

    >>> wf.random()
    'snow'

    >>> wf.random()
    'dog'
    """
    def __init__(self, path):
        "Read dictionary and reports the number of read items"
        dictionary_file = open(path)
        self.words = self.parse(dictionary_file)
        print(f"{len(self.words)} words read")

    def parse(self, dictionary_file):
        "Parse dictionary_file into list of words"
        return [word.strip() for word in dictionary_file]

    def random(self):
        "Return a random word"
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """
    Specialized word finder that removes blank lines and comments

    >>> swf = SpecialWordFinder("special.txt")
    3 words read

    >>> swf.random() in ["apple", "mango", "kale"]
    True

    >>> swf.random() in ["apple", "mango", "kale"]
    True

    >>> swf.random() in ["apple", "mango", "kale"]
    True

    """
    def parse(self, dictionary_file):
        "Parse dictionary file into a list of words removing the blank spaces and comments"
        return [word.strip() for word in dictionary_file if word.strip() and not word.startswith("#")]
