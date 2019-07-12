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

    user(){};
    user(string fn, string ln, string em, string pw):firstName(fn), lastName(ln), email(em), password(pw){}
    ~user(){}
};

class student:public user{
  public:
    string major;
    int graduationYear;
    int regCourses[5] = {};

    student(){
      cout << "A student has been created." << endl;
    };
    student(string fn, string ln, string em, string pw, string mj, int gy):user(fn, ln, em, pw), major(mj), graduationYear(gy) {
      role = "Student";
    }
    ~student(){
      cout << "A student has been deleted." << endl;
    };

  // log in, check schedule, register for classes, log out
    void checkSchedule();
    void courseRegister(list<course*> &courses);
};

class instructor:public user{
  public:
    string title, officeLoaction;
    list <int> offeredCourses;
    list <string> roster;

    instructor(){
      cout << "An instructor has been created." << endl;
    };
    instructor(string fn, string ln, string em, string pw, string t, string ol):user(fn, ln, em, pw), title(t), officeLoaction(ol) {
      role = "Instructor";
    }
    ~instructor(){
      cout << "An instructor has been deleted." << endl;
    };
    // log in, check roster, see their available courses, log out
    void checkRoster();
    void checkCourses();
};

class admin:public user{
  public:
    string title, officeLoction;

    admin(){
      cout << "An admin has been created." << endl;
    };
    admin(string fn, string ln, string em, string pw, string t, string ol):user(fn, ln, em, pw), title(t), officeLoction(ol) {
      role = "Admin";
    }
    ~admin(){
      cout << "An admin has been deleted." << endl;
    };

  // Log in, check rosters, add/remove/edit courses, force add/drop on student profiles, log out
    void checkRoster();
    void editCourse();
    void editStudent(list<student*> &students, list<course*> &courses);
};

#endif // USER_H