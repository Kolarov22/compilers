class Printer:
    def __init__(self, line):
        line = line[4:]
        line = [arg.strip() for arg in line[:-1].split("<<") if arg.strip()]
        self.args = line
    
    def write(self):
        output = "print("
        for argument in self.args:
            match argument:
                case "endl": output = output + "end = '\\n', "
                case '" "': output = output + '" ", '
                case _: output = output + argument + ", "
        output = output[0: len(output) - 2] + ")\n"
        return output