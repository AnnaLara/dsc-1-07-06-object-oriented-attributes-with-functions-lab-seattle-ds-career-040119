class School():
    def __init__(self, name, roster={}):
        self.name = name
        self.roster = roster
        
    def add_student(self, name, grade):
        if grade in self.roster.keys():
            self.roster[grade].append(name)
        else:
            self.roster.update({grade: [name]})
            
    def grade(self, grade):
        return self.roster[grade]
    
    def sort_roster(self):
        for value in self.roster.values():
            value.sort()
        
