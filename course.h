//course.h

#include <string>
#include <vector>
using namespace std;

class course {
    
    public:
  
    string coursename;
    int coursenumber;

    
    //constructors
    course(string name) 
        : coursename(name) {};
    

    //Function calculates and returns final grade, calculated using each weighted item.
    //If total combined weight of all items exceeds 100%, returns 0 (invalid);
    double getFinalGrade();
        
    //Adds a weighted item to the list
    void addItem(string name);
    void addItem(string name, double grade, double weight);
    
    //Prints all weighted items
    void printItems();
    //*******************************************************
    private:
    
    //Subclass weighted item represents an assignment, test, or other weighted category.
    ///TO DO:    If a weighted item represents a category (ex. Assignments), 
    //          it can have weighted items inside it (ex Assignment 1). 
    class WeightedItem {
        public:
        
        friend class course;
        
        //Set weight of a weighted item
        void setWeight(double weight);
        
        //Set the name of a weighted item
        void setName (string name);
        
        
        private:
        
        //private data members:
        string itemname;
        double itemweight;
        double itemgrade;
      
        //constructors
        
            //Takes only name as a parameter
        WeightedItem(string name)
            :itemname(name) {};
            
            //Takes name, grade, and weight as parameters. Enter the weight as a decimal (50% should be entered as 0.5);
        WeightedItem(string name, double grade, double weight)
            :itemname(name), itemgrade(grade), itemweight(weight) {};
    };
    
    vector<WeightedItem> itemlist;
};
