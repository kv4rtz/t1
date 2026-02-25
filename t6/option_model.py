class OptionModel:
    name: str
    votes: int

    def __init__(self, name: str):
        self.name = name
        self.votes = 0
