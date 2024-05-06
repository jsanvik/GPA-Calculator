class Course:
    #constructor
    def __init__(self, name):
        self.name = name
    
    #Item list (weightedItems) is a dictionary with a string as the key and a 2-tuple of floats (weight, grade) as the value.
    weightedItems = {}
    
    #Add a weighted item ("Assignments", "Projects", etc)
    def addItem(self, name, weight, grade):
        #item name as a string
        itemname = str(name)
        itemgrade = (float(weight), float(grade))
        #item grade is a 2-tuple (weight, grade%). 
        #Grade should be input as a percent: A grade of 50% should be entered as 50, not 0.5 or 0.50
        
        #Check if total weight exceeds 100%
        totalweight = 0
        for value in self.weightedItems.values():
            totalweight += value[0]
        #If total weight would not exceed 100%, add this item to collection of weightedItems
        if (float(totalweight) + float(weight)) <= 100:
            self.weightedItems[name] = itemgrade
        else:
            print("ERROR: Weight exceeds 100% (" + str(totalweight + itemgrade[0]) + "%). Please try again")
    
    #function to list all items
    def listItems(self):
        template = "Item name: {0:s}, Weight: {1:.2f}%   Grade: {2:.2f}%" 
        for key, value in self.weightedItems.items():
            print(template.format(key, float(value[0]), float(value[1])))
    
    #Remove a weighted item
    def removeItem(self):
        self.listItems()
        self.weightedItems.pop(input("Enter the name of the item you would like to remove: "))
    
    #function calculates and returns final grade, calculated using each weighted item.
    def getFinalGrade(self):
        total = 0;
        for i in self.weightedItems:
            total+= float(self.weightedItems[i][0])/100*self.weightedItems[i][1]
        return total
        
