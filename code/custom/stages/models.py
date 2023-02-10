import keras

import numpy
from keras \
    import layers

from tensorflow.python.keras.callbacks import EarlyStopping, ModelCheckpoint


class CustomModel:
    def __init__(
            self,
            input_node: tuple,
            x: int = 25,
            y: int = 128,
            max_classes: int = 1000,
            image_width: int = 128,
            image_height: int = 128
    ):
        self.input = keras.Input(
            shape=input_node
        )

        self.output = None

        self.model = None

        self.image_width = image_width
        self.image_height = image_height

        self.predict = None

        self.setup(
            x,
            y,
            max_classes
        )

        self.callbacks = []

    def early_stopper_added(self):
        callbacks = self.callbacks
        early_stopping = EarlyStopping(
            monitor="loss",
            mode="min",
            verbose=1,
            patience=5
        )

        callbacks.append(
            early_stopping
        )

    def checkpoint_added(self):
        callbacks = self.callbacks

        checkpoint_callback = ModelCheckpoint(
            filepath='/tmp/checkpoint/',
            save_weights_only=False,
            save_best_only=True,
            mode='max',
            monitor='accuracy',
            verbose=0,
            save_freq=4,
            steps_per_execution=50
        )

        callbacks.append(
            checkpoint_callback
        )

    def setup(
            self,
            x: int,
            y: int,
            max_classes: int
    ):
        start_layer = y / 2

        first_layer_in_mid = layers.Conv2D(
            start_layer,
            (3, 3),
            activation='relu',
            input_shape=(
                self.image_width,
                self.image_height,
                3
            )
        )

        mid_layers = first_layer_in_mid(
            self.input
        )

        mid_layers = layers.Conv2D(
            y,
            (3, 3),
            activation='relu',
            input_shape=(32, 32, 3)
        )(mid_layers)

        mid_layers = layers.MaxPooling2D(
            (2, 2)
        )(mid_layers)

        end_pos = x - 2

        for idx in range(0, end_pos):
            mid_layers = layers.Conv2D(
                y,
                (3, 3),
                activation='relu'
            )(mid_layers)

        mid_layers = layers.MaxPooling2D(
            (2, 2)
        )(mid_layers)

        self.output = layers.Conv2D(
            y,
            (3, 3),
            activation='relu'
        )(mid_layers)

        x = layers.Flatten()(self.output)
        prediction = layers.Dense(
            max_classes,
            activation='softmax'
        )(x)
        self.output = prediction

        self.model = keras.Model(
            inputs=self.input,
            outputs=self.output,
            name='model'
        )

        self.model.compile(
            loss='SparseCategoricalCrossentropy',
            optimizer='adam',
            metrics=[
                "accuracy"
            ]
        )

        self.model.summary()

    def debug(self):
        print(self.input.shape)

    def get_model(self) -> keras.Model:
        return self.model

    def get_callbacks(self) -> list:
        return self.callbacks

    def set_image_size(
            self,
            width: int,
            height: int
    ):
        self.image_width = width
        self.image_height = height
