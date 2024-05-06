import course as c

#Helper function checks if a value can be converted to a float: if not, asks for a new valid input
def floatify(number_to_floatify):
    try:
        return float(number_to_floatify)
    except:
        new_number = input("Invalid input, please enter a number: ")
        return floatify(new_number)

def printcommands():
    print("""
    i: Add a new addItem
    r: Remove an item
    l: List all items, each with their grade and weight
    g: Return final grade based on all items added
    h: help (lists valid commands)
    q: quit
    """)

testcourse = input("Enter course name: ")
testcourse = c.Course(testcourse)

#Print commands at the beginning
command = 'h'
#Execute commands and get new input (q to quit)
while command != 'q':
    #i: add a new item
    if command == 'i':
        testcourse.addItem(input("Enter item name: "), floatify(input("Enter item weight%: ")), floatify(input("Enter item grade% ")))
    #r: remove an item
    elif command == 'r':
        testcourse.removeItem()
    #l: list all items, each with their grade and weight
    elif command == 'l':
        testcourse.listItems()
    #g: return final grade based on all items added
    elif command == 'g':
        print("Final grade for " + testcourse.name + ": " + str(testcourse.getFinalGrade()) + "%")
    #help
    elif command == 'h':
        printcommands()
    #q: quit
    elif command == 'q':
        pass
    #Any other input (invalid command)
    else:
        
        print ("INVALID COMMAND, PLEASE TRY AGAIN")
        print ("Valid commands: ")
        printcommands()
    command = input("Input command character ('h' to list all commands): ")

#End of program
print("END OF PROGRAM!")
print(r"""                
                        (`.
                        \ `.
                        )  `._..---._
      \'.       __...---`         o  )
       \ `._,--'           ,    ___,'
        ) ,-._          \  )   _,-'
       /,'    ``--.._____\/--''
      """)


'''
PROPOSED UPDATES:
-Rest-of-course-grade option when inputting assignment weight??
-Make a globabl variable of totalWeight
-addGrade will change a grade if an assignment with that name already exists.
  Consider making two commands, or saying "that assignment already exists, want to change it?"
-The total grade function right now assumes you get 0 in the rest of the course.
  Consider changing it to divide by totalWeight instead of always 100.
  Maybe you could make a separate function that does what this one does now, if you find it useful.
-In the addGrade function, nterrupt when you enter a weight that would make the total exceed 100%. 
  As of now it still asks for a grade percent before saying error, even if the weight is invalid.
'''
