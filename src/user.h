#ifndef USER_H
#define USER_H

#include <string>
#include <list>
#include "course.h"

using namespace std;

class user{
  public:
    string firstName, lastName, email;
};

class student:public user{
  public:
    string major;
    list <course> regCourses;

  // constructor, destructor, and function prototypes
  // log in, check schedule, register for classes, log out
};

class instuctor:public user{
  public:
    string officeLoaction;
    list <course> courses;
    list <student> roster;

  // constructor, destructor, and function prototypes
  // log in, check roster, see their available courses, log out
};

class admin:public user{
  public:
    string officeLoction;

  // constructor, destructor, and function prototypes
  // Log in, check rosters, add/remove/edit courses, force add/drop on student profiles, log out
};

#endif