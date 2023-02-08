from keras.applications \
    import VGG19

from keras.layers \
    import \
    Flatten, \
    Dense

from tensorflow.python.keras.models \
    import Model

from configuration.machine_state \
    import \
    get_default_width, \
    get_default_height


def create_model() -> Model:
    vgg = VGG19(
        input_shape=(
            get_default_width(),
            get_default_height(),
            3
        ),
        weights='imagenet',
        include_top=False,
        classifier_activation=''
    )

    for layer in vgg.layers:
        layer.trainable = False

    x = Flatten()(
        vgg.output
    )

    prediction = Dense(
        3,
        activation='softmax'
    )(x)

    model = Model(
        inputs=vgg.inputs,
        outputs=prediction
    )

    model.compile(
        loss= "sparse_categorical_crossentropy",
        optimizer= "adam",
        metrics= [
            "accuracy"
        ]
    )

    model.summary()

    return model
