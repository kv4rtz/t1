from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from voting_service import VotingService

app = FastAPI()

votingService = VotingService()

@app.get("/polls")
def getAllPolls():
    return votingService.allPolls()

@app.get("/polls/{title}")
def getPoll(title: str):
    try:
        return votingService.findPollByTitle(title=title)
    except ValueError:
        raise HTTPException(status_code=404, detail="Poll not found")

@app.post("/polls/{title}")
def createPoll(title: str):
    votingService.addPoll(title=title)
    return {"msg": f"Poll {title} successfully created"}

@app.delete("/polls/{title}")
def deletePoll(title: str):
    try:
        votingService.deletePoll(title=title)
        return {"msg": f"Poll {title} successfully deleted"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Poll not found")

@app.post("/polls/{title}/options/{optionName}")
def createOption(title: str, optionName: str):
    try:
        votingService.addOption(pollTitle=title, optionName=optionName)
        return {"msg": f"Option {optionName} successfully created"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Poll not found")

@app.post("/polls/{title}/vote/{optionName}")
def vote(title: str, optionName: str):
    try:
        votingService.vote(pollTitle=title, optionName=optionName)
        return {"msg": f"Vote successfully recorded"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Poll or option not found")

@app.get("/polls/{title}/results")
def getResults(title: str):
    try:
        return votingService.results(pollTitle=title)
    except ValueError:
        raise HTTPException(status_code=404, detail="Poll not found")
