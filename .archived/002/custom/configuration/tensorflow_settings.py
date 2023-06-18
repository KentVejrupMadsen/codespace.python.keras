global_settings = dict()


def get_global_settings() -> dict:
    global global_settings
    return global_settings


def set_global_settings(
        value: dict
) -> None:
    global global_settings
    global_settings = value


def get_global_algorithm_settings() -> dict:
    global_values = get_global_settings()
    return global_values[
        'algorithm'
    ]


def get_global_model_settings() -> dict:
    global_values = get_global_algorithm_settings()
    return global_values[
        'model'
    ]


def get_value_from_global_algorithm_settings(
        key: str
):
    return get_global_algorithm_settings()[
        key
    ]


def get_global_dataset_settings() -> dict:
    global_values = get_global_settings()
    return global_values[
        'dataset'
    ]


def get_value_from_global_dataset_settings(
        key: str
):
    return get_global_dataset_settings()[
        key
    ]


def get_global_checkpoint_settings() -> dict:
    global_values = get_global_algorithm_settings()
    return global_values[
        'checkpoint'
    ]


def get_global_images_settings():
    global_values = get_global_settings()
    return global_values[
        'images'
    ]


def get_value_from_global_images_settings(
        key: str
):
    return get_global_images_settings()[
        key
    ]



