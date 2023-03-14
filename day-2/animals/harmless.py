class Birds:
    def __init__(self):
        self.members = ['Sparrow','Finch','Goose']
        
    def printMembers(self):
        print('Harmless birds')
        for member in self.members:
            print('\t%s ' % member)


class Fish:
    def __init__(self):
        self.members = ['Bass','Cod','Trout']
        
    def printMembers(self):
        print('Harmless fish')
        for member in self.members:
            print('\t%s ' % member)