import numpy as np

from wordle._wordle import check_guess

class Game(object):

    def __init__(self, word:str, turns=6, wordlength=5):
        self.state = -1 * np.ones((turns, wordlength))
        self.feedback = -1 * np.ones((turns, wordlength))
        self.word = word

    # def __next__(self, guess):
