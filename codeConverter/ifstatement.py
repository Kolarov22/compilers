class Ifstatement:
    def __init__(self, line):
        self.line = line[:-1].split()
    
    def writeIf(self):
        output = ""
        output = output + " ".join(self.line) + "):\n"
        return output