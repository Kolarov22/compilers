class Methods:
    dataTypes = ["int", "float", "double", "long", "string", "char", "unsigned", "void"]

    def __init__(self, line):
        self.line = line[:-1].split()

    def writeMethod(self, access, inClass):
        output = ""
        self.line = [x for x in self.line if x not in self.dataTypes]
        method_name = self.line[0].split("(")[0]
        if inClass:
            try:
                if self.line[1] == "":
                    if access == "private":
                        output = f"def __{method_name}(self):\n"
                    elif access == "protected":
                        output = f"def _{method_name}(self):\n"
                    else:
                        output = f"def {method_name}(self):\n"
                else:
                    if access == "private":
                        output = f"def __{method_name}(self, {''.join(self.line[1:])}):\n"
                    elif access == "protected":
                        output = f"def _{method_name}(self, {''.join(self.line[1:])}):\n"
                    else:
                        output = f"def {method_name}(self, {''.join(self.line[1:])}):\n"
                return output
            except IndexError:
                output = f"def {method_name}(self):\n"
                return output

        output = f"def {method_name}({''.join(self.line[1:])}):\n"
        return output

    def getMethodName(self):
        method_name = self.line[0].split("(")[0]
        return method_name
