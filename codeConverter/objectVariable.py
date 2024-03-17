class ObjectVariable:
    def __init__(self, line):
        self.line = line[:-1].split()
    
    def initialise(self):
        output = ""
        objType = self.line[0]
        self.line = self.line[1:]
        temp = " ".join(self.line)
        objName = temp[: temp.find("(")]
        objValue  = temp[temp.find("("):]
        output = output + objName + " = " + objType + objValue + "\n"
        return output
    
    def initialiseEmpty(self):
        output = ""
        objType = self.line[0]
        self.line = self.line[1:]
        temp = " ".join(self.line)
        objName = temp[: temp.find("(")]
        objValue  = "()"
        output = output + objName + " = " + objType + objValue + "\n"
        return output
    
    def getVariableName(self):
        line = " ".join(self.line)
        if("=" in line):
            return self.line[0]
        return line