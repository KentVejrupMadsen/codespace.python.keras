from tensorflow.python.keras.callbacks \
    import ModelCheckpoint

from variables \
    import get_checkpoint_path


def make_checkpoint_callback() -> ModelCheckpoint:
    return ModelCheckpoint(
        filepath=get_checkpoint_path(),
        save_weights_only=True,
        verbose=1
    )


def call_callbacks() -> list:
    retVal = []

    retVal.append(
        make_checkpoint_callback()
    )

    return retVal

