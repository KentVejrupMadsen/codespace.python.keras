# https://wandb.ai/site/experiment-tracking
import wandb
from custom.configuration.wandb_variables \
    import                                 \
    get_wandb,                              \
    get_wandb_project_name,                  \
    get_wandb_sync_tensorboard,               \
    get_wandb_tags,                            \
    get_wandb_mode,                             \
    get_wandb_save_code,                         \
    get_wandb_name,                               \
    get_wandb_notes,                               \
    get_wandb_group,                                \
    set_wandb

from custom.configuration.tensorflow_settings import    \
    get_global_settings

######################################################################################
configuration = None


def get_configuration() -> dict:
    global configuration

    if configuration is None:
        configuration = dict()

    return configuration


def set_configuration(
        value: dict
) -> None:
    global configuration
    configuration = value


######################################################################################
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

        wandb.log(
            {
                'configuration': get_configuration()
            }
        )

    def execute(self):
        set_configuration(
            get_global_settings()
        )

        wandb.config = get_global_settings()

    def clear(self):
        get_wandb().finish(
            0,
            True
        )

