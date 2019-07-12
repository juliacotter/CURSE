#ifndef USER_H
#define USER_H

#include <string>
#include <list>

using namespace std;

class course;

class user{
  public:
    int wNumber;
    string firstName, lastName, email, password, role;

    user(string fn, string ln, string em, string pw):firstName(fn), lastName(ln), email(em), password(pw){}
};

class student:public user{
  public:
    string major;
    int graduationYear;
    list <int*> regCourses;

    student();
    student(string fn, string ln, string em, string pw, string mj, int gy):user(fn, ln, em, pw), major(mj), graduationYear(gy) {
      role = "Student";
    }

  // log in, check schedule, register for classes, log out
    void checkSchedule();
    void courseRegister(list<course*> &courses);
};

class instructor:public user{
  public:
    string title, officeLoaction;
    list <int> offeredCourses;
    list <string> roster;

    instructor();
    instructor(string fn, string ln, string em, string pw, string t, string ol):user(fn, ln, em, pw), title(t), officeLoaction(ol) {
      role = "Instructor";
    }
    // log in, check roster, see their available courses, log out
    void checkRoster();
    void checkCourses();
};

class admin:public user{
  public:
    string title, officeLoction;

    admin();
    admin(string fn, string ln, string em, string pw, string t, string ol):user(fn, ln, em, pw), title(t), officeLoction(ol) {
      role = "Admin";
    }

  // Log in, check rosters, add/remove/edit courses, force add/drop on student profiles, log out
    void checkRoster();
    void editCourse();
    void editStudent(list<student*> &students, list<course*> &courses);
};

#endif // USER_H