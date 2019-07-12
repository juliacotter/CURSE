#include <iostream>
#include <string>
#include <list>
#include "course.h"
#include "user.h"

using namespace std;

list <student*> students;
list <instructor*> instructors;
list<admin*> admins;
list<course*> courses;

int main(){
  int choice = 0;
  string userEmail, userPW;
  string userRole;
  student *currentUser_s;
  instructor *currentUser_i;
  admin *currentUser_a;
  int quitter = 0;
  int loggedIn = 0;

  student *exampleStudent = new student("Julia", "Cotter", "cotterj@wit.edu", "abc123","CE", 2020);
  students.push_back(exampleStudent);

  do{
    cout << "-------------LOGIN MENU--------------" << endl;
    cout << "Enter email: ";
    cin >> userEmail;
    cout << endl << "Enter password: ";
    cin >> userPW;

    while(loggedIn!=1){
      for(list<student*>::iterator i = students.begin(); i != students.end(); i++){
        if(userEmail == (*i)->email && userPW == (*i)->password)
          currentUser_s = (*i);
          loggedIn = 1;
          break;
      }
      if(loggedIn == 1) break;
      for (list<instructor*>::iterator i = instructors.begin(); i != instructors.end(); i++){
        if(userEmail == (*i)->email && userPW == (*i)->password)
          currentUser_i = (*i);
          loggedIn = 1;
          break;
      }
      if(loggedIn == 1) break;
      for(list<admin*>::iterator i = admins.begin(); i != admins.end(); i++){
        if(userEmail == (*i)->email && userPW == (*i)->password)
          currentUser_a = (*i);
          loggedIn = 1;
          break;
      }
      if(loggedIn == 1) break;
    cout << "Invalid email or password." << endl;    
    }

    if(currentUser_a->role == "Admin"){
      while(loggedIn == 1){  
        cout << endl << "---------------ADMIN MENU----------------" << endl;
        cout << endl << "Type 1 to check a roster, type 2 to edit a course, type 3 to edit a student, or type 9 to Logout." << endl;
        switch(choice){
          case 1:
            currentUser_a->checkRoster();
            break;
          case 2:
            currentUser_a->editCourse();
            break;
          case 3:
            currentUser_a->editStudent(students, courses);
            break;
          case 9:
            delete currentUser_a;
            loggedIn = 0;
            break;
          default:
            cout << "Sorry, that was not one of the choices. Please try again." << endl;
            break;
        }
      }
    }
    else if(currentUser_s->role == "Student"){
      while(loggedIn == 1){
        cout << endl << "---------------STUDENT MENU----------------" << endl;
        cout << endl << "Type 1 to enter course registration, tpye 2 to check all available courses, type 3 to check your schedule, or type 9 to Logout." << endl;
        switch(choice){
          case 1:
            currentUser_s->courseRegister(courses);
            break;
          case 2:
            for(list<course*>::iterator i = courses.begin();i != courses.end(); i++){
              cout << (*i)->title << " " << (*i)->CRN << " " << (*i)->time.tm_hour << " " << (*i)->day.tm_wday << endl;
            }
            break;
          case 3:
            currentUser_s->checkSchedule();
            break;
          case 9:
            delete currentUser_s;
            loggedIn = 0;
            break;
          default:
            cout << "Sorry, that was not one of the choices. Please try again." << endl;
            break;
        }
      }
    }
    else if(currentUser_i->role == "Instructor"){
      while(loggedIn == 1){
          cout << endl << "---------------INSTRUCTOR MENU----------------" << endl;
        cout << endl << "Type 1 to check a roster, type 2 to check your courses, or type 9 to Logout." << endl;
        switch(choice){
          case 1:
            currentUser_i->checkRoster();
            break;
          case 2:
            currentUser_i->checkCourses();
            break;
          case 9:
            delete currentUser_i;
            loggedIn = 0;
            break;
          default:
            cout << "Sorry, that was not one of the choices. Please try again." << endl;
            break;
        }
      }
    }
    else{
      cout << "Sorry, it seems you are an unauthorized user. Please check with your Administrator to gain privileges." << endl;
      break;
    }
  } while (quitter == 0);
  return 0;
}