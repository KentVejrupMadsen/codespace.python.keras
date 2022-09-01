class KerasProperties:
    def __init__(self):
        self.batch_size = 64
        self.height = 128
        self.width = 384
        self.validation_size = 0.25

    def get_batch_size(self):
        return self.batch_size

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def get_validation_size(self):
        return self.validation_size


class KerasDataset:
    def __init__(self):
        self.path = ''
        self.properties = KerasProperties()
        self.subset = 'training'
        self.seed = 1


    def setup_dataset(self):
        pass


