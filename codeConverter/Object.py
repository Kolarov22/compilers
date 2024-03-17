class Object:
    def __init__(self, name):
        self.name = name
        self.members = []

    def addMember(self, memberName, memberType="public"):
        self.members.append((memberName, memberType))

    def getMemberType(self, memberName):
        for i in self.members:
            if i[0] == memberName:
                return i[1]
        return None

    def getName(self):
        return self.name

    def getMembers(self):
        return self.members
