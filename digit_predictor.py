# Inspired by
# https://www.kaggle.com/poonaml/deep-neural-network-keras-way
import numpy as np
import pandas as pd

from subprocess import check_output

from sklearn.model_selection import train_test_split

from keras.utils.np_utils import to_categorical
from keras.preprocessing import image
from keras.models import Sequential
from keras.layers import Dense, Dropout, Lambda, Flatten
from keras.optimizers import Adam, RMSprop
from keras.models import Sequential
from keras.layers.core import Lambda, Dense, Flatten, Dropout
from keras.callbacks import EarlyStopping
from keras.layers import BatchNormalization, Convolution2D, MaxPooling2D
from keras.optimizers import RMSprop


class NeuralNetwork():
    def __init__(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

        seed = 2029
        np.random.seed(seed)

        # feature standardization
        mean_px = X_train.mean().astype(np.float32)
        std_px = X_train.std().astype(np.float32)

        def standardize(x):
            return (x - mean_px) / std_px

        # One-hot-encoding
        self.y_train = to_categorical(self.y_train)

        self.model = Sequential()
        self.model.add(Lambda(standardize, input_shape=(28, 28, 1)))
        self.model.add(Flatten())
        self.model.add(Dense(10, activation="softmax"))
        self.model.compile(optimizer=RMSprop(lr=0.001),
                           loss="categorical_crossentropy",
                           metrics=["accuracy"])

    def split_train_test(self):
        gen = image.ImageDataGenerator()
        self.X_train, self.X_val, self.y_train, self.y_val = \
            train_test_split(self.X_train, self.y_train, test_size=0.10, random_state=2011)
        batches = gen.flow(self.X_train, self.y_train, batch_size=64)
        val_batches = gen.flow(self.X_val, self.y_val, batch_size=64)

        return batches, val_batches

    def fit(self, batches, val_batches):
        history = self.model.fit_generator(batches, batches.n, nb_epoch=1,
                                           validation_data=val_batches,
                                           nb_val_samples=val_batches.n)

        self.model.optimizer.lr = 0.01
        gen = image.ImageDataGenerator()
        batches = gen.flow(self.X_train, self.y_train, batch_size=64)
        history = self.model.fit_generator(batches, batches.n, nb_epoch=1)

    def predict(self, x):
        X = np.array([x])
        return self.model.predict_classes(X, verbose=0)[0]


def train_nn():
    # import data
    train = pd.read_csv("db/train_sample5.csv")

    X_train = (train.ix[:, 2:].values).astype("float32")
    y_train = train.ix[:, 1].values.astype("int32")

    X_train = X_train.reshape(X_train.shape[0], 28, 28)
    X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)

    # model
    nn = NeuralNetwork(X_train, y_train)
    batches, val_batches = nn.split_train_test()
    nn.fit(batches, val_batches)
    return nn
