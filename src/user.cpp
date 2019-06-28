#include "user.h"
#include <string>
#include <iostream>

using namespace std;

// class functions

// Julia
string user::login(list <student> &Students, list <instructor> &Instructors, list<admin> &Admins){
  string em, pw, currentUser;
  cout << "Enter email: ";
  cin.ignore();
  getline(cin, em);
  cout << "Eneter password: ";
  getline(cin, pw);
  
  for(list<student>::iterator i = Students.begin(); i != Student.end(); i++){
    if(em == (*i)->email && pw == (*i)->password){
      currentUser = (*i)->uID;
      return currentUser, (*i)->role;
    }
    else{
      cout << "Invalid email or password.";
    }
  }
}

// Julia
void user::logout(string currentUser){
  currentUser = NULL;
  return "Logging out...";
}

// Julia
void student::checkSchedule(){

}

void student::courseRegister(){
    int dropAdd = 0;
    string crnInput;
    cout << "Type 1 to Add and 2 to Drop." << endl;
    cin >> dropAdd;
    if(dropAdd == 1){
        if(student->regCourses.size() >= 5){
            cout << "Sorry, you have registered for too many courses." << endl;
            return;            
        }
        else{
            cout << "Please enter the CRN you wish to add." << endl;
            cin >> crnInput;
            for(int i = regCourses.begin(); i != regCourse.end(); i++){
                if(i == crnInput){
                    regCourses.erase();
                    cout << "Course has been dropped." << endl;
                    return;
                }   
            }
            cout << "" << endl;
        }
    }
    else if(dropAdd == 2){
        
    }
}
//Wilson
void instructor::checkRoster(){

}

// Julia
void instructor::checkCourses(){

}
//Wilson
void admin::checkRoster(){
// Wilson
}

void admin::editCourse(){

}

// Julia
void admin::editStudent(){

}