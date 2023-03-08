from random \
    import randint


class KerasProperties:
    def __init__(self):
        self.batch_size = 64

        self.height = 128
        self.width = 384

        self.validation_size = 0.25
        self.seed = randint(0, 20000)

    def get_batch_size(self):
        return self.batch_size

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def get_validation_size(self):
        return self.validation_size

    def get_seed(self):
        return self.seed
