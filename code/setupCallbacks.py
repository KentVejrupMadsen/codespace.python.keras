from tensorflow.python.keras.callbacks \
    import EarlyStopping

from tensorflow.python.keras.callbacks \
    import ModelCheckpoint

from configuration.variables \
    import get_checkpoint_path


def make_checkpoint_callback() -> ModelCheckpoint:
    return ModelCheckpoint(
        filepath=get_checkpoint_path(),
        save_weights_only=True,
        verbose=1
    )


def make_early_stopper_callback() -> EarlyStopping:
    return EarlyStopping(
        monitor='val_loss',
        mode='min',
        verbose=1,
        patience=2
    )


def call_callbacks() -> list:
    ret_val = []

    ret_val.append(
        make_checkpoint_callback()
    )

    ret_val.append(
        make_early_stopper_callback()
    )

    return ret_val

