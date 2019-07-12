#include <iostream>
#include <string>
#include <list>
#include "user.h"

// class functions

// Julia
 void student::checkSchedule(){
  int zeroCounter = 0;
  for(int i = 0; i < 5; i++){
    if(this->regCourses[i] == 0){
      zeroCounter++;
      if(zeroCounter == 5){
        cout << "You are not registered for any courses." << endl;
        zeroCounter = 0;
        return;
      }
      continue;
    }
    cout << "CRN: " << this->regCourses[i] << endl;
    
  }
}

// Julia
void student::courseRegister(list<course*> &courses){
    int dropAdd, crnInput = 0;
    cout << "Type 1 to Add and 2 to Drop." << endl;
    cin >> dropAdd;
    if(dropAdd == 1){
      for(int i = 0; i < 5; i++){
        if(this->regCourses[i] == 0){
          cout << "Please enter the CRN for the course you wish to register." << endl;
          cin >> crnInput;
          this->regCourses[i] = crnInput;
          for(list<course*>::iterator i = courses.begin(); i != courses.end(); i++){
            if((*i)->CRN == crnInput){
              (*i)->regStudents.push_back(this->email);
              cout << "You have been enrolled in the course." << endl;
              return;
            }
          }
        }
      }
      cout << "Sorry, you have registered for too many courses." << endl;
      return;            
      
    }
    /*else if(dropAdd == 2){
      if(this->_regCourses.size() == 0){
        cout << "Sorry, you have not registered for any courses yet." << endl;
        return;
      }
      else{
        cout << "Please enter the CRN you wish to remove." << endl;
        cin >> crnInput;
        for(list<course*> i = this->regCourses.begin(); i != this->regCourses.end(); i++){
          for(list<course*> j = courses.begin(); i != courses.end(); j++){
            if((*i)->CRN == crnInput && (*j)->_regStudents->wNumber == this->wNumber){
                (*j)->regStudents.erase(*j);
                this->regCourses.erase(*i);
                cout << "Course has been dropped." << endl;
                return;
            }
          }
        }
      }
    }*/
    else{
      cout << "Sorry, that was not one of the options." << endl;
    }
}

//Wilson
void instructor::checkRoster(){
/*   int crnInput;
  cout << "Please enter the CRN for the course roster you wish to view." << endl;
  cin >> crnInput;
  assigned = false;
  for(list<course>::iterator i = this->regCourses.begin(); i != this->regCourses.end(); i++){
    if(i == crnInput){
      assigned = true;
      break;
    }
  }
  if (assigned == true){
    cout << "The students in this course are :" << endl;
    for(int j = 0; j < studentsinCRN.size(); j++){
        cout << studentsinCRN[i] << endl;
      }
      cout << "~END OF COURSE LIST~" << endl;
      return;
  }
  else{
    cout << "Sorry, you are not assigned to any courses with that CRN." << endl;
    return;
  } */
}

// Julia
void instructor::checkCourses(){
  /* for(list<course*>::iterator i = this->offeredCourses.begin(); i != this->offeredCourses.end(); i++){
    cout << (*i)->title << ": " << (*i)->time.tm_hour << (*i)->time.tm_min << endl;
  } */
}

//Wilson
void admin::checkRoster(){
  /* int crnInput;
  cout << "Please enter the CRN for the course roster you wish to view." << endl;
  cin >> crnInput;
  for(int i = allCourses.begin(); i != allCourses.end(); i++){
    if(i == crnInput){
    cout << "The students in this course are :" << endl;
      for(int j = 0; j < studentsinCRN.size(); j++){
        cout << studentsinCRN[i] << endl;
      }
      cout << "~END OF COURSE LIST~" << endl;
      return;
    }
  }
  cout << "Sorry, no course was found with that CRN." << endl;   */
}

// Wilson
void admin::editCourse(){
  /* int adminChoice, crnInput;
  string courseName, courseDays;
  cout << "Type 1 to add a new course, 2 to remove a course, and 3 to edit an existing course." << endl;
  cin >> adminChoice;
  switch(adminChoice){
    case 1:
      cout << "Please type the CRN, Course Name, and days of the course you wish to add." << endl;
      cin >> crnInput >> courseName >> courseDays;
      for(int i = allCourses.begin(); i != allCourses.end(); i++){
        if(i == crnInput){
          cout << "Sorry, a course has already been created with that unique identifier." << endl;
          break;
        }
      }
      allCourses.pushback(crnInput);
      allCourses.back()->cName = courseName;
      allCourses.back()->cDays = courseDays;
      cout << "The course has been created." << endl;
      break;
    case 2:
      cout << "Please enter the CRN you wish to remove." << endl;
        cin >> crnInput;
        for(int i = allCourses.begin(); i != allCourses.end(); i++){
          if(i == crnInput){
              allCourses.erase();
              cout << "Course has been dropped." << endl;
              break;
          }   
        }
        cout << "Sorry, a course was not found with that CRN." << endl;
        break;
    case 3:
       cout << "Please enter the CRN you wish to edit." << endl;
        cin >> crnInput;
        for(int i = allCourses.begin(); i != allCourses.end(); i++){
          if(i == crnInput){
            cout << "What would you like to edit?" << endl;
            break;
          }
        }
        cout << "Sorry, a course was not found with that CRN." << endl;
        break;
    default:
      cout << "Sorry, that was not one of the options." << endl;
      break;
  } */
}

// Julia
void admin::editStudent(list<student*> &students, list<course*> &courses){
  /* int wInput, choice, crnInput = 0;
  cout << "Enter W number for student: ";
  cin >> wInput;
  // veiw student profile and schedule
  cout << "Select 1 to add course to student\nSelect 2 to drop student from course\n";
  cin >> choice;

  switch(choice){
    case 1:
      cout << "Enter the CRN you wish to add: " << endl;
      cin >> crnInput;
      // replace with SQL later
      for(list<student*>::iterator i = students.begin(); i != students.end(); i++){
        for(list<course*>::iterator j = courses.begin(); j != courses.end(); j++){
          if((*i)->wNumber == wInput && (j)->CRN == crnInput){
            (*i)->regCourses.push_back(*j);
            (*j)->regStudents.push_back(*i);
            cout << "Course has been added." << endl;
            return;
          }
        }
      }
      break;
    case 2:
      cout << "Enter the CRN you wish to drop: " << endl;
      cin >> crnInput;
      // replace with SQL later
      for(list<student*>::iterator i = students.begin(); i != students.end(); i++){
        if((*i)->wNumber == wInput){
          for(list<course*>::iterator j = (*i)->regCourses.begin(); j != (*i)->regCourses.end(); j++){
            if((*j)->CRN == crnInput){  
              (*i)->regCourses.erase(*j);
              for (list<course*>::iterator k = courses.begin(); k != courses.end(); k++){
                if ((*k)->CRN == crnInput){
                  for(list<student*>::iterator l = (*k)->regStudents.begin(); l != (*k)->regStudents.end(); l++){
                    (*k)->regStudents.erase(*l);
                    cout << "Course has been dropped." << endl;
                    return;
                  }
                }
              }
            }
          }
        }
      }
      break;
  } */
  
}