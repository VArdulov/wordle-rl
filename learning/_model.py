from tensorflow.keras.layers import Input, Dense, LSTM, Dropout, Flatten, RepeatVector, TimeDistributed
from tensorflow.keras.model import Model

from ._utils import alphabet_np

def create_recurrent_model(turns=6, wordlength=5):
    guess_input = Input((turns, wordlength))
    feedback_input = Input((turns, wordlength))

    embedding_1 = Dense(256)([guess_input, feedback_input])
    embedding_2 = Dense(128)(Dropout(p=0.2)(embedding_1))
    embedding_3 = Flatten()(Dense(16)(Dropout(p=0.2)(embedding_2)))

    repeat_vector = RepeatVector(wordlength)(embedding_3)
    recurrent = LSTM(16, return_sequences=True, dropout=0.2)(repeat_vector)
    character_q_values = TimeDistributed(Dense(alphabet_np.shape[0], activation="relu"))(recurrent)

    model = Model(inputs=[guess_input, feedback_input], output=character_q_values)

    model.compile(loss="mse", optimizer="rmsprop")
    return model



