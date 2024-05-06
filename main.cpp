#include <iostream>
#include <cassert>
#include "course.h"

using namespace std;

void printCommands();

course TestCourse(TestCourse);

int main() {
    
    ///Intro text
    printCommands();
    
    char command;
    cin >> command;
    while (command != 'q') {
        

        
        if (command == 'i') {
            ///Item: Enter item with name, grade, weight
            string name;
            double grade, weight;
            cout << "Enter item name: ";
            cin >> name;
            cout << "Enter item grade: ";
            cin >> grade;
            cout << "Enter item weight: ";
            cin >> weight;
            TestCourse.addItem(name, grade, weight);

        }
        ///List: Print all items, each with their grade and weight
        else if (command == 'l') {
            TestCourse.printItems();
        }
        ///Calculate: calculate final grade based on all items currently input
        else if (command == 'g') {
            cout << "Final Grade: " << TestCourse.getFinalGrade() << "%" << endl;
        }
        else if (command == 'h') {
            printCommands();
        }
        //All other command inputs are invalid
        else {
            cout << "INVALID COMMAND, TRY AGIAN" << endl;
        }
        //read next command
        cin >> command;
    }
    
    return 0;
}

void printCommands() {
    cout << "COMMANDS: " << endl;
    cout << "i: Add a new item" << endl;
    cout << "l: List all items, each with their grade and weight" << endl;
    cout << "g: Return final grade based on all items added" << endl;
}