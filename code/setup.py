import variables
import wandb


def start() -> None:
    wandb.tensorboard.patch(
        root_logdir=variables.get_log_directory()
    )

    wandb.init(
        project="Codespace",
        sync_tensorboard=True
    )


def end() -> None:
    wandb.finish()

