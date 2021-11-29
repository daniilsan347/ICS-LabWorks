# Laba No5 -- OOP -- Modified String Class

class ModStr(str):
    def __init__(self, string):
        if type(string) == str:
            self = string
    def repetives(self):
        for i in range(len(self)):
            if len(self) == 3:
                if self.count(self[i:i+3]) > 1:
                    return True
            else: 
                return False
    def palindrom(self):
        if self[::-1] == self:
            return True
        elif self == "":
            return True
        else:
            return False

print(ModStr("haha").repetives())
print(ModStr("тенет").palindrom())