models_path = '/home/madsen/models/'
checkpoint_path = '/home/madsen/checkpoint/'

log_path = '/tmp/logs/'


def get_models_path() -> str:
    global models_path
    return models_path


def get_checkpoint_path() -> str:
    global checkpoint_path
    return checkpoint_path


def get_log_path() -> str:
    global log_path
    return log_path

