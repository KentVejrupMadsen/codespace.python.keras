setup_of_wandb = False


def get_setup_of_wandb() -> bool:
    global setup_of_wandb
    return setup_of_wandb


def set_setup_of_wandb(
        value: bool
) -> None:
    global setup_of_wandb
    setup_of_wandb = value

##################################################################################################


wandb_project_name = 'codespace'


def get_wandb_project_name() -> str:
    global wandb_project_name
    return wandb_project_name


def set_wandb_project_name(
        value: str
) -> None:
    global wandb_project_name
    wandb_project_name = value

##################################################################################################


wandb_settings_sync_tensorboard = False


def get_wandb_sync_tensorboard() -> bool:
    global wandb_settings_sync_tensorboard
    return wandb_settings_sync_tensorboard


def set_wandb_sync_tensorboard(
        value: bool
) -> None:
    global wandb_settings_sync_tensorboard
    wandb_settings_sync_tensorboard = value

##################################################################################################


wandb_settings_tags = []


def get_wandb_tags() -> list:
    global wandb_settings_tags
    return wandb_settings_tags


def set_wandb_tags(
        value: list
) -> None:
    global wandb_settings_tags
    wandb_settings_tags = value

##################################################################################################


wandb_settings_mode = 'online'


def get_wandb_mode() -> str:
    global wandb_settings_mode
    return wandb_settings_mode


def set_wandb_mode(
        value: str
) -> None:
    global wandb_settings_mode
    wandb_settings_mode = value

##################################################################################################


wandb_settings_save_code = False


def get_wandb_save_code() -> bool:
    global wandb_settings_save_code
    return wandb_settings_save_code


def set_wandb_save_code(
        value: bool
) -> None:
    global wandb_settings_save_code
    wandb_settings_save_code = value

##################################################################################################


wandb_settings_name = ''


def get_wandb_name() -> str:
    global wandb_settings_name
    return wandb_settings_name


def set_wandb_name(
        value: str
) -> None:
    global wandb_settings_name
    wandb_settings_name = value

##################################################################################################


wandb_settings_notes = ''


def get_wandb_notes() -> str:
    global wandb_settings_notes
    return wandb_settings_notes


def set_wandb_notes(
        value: str
) -> None:
    global wandb_settings_notes
    wandb_settings_notes = value

##################################################################################################


wandb_settings_group = ''


def get_wandb_group() -> str:
    global wandb_settings_group
    return wandb_settings_group


def set_wandb_group(
        value: str
) -> None:
    global wandb_settings_group
    wandb_settings_group = value

