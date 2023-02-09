import wandb
from custom.configuration.Features \
    import \
    get_wandb_project_name, \
    get_wandb_sync_tensorboard, \
    get_wandb_tags, \
    get_wandb_mode, \
    get_wandb_save_code, \
    get_wandb_name, \
    get_wandb_notes, \
    get_wandb_group


class SetupWandb:
    def __init__(self):
        wandb.init(
            project=get_wandb_project_name(),
            sync_tensorboard=get_wandb_sync_tensorboard(),
            tags=get_wandb_tags(),
            mode=get_wandb_mode(),
            save_code=get_wandb_save_code(),
            name=get_wandb_name(),
            notes=get_wandb_notes(),
            group=get_wandb_group()
        )

    def execute(self):
        pass

    def clear(self):
        pass

