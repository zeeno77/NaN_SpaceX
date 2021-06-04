from typing import NoReturn


import controller


class Task:
    categories = ["Maintenance", "Research", "Test"]

    def __init__(self, title, category):
        if category in self.categories:
            self.label = category
            self.title = title

    def asCard(self):
        return controller.SendTask(self)
