import controller


class Issue:

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def asCard(self):
        return controller.SendIssue(self)
