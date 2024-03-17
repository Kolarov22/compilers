import re
class Replacer:
    replaced = {
         "true": "True",
         "false": "False",
         "this->": "self.",
         "switch": "match",
         "--" : " -= 1",
         "++" : " += 1",
    }
    def __init__(self, line):
        self.line = line
    
    def replace(self):
        for toReplace in self.replaced.keys():
            if(toReplace in self.line):
                self.line = self.line.replace(toReplace, self.replaced.get(toReplace))
        return self.line
    
    #def replace(self, )