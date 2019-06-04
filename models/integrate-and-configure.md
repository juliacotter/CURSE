# Integrate and Configure Process Model

Basically the same project: https://web.csulb.edu/~mopkins/cecs493/sdsfinaledit-140325142607-phpapp01.pdf
-  Section 3.4 shows their algorithms for what each user can do
-  Section 3.5.1 shows their relational model
-  Section 3.5.3 shows all the tables used in their database
-  Section 3.6 shows GUI designs
-  Implements multiple semesters, times of courses, timetable, notices
I like the tables they used for their database and I will most likely use most of the attributes for Student, Subject (course), Current Semester, and Notices. 

Login entry box: https://smallguysit.com/index.php/2017/03/13/python-tkinter-password-entry-box/
-  Using Tkinter, a standard GUI package in Python
-  Implements login with the password displaying as asterisks when you type
I want to make sure when users login that their password is protected so I looked up a way to do so. This code implements this through the line:
password_box = Entry(main, show='*')
This source also introduced me to the GUI package Tkinter and how it’s implemented. I looked into the actual documentation and decided it was basic enough to use for this system. I liked the GUI designs from the previous source, such as the User Login, Add New User, Add New Subject, Edit Subject Details, and for the timetables.

Creating tables: https://github.com/dmnfarrell/tkintertable
-  Creates interactive spreadsheet-style tables
I was trying to figure out how I would be able to implement the timetables and came across this GUI library created by Damien Farrrell. I would make a mini calendar of the week that listed course each student like what the first source did.
This link explains how to use it: https://github.com/dmnfarrell/tkintertable/wiki/Usage
