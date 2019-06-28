#ifndef USER_H
#define USER_H

#include <string>
#include <list>
#include "course.h"

using namespace std;

class user{
  public:
    string uID, firstName, lastName, email, password, role;

    string login(list <student *> &Students, list <instructor *> &Instructors, list<admin *> &Admins);
    void logout();
};

class student:public user{
  public:
    string major;
    list <course> regCourses;

    student(string fn, string ln, string em, string mj):firstName(fn), lastName(ln), email(em), major(mj);

  // log in, check schedule, register for classes, log out
    void checkSchedule();
    void courseRegister();
};

class instructor:public user{
  public:
    string officeLoaction;
    list <course> courses;
    list <student> roster;

    instructor(string fn, string ln, string em, string ol):firstName(fn), lastName(ln), email(em), officeLoaction(ol);
  // log in, check roster, see their available courses, log out
    void checkRoster();
    void checkCourses();
};

class admin:public user{
  public:
    string officeLoction;

    admin(string fn, string ln, string em, string ol):firstName(fn), lastName(ln), email(em), officeLoaction(ol);

  // Log in, check rosters, add/remove/edit courses, force add/drop on student profiles, log out
    void checkRoster();
    void editCourse();
    void editStudent();
};

#endif