from os.path \
    import join

# Variables
log_directory = r'/tmp/logs/'
checkpoint_path = r'/tmp/checkpoint/'

dataset_path = r'/tmp/dataset'

train_path = None
validation_path = None
test_path = None


cache_file_path = '/tmp/dataset'
cache_training_path = join(cache_file_path, 'training')
cache_test_path = join(cache_file_path, 'test')
cache_validation = join(cache_file_path, 'validation')

cached_log_path = None


def get_log_path(name) -> str:
    global \
        log_directory, \
        cached_log_path

    if cached_log_path is None:
        cached_log_path = join(log_directory, name)
        return cached_log_path

    return cached_log_path


def get_cache_training_path() -> str:
    global cache_training_path
    return cache_training_path


def set_cache_training_path(
        value: str
):
    global cache_training_path
    cache_training_path = value


def get_cache_test_path() -> str:
    global cache_test_path
    return cache_test_path


def set_cache_test_path(
        value: str
):
    global cache_test_path
    cache_test_path = value


def get_cache_validation_path() -> str:
    global cache_validation
    return cache_validation


def set_cache_validation_path(
        value: str
):
    global cache_validation
    cache_validation = value


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
