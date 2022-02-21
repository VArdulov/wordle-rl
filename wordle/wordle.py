import numpy as np

def check_guess(guess: str, game: str, verbose=False) -> np.ndarray:
    game_dict = {l:[] for l in game}

    for i, l in enumerate(game):
        game_dict[l].append(i)

    guess_dict = {l:[] for l in guess}

    for i, l in enumerate(guess):
        guess_dict[l].append(i)

    solution_check = np.array([-1 for _ in range(len(game))])

    for guess_letter in guess_dict:

        positions_to_remove = []
        for guess_position in guess_dict[guess_letter]:
            if (guess_letter in game_dict) and (guess_position in game_dict.get(guess_letter, [])):
                positions_to_remove.append(guess_position)
                solution_check[guess_position] = 1

        guess_dict[guess_letter] = [p for p in guess_dict[guess_letter] if p not in positions_to_remove]
        game_dict[guess_letter] = [p for p in game_dict.get(guess_letter, [])  if p not in positions_to_remove]

        if (len(guess_dict[guess_letter]) > 0):
            for guess_position in guess_dict[guess_letter]:
                if len(game_dict.get(guess_letter, [])) > 0:
                    solution_check[guess_position] = 0
                    game_dict[guess_letter].pop(0)

    return solution_check