from option_model import OptionModel

class PollModel:
    title: str
    options: list[OptionModel]

    def __init__(self, title: str):
        self.title = title
        self.options = []
