#ifndef COURSE_H
#define COURSE_H

#include <string>
#include <list>
#include <time.h>

using namespace std;

class course{
  public:
    string title, department, instructor, semester, day;
    int CRN, credits, time;
    list<string> regStudents;

    course();
    course(string t, string d, string i, string s, int crn, int c, int tm, string dy):title(t), department(d), instructor(i), semester(s), CRN(crn), credits(c), time(tm), day(dy){};
};

#endif // COURSE_H