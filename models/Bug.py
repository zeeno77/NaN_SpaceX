from models.Issue import Issue
import controller
from random import choice, randrange
import string


class Bug(Issue):
    def __init__(self, description):
        title = self.generateTitle()
        super().__init__(title, description)
        self.label = "Bug"

    # Generates a title with the pattern: bug-{word}-{number}
    # The word is randomly generated, it's between 4 and 20 characters
    # and each character is an upper or lower letter
    def generateTitle(self):
        word = ""
        for i in range(randrange(4, 20)):
            word = word+choice(string.ascii_letters)
        finalWord = "bug-"+word+"-"+str(randrange(0, 9999999))
        return finalWord

    def asCard(self):
        return controller.SendBug(self)
