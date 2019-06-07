# Integrate and Configure Process Model

## Requirements
The requirements for the CURSE system include:
- The capability of 100 students that can each register and view courses that are available, as well as their own schedule.
- 10 instructors that can view available courses and the roster for each of their classes.
- 1 admin that has access to read and edit all information within the database. (courses/users/instructors... etc)
- Courses, including the CRN code, name, time, description, and instructor for each course.

## System and Software Design
A similar system was found here:
https://web.csulb.edu/~mopkins/cecs493/sdsfinaledit-140325142607-phpapp01.pdf
We plan to implement this system to facilitate the design process. 
Although we might not copy the design exactly as it is shown, the basic framework is set for us to work with.
The parts we wish to implement include:
-  Section 3.4 shows their algorithms for what each user can do
-  Section 3.5.1 shows their relational model
-  Section 3.5.3 shows all the tables used in their database
-  Section 3.6 shows GUI designs
-  Implements multiple semesters, times of courses, timetable, notices<br>
-  Similar attributes to the classes given within the database

In order to assign users the privileges for their specific class, they must sign-in.
The system for a Login entry box was found here:
https://smallguysit.com/index.php/2017/03/13/python-tkinter-password-entry-box/
The design for this Login entry box includes:
-  Using Tkinter, a standard GUI package in Python
-  Implements login with the password displaying as asterisks when you type<br>
I want to make sure when users login that their password is protected so I looked up a way to do so. This code implements this through the line:<br>
password_box = Entry(main, show='*')<br>
This source also introduced me to the GUI package Tkinter and how it’s implemented. I looked into the actual documentation and decided it was basic enough to use for this system. I liked the GUI designs from the previous source, such as the User Login, Add New User, Add New Subject, Edit Subject Details, and for the timetables.

In order to build the database, we found a system for creating tables: 
https://github.com/dmnfarrell/tkintertable
-  Creates interactive spreadsheet-style tables<br>
I was trying to figure out how I would be able to implement the timetables and came across this GUI library created by Damien Farrell. I would make a mini calendar of the week that listed course each student like what the first source did. <br>
This link explains how to use it: https://github.com/dmnfarrell/tkintertable/wiki/Usage

## Implementation and Unit Testing
To begin implementing the parts for this system, we must first create each individual unit and ensure its functionality.
- For the database, we must make sure that the attributes include all information necessary for the other units to function properly. Since the classes found above include the attributes necessary, we plan to model the tables in a similar manner. Tests must be done to ensure that the attributes for each user can be identified quickly.
- To implement the User login, we must first test that the unit properly hides the users password and that the data entered can then be compared with some value later.
- Finally, we need to be able to pull, edit, and move information from the database. This can be tested by adding dummy data and trying to manpulate the data on a small scale.

## Integration and System Testing
From this point, we must implement each part one by one.
Since we unit tested the database to make sure that it can properly manipulate data, we must:
- Implement the user interface to allow easy manipulation of that data. 
- After the user interface is in place and can do everything it is required, we can implement the different roles based on the user that is signed in. This will restrict some users from some functions based on their attributes. 
- Onces that works as required, we can implement the Login. It is important to make sure that the password being entered can be compared to a saved value within the database then giving each user its allowed actions.
- A final test should be performed to make sure everything works as intended before moving to the final version.
