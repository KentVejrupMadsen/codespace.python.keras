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

from custom.configuration.global_entries \
    import \
    get_image_width, \
    get_image_height, \
    get_max_classes, \
    get_epochs, \
    get_batch_size, \
    get_validation_split, \
    get_preserve_aspect


def get_image_size_from_settings():
    return (
        get_image_width(),
        get_image_height()
    )


def get_dataset_path_from_settings():
    return get_global_settings()['dataset']['path']


class Domain:
    def __init__(self):
        self.setup = Setup()
        self.model = CustomModel(
            (
                get_image_width(),
                get_image_height(),
                3
            )
        )

        self.model.early_stopper_added()
        self.model.checkpoint_added()

        print(self.model.callbacks)

        self.__wandb = None

    def initialise(self):
        if get_setup_of_wandb():
            self.__wandb = SetupWandb()
            self.__wandb.execute()

    def execute(self):
        batch_size = get_batch_size()

        epochs_size = get_epochs()
        seed_size = get_global_settings()['algorithm']['seed']
        validation_split_size = get_global_settings()['algorithm']['validation']['split']

        to_be_cropped = get_global_settings()['images']['keep_aspect_ratio']
        color_mode = get_global_settings()['images']['color']['mode']

        training = image_dataset_from_directory(
            get_dataset_path_from_settings(),
            color_mode=color_mode,
            batch_size=batch_size,
            shuffle=True,
            crop_to_aspect_ratio=to_be_cropped,
            image_size=get_image_size_from_settings(),
            subset='training',
            validation_split=validation_split_size,
            seed=seed_size
        )

        validation = image_dataset_from_directory(
            get_dataset_path_from_settings(),
            color_mode=color_mode,
            batch_size=batch_size,
            shuffle=True,
            crop_to_aspect_ratio=to_be_cropped,
            image_size=get_image_size_from_settings(),
            subset='validation',
            validation_split=validation_split_size,
            seed=seed_size
        )

        Rescaling(1./255)

        history = self.model.get_model().fit(
            training,
            validation_data=validation,
            epochs=epochs_size,
            callbacks=self.model.get_callbacks(),
            shuffle=True,
            validation_freq=50
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

    def debug(self):
        self.model.debug()

