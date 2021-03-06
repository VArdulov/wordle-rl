from numpy import load, random
from wordle import take_turn
from argparse import ArgumentParser

args = ArgumentParser()
args.add_argument("--turns", "-t", default=6, type=int, help="maximum number of turns before game is considered a loss")

if __name__ == "__main__":
    parsed_args = args.parse_args()
    max_turns = int(parsed_args.turns)
    turn = 0

    words = load("words.npy")
    game = random.choice(words).astype(str)
    game_over = False
    solved = False
    while not game_over:
        print(f"You have {max_turns - turn} guesses remaining")
        turn += 1
        solved = take_turn(game)
        game_over = solved or (turn >= max_turns)

    if solved:
        print(f"Good job! it took you {turn} turns to guess the correct word")
    else:
        print(f"The word was {game}, better luck next time...")

