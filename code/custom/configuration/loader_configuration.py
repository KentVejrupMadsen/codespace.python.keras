batch_size = 32
image_width = 256,
image_height = 256

preserve_aspect = True

validation_split = 0.45
epochs = 10


def get_batch_size() -> int:
    global batch_size
    return batch_size


def get_validation_split() -> int:
    global validation_split
    return validation_split


def get_preserve_aspect() -> bool:
    global preserve_aspect
    return preserve_aspect


def get_image_width() -> int:
    global image_width
    return image_width


def get_image_height() -> int:
    global image_height
    return image_height


def get_epochs() -> int:
    global epochs
    return epochs
