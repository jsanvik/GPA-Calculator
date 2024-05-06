class Course:
    #constructor
    def __init__(self, name):
        self.name = name
    
    #Item list is a dictionary with a string as the key and a 2-tuple of floats (weight, grade) as the value.
    items = {}
    def addItem(self, name, weight, grade):
        #item name as a string
        itemname = str(name)
        #item grade is a 2-tuple (weight, grade%). 
        #Enter grade as a percent: A grade of 50% should be entered as 50, not 0.5 or 0.50
        itemgrade = (float(weight), float(grade))
        self.items[name] = itemgrade
    
    #function calculates and returns final grade, calculated using each weighted item.
    def getFinalGrade(self):
        total = 0
        for i in self.items:
            total+= float(self.items[i][0])/100*self.items[i][1]
        return total