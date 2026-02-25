from poll_model import PollModel
from option_model import OptionModel

class VotingService:
    polls: list[PollModel]

    def __init__(self):
        self.polls = []

    def allPolls(self):
        return self.polls

    def findPollByTitle(self, title: str):
        for poll in self.polls:
            if poll.title == title:
                return poll
        raise ValueError("Not Found")

    def addPoll(self, title: str):
        self.polls.append(PollModel(title=title))

    def deletePoll(self, title: str):
        for index, poll in enumerate(self.polls):
            if poll.title == title:
                del self.polls[index]
                return
        raise ValueError("Not Found")

    def addOption(self, pollTitle: str, optionName: str):
        poll = self.findPollByTitle(title=pollTitle)
        poll.options.append(OptionModel(name=optionName))

    def vote(self, pollTitle: str, optionName: str):
        poll = self.findPollByTitle(title=pollTitle)
        for option in poll.options:
            if option.name == optionName:
                option.votes += 1
                return
        raise ValueError("Not Found")

    def results(self, pollTitle: str):
        poll = self.findPollByTitle(title=pollTitle)
        return {option.name: option.votes for option in poll.options}
