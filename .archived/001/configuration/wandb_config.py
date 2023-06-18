from datetime \
    import datetime

from dateutil \
    import tz

now = datetime.now(
    tz=tz.gettz(
        'Europe / Copenhagen'
    )
)

wandb_project = 'codespace'
wandb_sync_tensorboard = False

wandb_name = 'codespace_' + str(
    now.strftime(
        '%H_%M_%S'
    )
)


def get_wandb_project_name() -> str:
    global wandb_project
    return wandb_project


def set_wandb_project_name(
        value: str
) -> None:
    global wandb_project
    wandb_project = value


def get_sync_tensorboard() -> bool:
    global wandb_sync_tensorboard
    return wandb_sync_tensorboard


def set_sync_tensorboard(
        value: bool
) -> None:
    global wandb_sync_tensorboard
    wandb_sync_tensorboard = value


def get_wandb_name() -> str:
    global wandb_name
    return wandb_name


def set_wandb_name(
        value: str
) -> None:
    global wandb_name
    wandb_name = value

