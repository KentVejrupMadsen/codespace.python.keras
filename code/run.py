import wandb
from wandb.keras \
    import WandbCallback

import tensorflow as tf

from kerasDataset \
    import KerasDataset


dataset_dir = '/home/madsen/codespace/frameworks/keras/dataset/train'


def main():
    wandb.init(project="codespace", entity="designermadsen")
    print("run.py")

    dataset = KerasDataset()
    dataset.setup_dataset()
    dataset.setup_model()

    wandb.config = {
        "learning_rate": 0.001,
        "epochs": dataset.epoch,
        "batch_size": dataset.properties.get_batch_size()
    }

    dataset.train()

    wandb.tensorflow.log( dataset.last_history )
    wandb.tensorflow.log( dataset.model.summary() )


if __name__ == '__main__':
    main()