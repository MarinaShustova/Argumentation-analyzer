import uuid


class ArgumentationTemplate:

    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name
        self.argumentation = {}
        self.theses = []
        self.arguments = []
        self.parameters = []

