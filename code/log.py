import wandb


def log_setup():
    art = wandb.Artifact(
        'configuration',
        'python'
    )

    art.add_file(
        '/mnt/c/Workspace/codespace/spaces/python/frameworks/Keras/code/config.py',
        'python'
    )

    wandb.init().log_artifact(art)

    checkpoint = wandb.Artifact('checkpoint', 'save-data')
    checkpoint.add_dir('/tmp/checkpoint')
    wandb.init().log_artifact(checkpoint)
