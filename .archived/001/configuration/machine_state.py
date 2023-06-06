optimizer = 'adam'
class_mode_type = 'sparse'
color_mode_type = 'rgb'

activation_type = 'softmax'
loss_func_type = 'sparse_categorical_crossentropy'

weight_set = 'imagenet'
include_weight_top = False

validation_split = 0.5

decay_steps = 2000
decay_rate = 0.4

normalise_value = 255.0
epoch = 10

batch_size = 3

image_width_size = 256
image_height_size = 256


def get_loss_function_type() -> str:
    global loss_func_type
    return loss_func_type


def get_include_weight_top() -> bool:
    global include_weight_top
    return include_weight_top


def get_weight_set() -> str:
    global weight_set
    return weight_set


def get_activation_type() -> str:
    global activation_type
    return activation_type


def get_color_mode_type():
    global color_mode_type
    return color_mode_type


def get_class_mode_type() -> str:
    global class_mode_type
    return class_mode_type


def set_optimizer_type(
        value: str
) -> None:
    global optimizer
    optimizer = value


def get_optimizer_type() -> str:
    global optimizer
    return optimizer


def get_batch_size_value() -> int:
    global batch_size
    return batch_size


def set_batch_size_value(
        value: int
) -> None:
    global batch_size
    batch_size = value


def get_normalise_value() -> float:
    global normalise_value
    return normalise_value


def set_normalise_value(
        value: float
) -> None:
    global normalise_value
    normalise_value = value


def get_default_width() -> int:
    global image_width_size
    return image_width_size


def set_default_width(
        value: int
) -> None:
    global image_width_size
    image_width_size = value


def get_default_height() -> int:
    global image_height_size
    return image_height_size


def set_default_height(
        value: int
) -> None:
    global image_height_size
    image_height_size = value


def get_epoch() -> int:
    global epoch
    return epoch


def set_epoch(
        value: int
) -> None:
    global epoch
    epoch = value


def get_default_image_size() -> tuple:
    return \
        get_default_width(), \
        get_default_height()


def get_validation_split() -> float:
    global validation_split
    return validation_split


def set_validation_split(
        value: float
) -> None:
    global validation_split
    validation_split = value


def get_decay_steps() -> int:
    global decay_steps
    return decay_steps


def set_decay_steps(
        value: int
) -> None:
    global decay_steps
    decay_steps = value


def get_decay_rate() -> float:
    global decay_rate
    return decay_rate


def set_decay_rate(
        value: float
) -> None:
    global decay_rate
    decay_rate = value


def get_optimizer() -> str:
    global optimizer
    return optimizer


def set_optimizer(
        value: str
) -> None:
    global optimizer
    optimizer = value

