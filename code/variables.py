import random

from sys \
    import maxsize

# Variables
batch_size_values = [
    16,
    32,
    64,
    128,
    256
]

defaultValues = [
    8,
    16,
    32,
    64,
    128
]

img_height_values = []
img_width_values = []

max_seed_value = maxsize - 2
min_seed_value = 0

validation_split = 0.4

train_path = r''
validation_path = r''
test_path = r''

log_directory = r'/tmp/logs'
checkpoint_path = r'/tmp/checkpoint'

decay_steps = 2000
decay_rate = 0.4

optimizer = 'adam'


# has accessors
def get_checkpoint_path() -> str:
    global checkpoint_path
    return checkpoint_path


def set_checkpoint_path(
        value: str
) -> None:
    global checkpoint_path
    checkpoint_path = value


def get_batch_sizes() -> list:
    global batch_size_values
    return batch_size_values


def set_batch_sizes(
        value: list
) -> None:
    global batch_size_values
    batch_size_values = value


def get_batch_sizes_length() -> int:
    global batch_size_values
    return len(
        batch_size_values
    )


def get_height_values() -> list:
    global img_height_values

    if get_height_values_length() == 0:
        setup_arrays(
            img_height_values
        )

    return img_height_values


def get_width_values() -> list:
    global img_width_values

    if get_width_values_length() == 0:
        setup_arrays(
            img_width_values
        )

    return img_width_values


def get_width_values_length() -> int:
    global img_width_values

    return len(
        img_width_values
    )


def get_height_values_length() -> int:
    global img_height_values

    return len(
        img_height_values
    )


def set_width_values(
        value: list
) -> None:
    global img_width_values
    img_width_values = value


def set_height_values(
        value: list
) -> None:
    global img_height_values
    img_height_values = value


def get_validation_split() -> float:
    global validation_split
    return validation_split


def set_validation_split(
        value: float
):
    global validation_split
    validation_split = value


def get_test_path() -> str:
    global test_path
    return test_path


def set_test_path(
        value: str
) -> None:
    global test_path
    test_path = value


def get_validation_path() -> str:
    global validation_path
    return validation_path


def set_validation_path(
        value: str
) -> None:
    global validation_path
    validation_path = value


def get_train_path() -> str:
    global train_path
    return train_path


def set_train_path(
        value: str
) -> None:
    global train_path
    train_path = value


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


def get_log_directory() -> str:
    global log_directory
    return log_directory


def set_log_directory(
        value: str
) -> None:
    global log_directory
    log_directory = value


def setup_arrays(
        arr: list
) -> None:
    global defaultValues

    for e in defaultValues:
        arr.append(
            e
        )


def generate_seed() -> int:
    global \
        min_seed_value, \
        max_seed_value

    return random.randint(
        min_seed_value,
        max_seed_value
    )
