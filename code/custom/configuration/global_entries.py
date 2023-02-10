from custom.configuration.tensorflow_settings \
    import \
    get_global_model_settings, \
    get_value_from_global_images_settings, \
    get_value_from_global_algorithm_settings, \
    get_value_from_global_dataset_settings


batch_size = None

epochs = None

image_width = None
image_height = None
image_color_channels = None
image_color_mode = None

preserve_aspect = True

validation_split = None

# Categories
max_classes = None
seed = None

model_name = None


def get_image_color_mode():
    global image_color_mode

    if image_color_mode is None:
        set_image_color_mode(
            get_value_from_global_images_settings(
                'color'
            )['mode']
        )

    return image_color_mode


def set_image_color_mode(
        value: str
):
    global image_color_mode
    image_color_mode = value


def get_model_name():
    global model_name

    if model_name is None:
        set_model_name(
            get_global_model_settings()[
                'name'
            ]
        )

    return model_name


def set_model_name(
        value: str
):
    global model_name
    model_name = value


def get_seed() -> int:
    global seed

    if seed is None:
        set_seed(
            get_value_from_global_algorithm_settings(
                'seed'
            )
        )

    return seed


def set_seed(
        value: int
) -> None:
    global seed
    seed = value


def get_max_classes() -> int:
    global max_classes

    if max_classes is None:
        set_max_classes(
            get_value_from_global_dataset_settings(
                'categories'
            )
        )

    return max_classes


def set_max_classes(
        value: int
):
    global max_classes
    max_classes = value


def get_batch_size() -> int:
    global batch_size

    if batch_size is None:
        set_batch_size(
            get_value_from_global_algorithm_settings(
                'batch_size'
            )
        )

    return batch_size


def set_batch_size(value: int):
    global batch_size
    batch_size = value


def get_validation_split() -> int:
    global validation_split

    if validation_split is None:
        set_validation_split(
            get_value_from_global_algorithm_settings(
                'validation'
            )['split']
        )

    return validation_split


def set_validation_split(value: int):
    global validation_split
    validation_split = value


def get_preserve_aspect() -> bool:
    global preserve_aspect

    if preserve_aspect is None:
        set_preserve_aspect(
            get_value_from_global_images_settings(
                'keep_aspect_ratio'
            )
        )

    return preserve_aspect


def set_preserve_aspect(
        value: bool
):
    global preserve_aspect
    preserve_aspect = value


def get_image_width() -> int:
    global image_width

    if image_width is None:
        set_image_width(
            get_value_from_global_images_settings(
                'width'
            )
        )

    return image_width


def set_image_width(
        value: int
):
    global image_width
    image_width = value


def get_image_height() -> int:
    global image_height

    if image_height is None:
        set_image_height(
            get_value_from_global_images_settings(
                'height'
            )
        )

    return image_height


def set_image_height(
        value: int
):
    global image_height
    image_height = value


def get_epochs() -> int:
    global epochs

    if epochs is None:
        set_epochs(
            get_value_from_global_algorithm_settings(
                'epochs'
            )
        )

    return epochs


def set_epochs(
        value: int
):
    global epochs
    epochs = value


def get_image_color_channels() -> str:
    global image_color_channels

    if image_color_channels is None:
        set_image_color_channels(
            get_value_from_global_images_settings(
                'color'
            )['mode']
        )

    return image_color_channels


def set_image_color_channels(
        value: str
):
    global image_color_channels
    image_color_channels = value

