import wandb

from wandb.keras \
    import WandbCallback


def main():
    wandb.init(project="codespace", entity="designermadsen")
    print("run.py")

    wandb.config = {
        "learning_rate": 0.001,
        "epochs": 100,
        "batch_size": 128
    }


if __name__ == '__main__':
    main()