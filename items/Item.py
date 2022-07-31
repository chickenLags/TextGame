

class Item:
    def __init__(self):
        pass

    def get_name(self):
        raise NotImplementedError()

    def to_row(self):
        return [self.get_name()]



