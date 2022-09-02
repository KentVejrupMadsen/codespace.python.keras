import tensorflow \
    as tf


import PIL
import numpy as np


import secrets

from tensorflow \
    import keras

from tensorflow.keras \
    import layers

from tensorflow.keras.models \
    import Sequential

from properties \
    import KerasProperties

AUTOTUNE = tf.data.AUTOTUNE


class KerasDataset:
    def __init__(self):
        self.path = "/home/madsen/codespace/frameworks/keras/dataset/train"
        self.properties = KerasProperties()
        self.subset = 'training'
        self.seed = 1

        self.dataset = None
        self.validation = None

        self.model = None

        self.epoch = 10
        self.last_history = None

    def setup_dataset(self):
        global AUTOTUNE

        train_dataset=tf.keras.utils.image_dataset_from_directory(
            self.path,
            validation_split=self.properties.get_validation_size(),
            subset="training",
            seed=self.properties.get_seed(),
            image_size=(self.properties.get_height(), self.properties.get_width()), batch_size=self.properties.get_batch_size()
        )
        train_dataset.cache().shuffle(10).prefetch(buffer_size=AUTOTUNE)

        validation_dataset = tf.keras.utils.image_dataset_from_directory(
            self.path,
            validation_split=self.properties.get_validation_size(),
            subset="training",
            seed=self.properties.get_seed(),
            image_size=(self.properties.get_height(), self.properties.get_width()),
            batch_size=self.properties.get_batch_size()
        )
        validation_dataset.cache().prefetch(buffer_size=AUTOTUNE)

        self.dataset = train_dataset
        self.validation = validation_dataset

    def setup_model(self):
        classesS = len(self.dataset.class_names)

        self.model = Sequential(
            [
                layers.Rescaling(1. / 255, input_shape=(self.properties.get_height(), self.properties.get_width(), 3)),

                layers.Conv2D(32, 3, padding='same', activation='relu'),
                layers.MaxPooling2D(),

                layers.Conv2D(32, 3, padding='same', activation='relu'),
                layers.MaxPooling2D(),

                layers.Conv2D(32, 3, padding='same', activation='relu'),
                layers.MaxPooling2D(),

                layers.Conv2D(32, 3, padding='same', activation='relu'),
                layers.MaxPooling2D(),

                layers.Conv2D(32, 3, padding='same', activation='relu'),
                layers.MaxPooling2D(),

                layers.Flatten(),
                layers.Dense(256, activation='relu'),
                layers.Dense(classesS)
            ]
        )

        self.model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])
        self.model.build()

    def get_dataset(self):
        return self.dataset

    def set_dataset(self, dataset):
        self.dataset = dataset

    def train(self):
        history = self.model.fit(
            self.dataset,
            validation_data=self.validation,
            epochs=self.epoch
        )

        self.last_history = history
        return self.last_history

    def classify(self, url):
        path = tf.keras.utils.get_file('classify', origin=url)
        img = tf.keras.utils.load_img(path, target_size=(self.properties.get_height(), self.properties.get_width()))

        img_batch = tf.keras.utils.img_to_array(img)
        img_batch = tf.expand_dims(img_batch, 0)

        predictions = self.model.predict(img_batch)
        score = tf.nn.softmax(predictions[0])

        _class_ = self.dataset.class_names[np.argmax(score)]

        print("this image belongs to: {} with {:.2f} percent confidence".format(_class_, 100 * np.max(score)))

