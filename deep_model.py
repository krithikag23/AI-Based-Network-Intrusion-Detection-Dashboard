import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense

def train_autoencoder(data):
    input_dim = data.shape[1]

    input_layer = Input(shape=(input_dim,))
    encoder = Dense(8, activation="relu")(input_layer)
    bottleneck = Dense(4, activation="relu")(encoder)
    decoder = Dense(8, activation="relu")(bottleneck)
    output_layer = Dense(input_dim, activation="linear")(decoder)

    autoencoder = Model(inputs=input_layer, outputs=output_layer)
    autoencoder.compile(optimizer="adam", loss="mse")

    autoencoder.fit(data, data, epochs=20, batch_size=2, verbose=0)

    return autoencoder


def detect_anomaly(model, sample, threshold=0.01):
    reconstructed = model.predict(sample)
    error = np.mean(np.square(sample - reconstructed))

    return error > threshold, error
