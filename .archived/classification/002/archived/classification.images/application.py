from extra \
    import Extra


class Application:
    def __init__(self):
        self.title = 'ai'
        self.optional = Extra()

    def initialise(self):
        print(self.title)
        pass

    def execute(self):
        pass

    def gc(self):
        pass