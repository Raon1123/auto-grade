class student:
    def __init__(self):
        self.id = -1
        self.score = 0
        self.codepath = ''

    def codePath(self):
        return self.codepath

    def printId(self):
        print(self.id)

    def printScore(self):
        print(str(self.id) + ": " + str(self.score))