import Object
import re
class objectReplacer:
    
    objects = []
    
    def add_spaces_around_parentheses(self, input_string):
        modified_string = re.sub(r'(\()(\S)', r'\1 \2', input_string)
        modified_string = re.sub(r'(\S)(\))', r'\1 \2', modified_string)
        
        return modified_string
    
    def __init__(self, line, objects, currClass):
        self.line = self.add_spaces_around_parentheses(line)
        self.objects = objects
        self.currClass = currClass
    
    def _search(self, word):
        for i in self.objects:
            for j in i.getMembers():
                if(word in j[0]):
                    if j[1] == "private":
                        return "_" + word
                    elif j[1] == "protected":
                        return "__" + word
                    else:
                        return word 
        return None 
    
    def _searchInClass(self, word):   
        for i in self.objects:
            if i.getName() in self.currClass:
                for j in i.getMembers():
                    if(word in j[0]):
                        if j[1] == "private":
                            return "_" + word
                        elif j[1] == "protected":
                            return "__" + word
                        else:
                            return word 
        return None 
    
    def replace(self):
        line = self.line.split(" ")
        if self.currClass == "":
            for i in range(len(line)):
                search = self._search(line[i])
                if search is not None:
                    line[i] = search
            return " ".join(line)
        else:
            for i in range(len(line)):
                search = self._searchInClass(line[i])
                if search is not None:
                    line[i] = search
            return " ".join(line)     