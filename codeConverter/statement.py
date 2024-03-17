import searcher

class Statement:
    def __init__(self, line):
        self.line = line[:-1]
    
    def writeStatement(self, inClass = False, currClass = "", object = None):
        if inClass is True:
            miau = 3
        output = ""
        output = self.line + "\n"
        return output