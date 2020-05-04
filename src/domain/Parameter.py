import uuid


class Parameter:

    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name
        self.value = None

    def set_value(self, value):
        self.value = value
