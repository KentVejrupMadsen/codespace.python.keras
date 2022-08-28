from extra \
    import Extra

from keras import Model

import tensorflow \
    as tf

from tensorflow \
    import keras

import numpy \
    as np

from keras.models \
    import Sequential

from keras.layers \
    import *


#inputs = Input(shape=(32,))
#body = Dense(32)(inputs)

#model = Model(inputs, body)

#model.add(Dense(32))

#model.summary()


class Application:
    def __init__(self):
        self.title = 'ai'
        self.optional = Extra()

    def initialise(self):
        print(self.title)
        pass

    def execute(self):
        pass

    def gc(self):
        pass