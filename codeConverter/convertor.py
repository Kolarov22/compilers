import printer
import checker
import ifstatement
import variable
import statement
import forloop
import whileloop
import methods
import replacer
import matchcase
import classes
import Object
import objectVariable
import objectReplacer

read = open("source.cpp", "r")
write = open("result.py", "w")
#tabulate = 0
#elseTabulate = 0
brackets = 0
type = "public"
inClass = False
currClass = ""
objects = []
myClasses = []
for line in read:
    line = line.strip()
    line = replacer.Replacer(line).replace()
    
    for myClass in myClasses:
        if myClass in line:
            if checker.Checker(line, brackets, myClass).check() == "obj variable":
                printed = objectVariable.ObjectVariable(line)
                if brackets > 0:
                    for i in range(brackets):
                        write.write("\t")
                objReplacer = objectReplacer.objectReplacer(printed.initialise(), objects, currClass)
                write.write(objReplacer.replace())
                for obj in objects:
                    if obj.getName() == currClass:
                        obj.addMember(printed.getVariableName(), type)
                continue
            
            if checker.Checker(line, brackets, myClass).check() == "empty obj variable":
                printed = objectVariable.ObjectVariable(line)
                if brackets > 0:
                    for i in range(brackets):
                        write.write("\t")
                objReplacer = objectReplacer.objectReplacer(printed.initialiseEmpty(), objects, currClass)
                write.write(objReplacer.replace())
                for obj in objects:
                    if obj.getName() == currClass:
                        obj.addMember(printed.getVariableName(), type)
                continue
            
    if len(line) == 0:
        continue
    if line == "{":
        brackets += 1
        continue
    if line == "}":
        brackets -= 1
        continue
    
    if line == "};":
        type = "public"
        brackets -= 1
        inClass = False
        currClass = ""
        continue
    
    if checker.Checker(line, brackets).check() == "include":
        module = line[line.find("<") + 1: line.find(">")]
        if module == "cmath":
            write.write("import math\n")
        continue
            
    if checker.Checker(line, brackets).check() == "print":
        printed = printer.Printer(line)
        if brackets > 0:
            for i in range(brackets):
                write.write("\t")
        objReplacer = objectReplacer.objectReplacer(printed.write(), objects, currClass)
        write.write(objReplacer.replace())
        continue
        
    if checker.Checker(line, brackets).check() == "if":
        #tabulate += 1
        printed = ifstatement.Ifstatement(line)
        if brackets > 0:
            for i in range(brackets):
                write.write("\t")
        objReplacer = objectReplacer.objectReplacer(printed.writeIf(), objects, currClass)
        write.write(objReplacer.replace())
        continue
        
    if(line == "else"):
        #elseTabulate += 1
        if brackets > 0:
            for i in range(brackets):
                write.write("\t")
        write.write("else:\n")
        continue
        
    if checker.Checker(line, brackets).check() == "variable":
        printed = variable.Variable(line)
        if brackets > 0:
            for i in range(brackets):
                write.write("\t")
        objReplacer = objectReplacer.objectReplacer(printed.initialise(), objects, currClass)
        write.write(objReplacer.replace())
        for obj in objects:
            if obj.getName() == currClass:
                obj.addMember(printed.getVariableName(), type)
        continue
    
    if checker.Checker(line, brackets).check() == "empty variable":
        printed = variable.Variable(line)
        if brackets > 0:
            for i in range(brackets):
                write.write("\t")
        objReplacer = objectReplacer.objectReplacer(printed.initialiseEmpty(), objects, currClass)
        write.write(objReplacer.replace())
        for obj in objects:
            if obj.getName() == currClass:
                obj.addMember(printed.getVariableName(), type)
        continue
    
    if checker.Checker(line, brackets).check() == "statement":
        printed = statement.Statement(line)
        if brackets > 0:
            for i in range(brackets):
                write.write("\t")
        objReplacer = objectReplacer.objectReplacer(printed.writeStatement(), objects, currClass)
        write.write(objReplacer.replace())
        continue
    
    if checker.Checker(line, brackets).check() == "for":
        printed = forloop.Forloop(line)
        if brackets > 0:
            for i in range(brackets):
                write.write("\t")
        objReplacer = objectReplacer.objectReplacer(printed.writeFor(), objects, currClass)
        write.write(objReplacer.replace())
        continue
    
    if checker.Checker(line, brackets).check() == "while":
        printed = whileloop.Whileloop(line)
        if brackets > 0:
            for i in range(brackets):
                write.write("\t")
        objReplacer = objectReplacer.objectReplacer(printed.writeWhile(), objects, currClass)
        write.write(objReplacer.replace())
        continue
    
    if checker.Checker(line, brackets).check() == "method":
        printed = methods.Methods(line)
        if brackets > 0:
            for i in range(brackets):
                write.write("\t")
        objReplacer = objectReplacer.objectReplacer(printed.writeMethod(type, inClass), objects, currClass)
        write.write(objReplacer.replace())
        for obj in objects:
            if obj.getName() == currClass:
                obj.addMember(printed.getMethodName(), type)
        continue
    
    if checker.Checker(line, brackets).check() == "switch":
        objReplacer = objectReplacer.objectReplacer(line + ": \n", objects, currClass)
        write.write(objReplacer.replace())
        continue
    
    if checker.Checker(line, brackets).check() == "matchcase":
        printed = matchcase.Case(line)
        if brackets > 0:
            for i in range(brackets):
                write.write("\t")
        objReplacer = objectReplacer.objectReplacer(printed.writeCase(), objects, currClass)
        write.write(objReplacer.replace())
        continue
    
    if checker.Checker(line, brackets).check() == "class":
        inClass = True
        printed = classes.Classes(line)
        currClass = printed.getClassName()
        if currClass not in myClasses:
            myClasses.append(currClass)
        if brackets > 0:
            for i in range(brackets):
                write.write("\t")
        write.write(printed.writeClass())
        object = Object.Object(printed.getClassName())
        objects.append(object)
        continue

    if line == "public:":
        type = "public"
        continue
    if line == "protected:":
        type = "protected"
        continue
    if line == "private:":
        type = "private"
        continue
    
    if checker.Checker(line, brackets).check() == "main":
        brackets -= 1
        continue