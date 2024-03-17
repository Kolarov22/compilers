class Checker:
    dataTypes= ["int", "float", "double", "long", "string", "char", "unsigned"]
    dataTypesOriginalLength = len(dataTypes)
    def __init__(self, line, brackets, additionalDataTypes = None):
        self.line = line[:-1].split()
        if(brackets == 0):
            self.inBrackets = False
        else:
            self.inBrackets = True      
        if additionalDataTypes != None:
            self.dataTypes.append(additionalDataTypes)
        
    def check(self):
        if("for" in self.line[0]):
            return "for"
        if("while" in self.line[0]):
            return "while"
        if("if" in self.line[0]):
            return "if"
        if("cout" in self.line[0]):
            return "print"
        if("#" in self.line[0]):
            return "include"
        if("switch" in self.line[0] or "match" in self.line[0]):
            return "switch"
        if("case" in self.line[0]):
            return "matchcase"
        if("class" in self.line[0]):
            return "class"
            
        if(self.line[0] in self.dataTypes):
            if("main" in self.line[1]):
                return "main"
            if(self.line[0] not in self.dataTypes[:7]):
                temp = "".join(self.line)
                length = len(temp[temp.find("(") : temp.find(")")])
                if length == 0:
                    return "empty obj variable"
                return "obj variable"
            if(len(self.line) == 2 and self.line[1] not in "()=!"):
                return "empty variable"
            if("=" in self.line[1] or self.line[2] == "="):
                return "variable"
            else:
                if("(" in self.line[1] or "(" in self.line[2]):
                    return "method"
        elif(self.line[0] == "void"):
            return "method"
        if("using" in self.line[0] or "public" in self.line[0] or "private" in self.line[0] or "protected" in self.line[0]):
            return
         
        return "statement"

        