//course.cc
#include "course.h"
#include <iostream>

//Public member function adds an item to the list of weighted items

void course::addItem(string name) {
    WeightedItem item(name);
    this->itemlist.push_back(item);
}

void                course::addItem(string name, double grade, double weight) {
    WeightedItem item(name, grade, weight);
    this->itemlist.push_back(item);
}

//Set weight of a weighted item
void course::WeightedItem::setWeight(double weight) {
    itemweight = weight;
}

//Set the name of a weighted item
void course::WeightedItem::setName (string name) {
    itemname = name;
}

//Calculates and returns the course's final grade based on all weighted items
double course::getFinalGrade() {
    double total = 0; //Total 
    int items = 0.0; //Number of weighted items used in the calculation
    double totalweight;
    
    for (int i = 0; i < itemlist.size(); ++i) {
        if (itemlist[i].itemgrade && itemlist[i].itemweight) {
            //Adds each item's grade multiplied by its weight percentage to the total final grade
            total += ((itemlist[i].itemweight/100) * itemlist[i].itemgrade);
            //Count the total weight of all items (if >= 100, calculation is invalid);
            totalweight += itemlist[i].itemweight;
            //Count the total number of items used in the calculation
            items += 1.0;
        }
    }
    //Check to make sure total weight is valid (= 100%). 
    //If less than 100%, will still return but will print error message.
    //If greater than 100%, returns 0.
    if (totalweight <= 100) {
        if (totalweight < 100) {
            cout << "ITEMS MISSING (total weight < 100%)" << endl;
        }
        return (total);
    }
    else {
        cout << "TOTAL WEIGHT EXCEEDS 100%" << endl;
        return 0;
    }
}

    
//Prints all weighted items
void course::printItems() {
    for (int i = 0; i < itemlist.size(); ++i) {
        cout << itemlist[i].itemname << "- Grade: " << itemlist[i].itemgrade << ", Weight: " << (itemlist[i].itemweight) << "%" << endl; 
    }
}



/*
TO DO:
    Function to remove items from a course
    Functions to change the weight, grade, or name of an item
    Change vector to a faster data structure; Linked list, binary search tree, or map
    Use assert (or if statements) to check for invalid inputs
*/