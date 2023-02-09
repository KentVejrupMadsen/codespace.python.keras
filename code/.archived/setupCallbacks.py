from keras.callbacks \
    import TensorBoard

from tensorflow.python.keras.callbacks \
    import EarlyStopping

from tensorflow.python.keras.callbacks \
    import ModelCheckpoint

from custom.configuration \
    import \
    get_checkpoint_path, \
    get_log_path

from datetime \
    import datetime


def make_checkpoint_callback() -> ModelCheckpoint:
    return ModelCheckpoint(
        filepath=get_checkpoint_path(),
        save_weights_only=False,
        verbose=0,
        mode='max',
        save_best_only=True
    )


def make_early_stopper_callback() -> EarlyStopping:
    return EarlyStopping(
        monitor='val_loss',
        mode='min',
        verbose=0,
        patience=3
    )


# https://www.tensorflow.org/tensorboard/get_started
def make_tensorboard_callback():
    log_dir = get_log_path(
        str(datetime.now().strftime("%Y%m%d-%H%M%S"))
    )

    return TensorBoard(
        log_dir=log_dir,
        histogram_freq=2,
        write_images=True,
        write_steps_per_second=True
    )


def call_callbacks() -> list:
    ret_val = []

    ret_val.append(
        make_checkpoint_callback()
    )

    ret_val.append(
        make_early_stopper_callback()
    )

    ret_val.append(
        make_tensorboard_callback()
    )

    return ret_val

