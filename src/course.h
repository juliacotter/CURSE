#ifndef COURSE_H
#define COURSE_H

#include <string>
#include <list>
#include "user.h"

using namespace std;

class course{
  public:
    string title, department, instructor, semester;
    int CRN, credits;
    list<student> regStudents;

    // constructor, destructor, and function prototypes
};

#endif