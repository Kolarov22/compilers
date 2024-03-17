class Classes:
    def __init__(self, line):
        self.line = line.split()
    
    def writeClass(self):
        output = ""
        output = output + " ".join(self.line) + ":\n"
        return output
    
    def getClassName(self):
        line = self.line
        line = line[1]
        return line