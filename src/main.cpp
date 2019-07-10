#include <iostream>
#include <string>
#include <list>
#include "user.h"
#include "course.h"

list <user> users;
list<course> courses;

int main(){
  int choice = 0;
  string userEmail, userPW;
  string userRole;
  int quitter = 0;
  int loggedIn = 0;
  do{
    cout << "-------------LOGIN MENU--------------" << ENDL;
    cout << "Enter email: ";
    cin >> userEmail;
    cout << endl << "Enter password: ";
    cin << userPW;
    list<user>::iterator i = users.begin();
    for(i;i!=user.end();i++){
      (i).login(users);
    }

    currentUser.userRole = user->role;
    currentUser.userID = user->userID;
    loggedIn = 1;
    if(currentUser.userRole == "admin"){
      while(loggedIn == 1){  
        cout << endl << "---------------ADMIN MENU----------------" << endl;
        cout << endl << "Type 1 to check a roster, type 2 to edit a course, type 3 to edit a student, or type 9 to Logout." << endl;
        switch(choice){
          case 1:
            currentUser.checkRoster();
            break;
          case 2:
            currentUser.editCourse();
            break;
          case 3:
            currentUser.editStudent();
            break;
          case 9:
            currentUser.logout();
            currentUser.userRole = NULL;
            loggedIn = 0;
            break;
          default:
            cout << "Sorry, that was not one of the choices. Please try again." << endl;
            break;
        }
      }
    }
    else if(currentUser.userRole == "student"){
      while(loggedIn == 1){
        cout << endl << "---------------STUDENT MENU----------------" << endl;
        cout << endl << "Type 1 to enter course registration, type 2 to check your schedule, or type 9 to Logout." << endl;
        switch(choice){
          case 1:
            currentUser.courseRegister();
            break;
          case 2:
            currentUser.checkSchedule();
            break;
          case 9:
            currentUser.logout();
            currentUser.userRole = NULL;
            loggedIn = 0;
            break;
          default:
            cout << "Sorry, that was not one of the choices. Please try again." << endl;
            break;
        }
      }
    }
    else if(currentUser.userRole == "instructor"){
      while(loggedIn == 1){
          cout << endl << "---------------INSTRUCTOR MENU----------------" << endl;
        cout << endl << "Type 1 to check a roster, type 2 to check your courses, or type 9 to Logout." << endl;
        switch(choice){
          case 1:
            currentUser.checkRoster();
            break;
          case 2:
            currentUser.checkCourses();
            break;
          case 9:
            currentUser.logout();
            currentUser.userRole = NULL;
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
}