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
  int quitter = 0;
  int loggedIn = 0;

  student *exampleStudent = new student("Julia", "Cotter", "cotterj@wit.edu", "abc123","CE", 2020);
  instructor *exampleInstructor = new instructor("Aaron", "Carpenter", "carpentera1@wit.edu", "oop123", "Assistant Professor", "DOBBS203");
  admin *exampleAdmin = new admin("Spongebob", "Squarepants", "squarepantss@wit.edu", "patrick", "Frycook", "Krusty Krab");
  course *exampleCourse = new course("APC", "CE", "Carpenter", "Summer 2019", 12345, 3, 1300, "MTR");

  students.push_back(exampleStudent);
  instructors.push_back(exampleInstructor);
  admins.push_back(exampleAdmin);
  courses.push_back(exampleCourse);

  do{
    student *currentUser_s;
    currentUser_s = new student();
    instructor *currentUser_i;
    currentUser_i = new instructor();
    admin *currentUser_a;
    currentUser_a = new admin();
    currentUser_s->role = "NULL";
    currentUser_i->role = "NULL";
    currentUser_a->role = "NULL";

    while(loggedIn!=1){
      cout << "-------------LOGIN MENU--------------" << endl;
      cout << "Enter email: ";
      cin >> userEmail;
      cout << endl << "Enter password: ";
      cin >> userPW;
      for(list<student*>::iterator i = students.begin(); i != students.end(); i++){
        if(userEmail == (*i)->email && userPW == (*i)->password){
          currentUser_s = (*i);
          loggedIn = 1;
          break;
        }
      }
      if(loggedIn == 1) break;
      for (list<instructor*>::iterator i = instructors.begin(); i != instructors.end(); i++){
        if(userEmail == (*i)->email && userPW == (*i)->password){
          currentUser_i = (*i);
          loggedIn = 1;
          break;
        }
      }
      if(loggedIn == 1) break;
      for(list<admin*>::iterator i = admins.begin(); i != admins.end(); i++){
        if(userEmail == (*i)->email && userPW == (*i)->password){
          currentUser_a = (*i);
          loggedIn = 1;
          break;
        }
      }
      if(loggedIn == 1) break;
    cout << "Invalid email or password." << endl;
    }

    if(currentUser_a->role == "Admin"){
      while(loggedIn == 1){  
        cout << endl << "---------------ADMIN MENU----------------" << endl;
        cout << endl << "Type 1 to check a roster, type 2 to edit a course, type 3 to edit a student, or type 9 to Logout." << endl;
        cin >> choice;
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
            delete currentUser_s;
            delete currentUser_i;
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
        cin >> choice;
        switch(choice){
          case 1:
            currentUser_s->courseRegister(courses);
            break;
          case 2:
            for(list<course*>::iterator i = courses.begin();i != courses.end(); i++){
              cout << (*i)->title << " " << (*i)->CRN << " " << (*i)->time << " " << (*i)->day << endl;
            }
            break;
          case 3:
            currentUser_s->checkSchedule();
            break;
          case 9:
            delete currentUser_s;
            delete currentUser_i;
            delete currentUser_a;
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
        cin >> choice;
        switch(choice){
          case 1:
            currentUser_i->checkRoster();
            break;
          case 2:
            currentUser_i->checkCourses();
            break;
          case 9:
            delete currentUser_s;
            delete currentUser_i;
            delete currentUser_a;
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