import numpy as np
from typing import List
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_np = np.array(list(alphabet))


def tokenize_word(word:str) -> np.ndarray:
    return np.array([alphabet.index(l) for l in word]).astype(int)


def ints_to_word(indices: List[int]) -> str:
    return "".join(alphabet_np[indices])


def prediction_to_word(prediction:np.ndarray) -> str:
    return ints_to_word(np.argmax(prediction, axis=1))


