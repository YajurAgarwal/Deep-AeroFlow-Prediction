import tensorflow as tf
from tensorflow.keras import layers
from config import Config
from tensorflow.keras import regularizers
import numpy as np
from livelossplot import PlotLossesKerasTF
from Load_Dataset import load_train_test_data
from config import Config
X_train, y_train, X_test, y_test = load_train_test_data(
    Config.train_data, Config.test_data)
data_normalizer = tf.keras.layers.Normalization(axis=-1)
data_normalizer.adapt(np.array(X_train))


def build_model(input_shape, hidden_units, kernel_regularizer, learning_rate, loss_function):
    model = tf.keras.Sequential([
        data_normalizer,
        layers.Input(shape=input_shape),
    ])

    for units in hidden_units:
        model.add(layers.Dense(units, activation="relu",
                  kernel_regularizer=regularizers.l2(kernel_regularizer)))
        model.add(layers.BatchNormalization())
    model.add(layers.Dense(1))

    model.compile(loss=loss_function,
                  optimizer=tf.keras.optimizers.Adam(learning_rate))
    return model
