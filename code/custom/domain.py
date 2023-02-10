from keras.layers import Rescaling
from keras.utils import image_dataset_from_directory
from tensorflow.python.data import AUTOTUNE

from custom.stages.setup \
    import Setup

from custom.stages.models \
    import CustomModel

from custom.additional.setup_wandb \
    import SetupWandb

from custom.configuration.wandb_variables \
    import get_setup_of_wandb

from custom.configuration.tensorflow_settings \
    import get_global_settings


def get_dataset_path_from_settings():
    return get_global_settings()['dataset']['path']


class Domain:
    def __init__(self):
        self.setup = Setup()
        self.model = CustomModel()

        self.model.early_stopper_added()
        self.model.checkpoint_added()

        self.__wandb = None

    def initialise(self):
        if get_setup_of_wandb():
            self.__wandb = SetupWandb()
            self.__wandb.execute()

    def execute(self):
        self.model.fit(
            get_dataset_path_from_settings()
        )

    def garbage_collection(self):
        if not self.is_wandb_none:
            self.get_wandb().clear()

    def get_wandb(self) -> SetupWandb:
        return self.__wandb

    def set_wandb(
            self,
            setup: SetupWandb
    ) -> None:
        self.__wandb = setup

    def is_wandb_none(self):
        return self.__wandb is None


