import datetime

from tensorflow.python.keras.callbacks \
    import TensorBoard


def add_tensorboard_callback(
        callbacks: list
):
    directory = "logs/fit/" + str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
    callbacks.append(TensorBoard(log_dir=directory, histogram_freq=1))

