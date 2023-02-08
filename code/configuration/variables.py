from configuration.variable_setup \
    import setup_arrays

# Variables
batch_size_index = 0

batch_size_values = [
    8,
    16,
    32,
    64,
    128,
    256,
    512
]


img_height_index = 0
img_height_values = []

img_width_index = 0
img_width_values = []


def get_width_index() -> int:
    global img_width_index
    return img_width_index


def get_height_index() -> int:
    global img_height_index
    return img_height_index


# has accessors
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


def get_batch_size_index() -> int:
    global batch_size_index
    return batch_size_index


def set_batch_size_index(
        value: int
) -> None:
    global batch_size_index
    batch_size_index = value


def get_default_batch_size() -> int:
    if get_batch_size_index() > get_batch_sizes_length():
        set_batch_size_index(
            get_batch_size_index() %
            get_batch_sizes_length()
        )

    return get_batch_size_index()


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




