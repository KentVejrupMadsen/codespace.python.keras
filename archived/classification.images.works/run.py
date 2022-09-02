import wandb
from wandb.keras \
    import WandbCallback

import tensorflow as tf

from kerasDataset \
    import KerasDataset


dataset_dir = '/home/madsen/codespace/frameworks/keras/dataset/train'

classify_url = 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c60cd855-0e33-45b9-814d-35a17a0900d2/df75dwl-60c42ec7-0fa5-423a-8d51-4f2f36d11741.png/v1/fill/w_1280,h_490,q_80,strp/kupala_night_by_rav89_df75dwl-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NDkwIiwicGF0aCI6IlwvZlwvYzYwY2Q4NTUtMGUzMy00NWI5LTgxNGQtMzVhMTdhMDkwMGQyXC9kZjc1ZHdsLTYwYzQyZWM3LTBmYTUtNDIzYS04ZDUxLTRmMmYzNmQxMTc0MS5wbmciLCJ3aWR0aCI6Ijw9MTI4MCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.G1aB9_v6uA9EErrDqNASnH8q-jOsVf3yvIoc113yGEg'


def main():
    global classify_url
    wandb.init(project="codespace",
               entity="designermadsen")
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
    dataset.classify(classify_url)

    wandb.tensorflow.log(dataset.model.summary())


if __name__ == '__main__':
    main()