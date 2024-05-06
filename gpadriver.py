import course as c

'''
# Testing the course class
Math = c.Course("Math")
Math.addItem("Assignments", 50, 80)
Math.addItem("Exams", 50, 90)
print(str(Math.getFinalGrade()) + '%')
'''

#Driver

def printcommands():
    print("""
    i: Add a new addItem
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
        testcourse.addItem(input("Enter item name: "), input("Enter item weight%: "), input("Enter item grade% "))
    #l: list all items, each with their grade and weight
    elif command == 'l':
        pass
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
    command = input("Input command character: ")

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
