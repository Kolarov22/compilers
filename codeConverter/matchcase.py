import printer
class Case:
    def __init__(self, line):
        self.line = line
    
    def writeCase(self):
        output = ""
        if("cout" in self.line):
            number = self.line[self.line.find(" ") : self.line.find(":")].strip()
            toPrint = self.line[self.line.find(":") + 1 : self.line.find(";") + 1].strip()
            printed = printer.Printer(toPrint)
            output = "case " + number + ": " +  printed.write()
            return output
        return self.line