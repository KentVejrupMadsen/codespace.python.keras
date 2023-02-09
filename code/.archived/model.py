from keras.applications \
    import VGG19

from keras.layers \
    import \
    Flatten, \
    Dense

from tensorflow.python.keras.models \
    import Model

from custom.configuration \
    import \
    get_default_width, \
    get_default_height, \
    get_activation_type, \
    get_weight_set, \
    get_include_weight_top, \
    get_optimizer_type, \
    get_loss_function_type


def create_model() -> Model:
    vgg = VGG19(
        input_shape=(
            get_default_width(),
            get_default_height(),
            3
        ),
        weights=get_weight_set(),
        include_top=get_include_weight_top(),
        classifier_activation=get_activation_type(),
        pooling='avg'
    )

    for layer in vgg.layers:
        layer.trainable = False

    x = Flatten()(
        vgg.output
    )

    prediction = Dense(
        4,
        activation='softmax'
    )(x)

    model = Model(
        inputs=vgg.inputs,
        outputs=prediction
    )

    model.compile(
        loss=get_loss_function_type(),
        optimizer=get_optimizer_type(),

        metrics=[
            "accuracy"
        ],

    )

    model.summary()

    return model
