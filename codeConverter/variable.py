class Variable:
    def __init__(self, line):
        self.line = line[:-1].split()
    
    def initialise(self):
        output = ""
        self.line = self.line[1:]
        output = output + " ".join(self.line) + "\n"
        return output
    
    def initialiseEmpty(self):
        output = ""
        self.line = self.line[1:]
        output = output + " ".join(self.line) + " = 0\n"
        return output
    
    def getVariableName(self):
        line = " ".join(self.line)
        if("=" in line):
            return self.line[0]
        return line