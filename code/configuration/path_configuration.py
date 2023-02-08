from os.path \
    import join

# Variables
log_directory = r'/tmp/logs/'
checkpoint_path = r'/tmp/checkpoint'

dataset_path = r'/tmp/dataset'

train_path = None
validation_path = None
test_path = None


# Accessors
def get_dataset_path() -> str:
    global dataset_path
    return dataset_path


def set_dataset_path(
        value: str
) -> None:
    global dataset_path
    dataset_path = value


def get_test_path() -> str:
    global test_path

    if test_path is None:
        return get_dataset_path()

    return join(
        get_dataset_path(),
        test_path
    )


def set_test_path(
        value: str
) -> None:
    global test_path
    test_path = value


def get_validation_path() -> str:
    global validation_path

    if validation_path is None:
        return get_dataset_path()

    return join(
        get_dataset_path(),
        validation_path
    )


def set_validation_path(
        value: str
) -> None:
    global validation_path
    validation_path = value


def get_train_path() -> str:
    global train_path

    if train_path is None:
        return get_dataset_path()

    return join(
        get_dataset_path(),
        train_path
    )


def set_train_path(
        value: str
) -> None:
    global train_path
    train_path = value


def get_log_directory() -> str:
    global log_directory
    return log_directory


def set_log_directory(
        value: str
) -> None:
    global log_directory
    log_directory = value


def get_checkpoint_path() -> str:
    global checkpoint_path
    return checkpoint_path


def set_checkpoint_path(
        value: str
) -> None:
    global checkpoint_path
    checkpoint_path = value
