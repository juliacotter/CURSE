#ifndef COURSE_H
#define COURSE_H

#include <string>
#include <list>
#include <time.h>
#include "user.h"

using namespace std;

class course{
  public:
    string title, department, instructor, semester;
    int CRN, credits;
    struct tm time, day;
    list<student> regStudents;

    course(string t, string d, string i, string s, int crn, int c, struct tm tm, struct tm dy):title(t), department(d), instructor(i), semester(s), CRN(crn), credits(c), time(tm), day(dy){};
};

#endif