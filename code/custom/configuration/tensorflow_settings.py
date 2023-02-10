global_settings = dict()


def get_global_settings() -> dict:
    global global_settings
    return global_settings


def set_global_settings(
        value: dict
) -> None:
    global global_settings
    global_settings = value

