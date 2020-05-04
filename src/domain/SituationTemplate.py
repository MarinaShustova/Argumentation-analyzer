import uuid


class SituationTemplate:

    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name
        self.theses = []
        self.parameters = []
