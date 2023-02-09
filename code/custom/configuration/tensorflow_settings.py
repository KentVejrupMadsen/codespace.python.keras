import tensorflow

AUTOTUNE = tensorflow.data.AUTOTUNE


def get_autotune():
    global AUTOTUNE
    return AUTOTUNE
