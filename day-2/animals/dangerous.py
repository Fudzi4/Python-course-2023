class Birds:
    def __init__(self):
        self.members = ['Falcon','Eagle','Owl']
        
    def printMembers(self):
        print('Dangerous birds')
        for member in self.members:
            print('\t%s ' % member)


class Fish:
    def __init__(self):
        self.members = ['Pike','Shark','Salmon']
        
    def printMembers(self):
        print('Dangerous fish')
        for member in self.members:
            print('\t%s ' % member)