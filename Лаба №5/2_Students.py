# Laba No5 -- OOP -- Students

class Student:
    def __init__(self, name, settings_dict):
        self.name = name
        self.maxIndTaskMark = settings_dict['maxIndTaskMark']
        self.maxLabTaskMark = settings_dict['maxLabTaskMark']
        self.labAmount      = settings_dict['labAmount']
        self.avtomat        = settings_dict['avtomat']
        self.tryCountLab    = 0
        self.tryCountInd    = 0
        self.labs           = []
        for i in range(self.labAmount):
            self.labs.append(dict(tryCount = 0, mark = None))
    def passLabWork(self, mark, labID):
        if mark > self.maxLabTaskMark:
            try:
                self.labs[labID]['tryCount'] += 1
                self.labs[labID]['mark']      = mark
                return True
            except IndexError:
                return False
        else:
            return False
    def passIndWork(self, mark):
        if mark > self.maxIndTaskMark:
            self.tryCountInd += 1
            self.indWorkMark = mark
            return True
        else:
            return False
