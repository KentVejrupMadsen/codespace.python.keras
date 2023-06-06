from custom.configuration \
    import get_log_directory

from custom.configuration \
    import \
    get_wandb_project_name, \
    get_sync_tensorboard

import wandb

api = None


def start() -> None:
    wandb.tensorboard.patch(
        root_logdir=get_log_directory()
    )

    wandb.init(
        project=get_wandb_project_name(),
        sync_tensorboard=get_sync_tensorboard(),
        name=''
    )


def get_api():
    global api

    if api is None:
        api = wandb.Api()

    return api


def end() -> None:
    wandb.finish()

