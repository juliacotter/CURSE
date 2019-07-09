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
  string 
  string userRole;
  do{
    cout << "-------------LOGIN MENU--------------" << ENDL;
    cout << "Enter email: ";
    cin >> userEmail;
    cout << "Enter password: ";
    cin << userPW;
    list<user>::iterator i = users.begin();
    for(i;i!=user.end();i++){
      (i).login(users);
    }
    userRole = user->role;
    userID = user->userID;
    if(userRole == "admin"){
      
    }
    else if(userRole == "student"){
    
    }
    else if(userRole == "instructor"){
    
    }
    else{

    }
    cout << endl << "---------------MAIN MENU----------------" << endl;
    cout << endl << "Type 1 to check your roster, type 2 to "
    switch(choice){
      case 0:
      if

    }
  } while ();
}