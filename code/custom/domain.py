from custom.stages.setup \
    import Setup

from custom.stages.kera_model \
    import KeraModel

from custom.additional.setup_wandb \
    import SetupWandb

from custom.configuration.Features \
    import get_setup_of_wandb


class Domain:
    def __init__(self):
        self.setup = Setup()
        self.model = KeraModel()

        self.__wandb = None

    def initialise(self):
        if get_setup_of_wandb():
            self.__wandb = SetupWandb()
            self.__wandb.execute()


    def execute(self):
        pass

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


