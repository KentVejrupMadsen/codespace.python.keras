import wandb
from keras import Model

from wandb.keras \
    import WandbCallback

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

wandb.init(project="keras-codespace", entity="designermadsen")
wandb.config = \
{
    "learning_rate": 0.05,
    "epochs": 100,
    "batch_size": 126
}

inputs = Input(shape=(32,))
body = Dense(32)(inputs)

model = Model(inputs, body)

model.add(Dense(32))

model.summary()
