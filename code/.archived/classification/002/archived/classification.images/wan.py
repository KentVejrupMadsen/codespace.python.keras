import wandb

from wandb.keras \
    import WandbCallback


def init_config():
    wandb.config = \
    {
        "learning_rate": 0.10,
        "epochs": 300,
        "batch_size": 32
    }


class Wan:
    def __init__( self, project_name="keras-codespace", entity="designermadsen"):
        self.wdb = wandb.init(project=project_name, entity=entity)
        init_config()
