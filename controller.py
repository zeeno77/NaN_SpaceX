import json
from random import choice
from trello import TrelloApi
from models.Bug import Bug
from models.Task import Task
from models.Issue import Issue

Trello_app_key = ""
Trello_token = ""
Trello_boardId = ""
CARD_POS = "top"


def Request_handler(data):
    try:
        if data["type"] == "bug":
            task = Bug(data["description"])
        else:
            if data["type"] == "issue":
                task = Issue(data["title"], data["description"])
            else:
                if data["type"] == "task":
                    task = Task(data["title"], data["category"])
        return task
    except Exception:
        return "400 - Bad parameters\n", 400


def SendIssue(task):
    trello = TrelloApi(Trello_app_key, Trello_token)
    listID = findListID("To Do")
    newCard = trello.cards.new(task.title, idList=listID,
                               desc=task.description, pos=CARD_POS)
    return newCard


def SendBug(task):
    trello = TrelloApi(Trello_app_key, Trello_token)
    members = trello.boards.get_member(Trello_boardId)
    labelID = findLabelID("Bug")
    listID = findListID("To Do")
    newCard = trello.cards.new(task.title, idList=listID,
                               desc=task.description,
                               idMembers=choice(members)["id"],
                               idLabels=labelID, pos=CARD_POS)
    return newCard


def SendTask(task):
    trello = TrelloApi(Trello_app_key, Trello_token)
    labelID = findLabelID(task.label)
    listID = findListID("To Do")
    newCard = trello.cards.new(task.title, idList=listID, idLabels=labelID,
                               pos=CARD_POS)
    return newCard


# findLabelID searches for a label by name and return it's id if the label\
#  doesn't exists it creates it
def findLabelID(name):
    colors = ["green", "yellow", "orange", "red", "purple", "blue", "sky",
              "lime", "pink", "black"]
    trello = TrelloApi(Trello_app_key, Trello_token)
    labels = trello.boards.get_label(Trello_boardId)
    labelID = False
    for label in labels:
        if label["name"] == name:
            labelID = label["id"]
    if not labelID:
        label = trello.labels.new(name, choice(colors), Trello_boardId)
        labelID = label["id"]
    return labelID


# findListID searches for a list by name and return it's id \
# if the list doesn't exists, or it's closed, it creates it
def findListID(name):
    trello = TrelloApi(Trello_app_key, Trello_token)
    lists = trello.boards.get_list(Trello_boardId)
    listID = False
    for li in lists:
        if li["name"] == name and not li["closed"]:
            listID = li["id"]
        if not listID:
            li = trello.lists.new(name, Trello_boardId)
            listID = li["id"]
    return listID


def SetupBoard(file_path):
    global Trello_app_key
    global Trello_token
    global Trello_boardId
    try:
        f = open(file_path)
        data = json.load(f)
        Trello_app_key = data["key"]
        Trello_token = data["token"]
        Trello_boardId = data["boardId"]
        f.close()
    except Exception:
        print("500 - Internal Server Error - Configuration file error\n")
        raise


def ShowBoard():
    trello = TrelloApi(Trello_app_key, Trello_token)
    return trello.boards.get(Trello_boardId)


def ShowMembers():
    trello = TrelloApi(Trello_app_key, Trello_token)
    return trello.boards.get_member(Trello_boardId)


def ShowLists():
    trello = TrelloApi(Trello_app_key, Trello_token)
    return trello.boards.get_list(Trello_boardId)
