class Whileloop:
    def __init__(self, line):
        self.line = line[:-1].split()
    
    def writeWhile(self):
        output = ""
        output = output + " ".join(self.line) + "):\n"
        return output