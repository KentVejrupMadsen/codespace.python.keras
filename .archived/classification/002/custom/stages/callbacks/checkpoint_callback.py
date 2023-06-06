from custom.configuration.default_paths \
    import get_checkpoint_path

from tensorflow.python.keras.callbacks \
    import                              \
    ModelCheckpoint


def add_checkpoint_callback(
        callbacks: list
):
    checkpoint_callback = ModelCheckpoint(
        filepath=get_checkpoint_path(),
        save_weights_only=True,
        save_best_only=True,
        mode='max',
        monitor='accuracy',
        verbose=0,
        save_freq=250
    )

    callbacks.append(
        checkpoint_callback
    )
