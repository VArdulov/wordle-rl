import numpy as np

from tensorflow.keras.layers import Input, Dense, LSTM, Dropout, Flatten, RepeatVector, TimeDistributed, concatenate
from tensorflow.keras.models import Model

from _utils import alphabet_np
from _environment import Game


def create_recurrent_model(turns: int=6, wordlength:int =5) -> Model:
    guess_input = Input((turns, wordlength))
    feedback_input = Input((turns, wordlength))

    embedding_1 = Dense(256)(concatenate([guess_input, feedback_input]))
    embedding_2 = Dense(128)(Dropout(0.2)(embedding_1))
    embedding_3 = Flatten()(Dense(16)(Dropout(0.2)(embedding_2)))

    repeat_vector = RepeatVector(wordlength)(embedding_3)
    recurrent = LSTM(16, return_sequences=True, dropout=0.2)(repeat_vector)
    character_q_values = TimeDistributed(Dense(alphabet_np.shape[0], activation="relu"))(recurrent)

    model = Model(inputs=[guess_input, feedback_input], outputs=character_q_values)

    model.compile(loss="mse", optimizer="rmsprop")
    return model


def deterministic_model_prediction(model: Model, game: Game) -> np.ndarray:
    inputs = [np.expand_dims(game.state, 0), np.expand_dims(game.feedback, 0)]
    prediction = np.argmax(model(inputs).numpy().squeeze(), axis=1)
    print(prediction.shape)
    return prediction


def probabilistic_model_prediction(model: Model, game: Game) -> np.ndarray:
    inputs = [np.expand_dims(game.state, 0), np.expand_dims(game.feedback, 0)]
    prediction = model(inputs).numpy().squeeze()
    print(prediction.shape)
    prediction = [
        np.random.choice(
            np.arange(0, alphabet_np.shape[0]),
            replace=True,
            p=row/sum(row)
        )
        for row in prediction
    ]
    return np.array(prediction)

if __name__ == "__main__":
    model = create_recurrent_model()

    from _environment import Game
    game = Game("hello")

    d_pred = deterministic_model_prediction(model=model, game=game)
    p_pred = probabilistic_model_prediction(model=model, game=game)

    print(d_pred)
    print(p_pred)

    from _utils import prediction_to_word
    inputs = [np.expand_dims(game.state, 0), np.expand_dims(game.feedback, 0)]
    prediction = model(inputs).numpy().squeeze()
    d_word = prediction_to_word(prediction)

    p_word = "".join(alphabet_np[p_pred])#prediction_to_word(p_pred)

    print(d_word)
    print(p_word)

    from wordle._wordle import check_guess
    print(check_guess(d_word, game.word))
    print(check_guess(p_word, game.word))

