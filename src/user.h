#ifndef USER_H
#define USER_H

#include <string>
#include <list>
#include "course.h"

using namespace std;

class user{
  public:
    int wNumber;
    string firstName, lastName, email, password, role;

    user(string fn, string ln, string em):firstName(fn), lastName(ln), email(em){}

    string login(list <student> Students, list <instructor> Instructors, list<admin> Admins);
    void logout(string currentUser);
};

class student:public user{
  public:
    string major;
    int graduationYear;
    list <course> regCourses;

    student(string fn, string ln, string em, string mj, int gy):user(fn, ln, em), major(mj), graduationYear(gy) {
      role = "Student";
    }

  // log in, check schedule, register for classes, log out
    void checkSchedule();
    void courseRegister();
};

class instructor:public user{
  public:
    string title, officeLoaction;
    list <course> offeredCourses;
    list <student> roster;

    instructor(string fn, string ln, string em, string t, string ol):user(fn, ln, em), title(t), officeLoaction(ol) {
      role = "Instructor";
    }
    // log in, check roster, see their available courses, log out
    void checkRoster();
    void checkCourses();
};

class admin:public user{
  public:
    string title, officeLoction;

    admin(string fn, string ln, string em, string t, string ol):user(fn, ln, em), title(t), officeLocation(ol) {
      role = "Admin";
    }

  // Log in, check rosters, add/remove/edit courses, force add/drop on student profiles, log out
    void checkRoster();
    void editCourse();
    void editStudent(list<student> Students, list<course> Courses);
};

#endif