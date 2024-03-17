import re
class Forloop:
    def __init__(self, line):
        pattern = r'for\s*\(\s*([^;]*)\s*;\s*([^;]*)\s*;\s*([^)]*)\s*\)'
        matches = re.search(pattern, line)
        if matches:
            self.start_value = matches.group(1).strip()
            self.end_value = matches.group(2).strip()
            self.step_value = matches.group(3).strip()
    
    def writeFor(self):
        variable = self.start_value[4:5]
        start = int(''.join(arg for arg in self.start_value if arg.isdigit()))
        end = int(''.join(arg for arg in self.end_value if arg.isdigit()))
        if(self.step_value == "i++"):
            step = 1
        else:
            step = int(''.join(arg for arg in self.step_value if arg.isdigit()))
        output = "for " + variable  + " in range(" + str(start) + ", " + str(end) + ", " + str(step) + "):\n"
        return output