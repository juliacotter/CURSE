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
            regCourse.pushback(crnInput);
            cout << "You have been enrolled in the course." << endl;
        }
    }
    else if(dropAdd == 2){
      if(student->regCourses.size() == 0){
        cout << "Sorry, you have not registered for any courses yet." << endl;
        return;
      }
      else{
        cout << "Please enter the CRN you wish to remove." << endl;
        cin >> crnInput;
        for(int i = regCourses.begin(); i != regCourses.end(); i++){
          if(i == crnInput){
              regCourses.erase();
              cout << "Course has been dropped." << endl;
              return;
          }   
        }
      }
    }
    else{
      cout << "Sorry, that was not one of the options." << endl;
    }
}
//Wilson
void instructor::checkRoster(){
  int crnInput;
  cout << "Please enter the CRN for the course roster you wish to view." << endl;
  cin >> crnInput;
  for(int i = instructor->regCourses.begin(); i != instructor->regCourses.end(); i++){
    if(i == crnInput){
      cout << "The students in this course are :" << endl;
      for(int j = 0; j < studentsinCRN.size(); j++){
        cout << studentsinCRN[i] << endl;
      }
      cout << "~END OF COURSE LIST~" << endl;
      return;
    }
  }
  cout << "Sorry, you are not assigned to any courses with that CRN." << endl;
  return;
}

// Julia
void instructor::checkCourses(){

}
//Wilson
void admin::checkRoster(){
  int crnInput;
  cout << "Please enter the CRN for the course roster you wish to view." << endl;
  cin >> crnInput;
  for(int i = allCourses.begin(); i != allCourses.end(); i++){
    if(i == crnInput){
    cout << "The students in this course are :" << endl;
      for(int j = 0; j < studentsinCRN.size(); j++){
        cout << studentsinCRN[i] << endl;
      }
      cout << "~END OF COURSE LIST~" << endl;
      return;
    }
  }
  cout << "Sorry, no course was found with that CRN." << endl;  
}
// Wilson
void admin::editCourse(){
  int adminChoice, crnInput;
  string courseName, courseDays;
  cout << "Type 1 to add a new course, 2 to remove a course, and 3 to edit an existing course." << endl;
  cin >> adminChoice;
  switch(adminChoice){
    case 1:
      cout << "Please type the CRN, Course Name, and days of the course you wish to add." << endl;
      cin >> crnInput >> courseName >> courseDays;
      for(int i = allCourses.begin(); i != allCourses.end(); i++){
        if(i == crnInput){
          cout << "Sorry, a course has already been created with that unique identifier." << endl;
          break;
        }
      }
      allCourses.pushback(crnInput);
      allCourses.back()->cName = courseName;
      allCourses.back()->cDays = courseDays;
      cout << "The course has been created." << endl;
      break;
    case 2:
      cout << "Please enter the CRN you wish to remove." << endl;
        cin >> crnInput;
        for(int i = allCourses.begin(); i != allCourses.end(); i++){
          if(i == crnInput){
              allCourses.erase();
              cout << "Course has been dropped." << endl;
              break;
          }   
        }
        cout << "Sorry, a course was not found with that CRN." << endl;
        break;
    case 3:
       cout << "Please enter the CRN you wish to edit." << endl;
        cin >> crnInput;
        for(int i = allCourses.begin(); i != allCourses.end(); i++){
          if(i == crnInput){
            cout << "What would you like to edit?" << endl;
            break;
          }
        }
        cout << "Sorry, a course was not found with that CRN." << endl;
        break;
    default:
      cout << "Sorry, that was not one of the options." << endl;
      break;
  }
}

// Julia
void admin::editStudent(){

}