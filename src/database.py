import sqlite3
import os

filepath = os.path.abspath("CURSE/src/db/assignment7.db")
connection = sqlite3.connect(filepath)
crsr = connection.cursor()

users = ["STUDENT", "INSTRUCTOR", "ADMIN"]

create_table = """CREATE TABLE IF NOT EXISTS COURSE(
  CRN INT PRIMARY KEY NOT NULL,
  TITLE TEXT NOT NULL,
  DEPT CHAR(4) NOT NULL,
  INSTRUCTOR INT,
  TIME INT NOT NULL,
  DAY TEXT NOT NULL,
  SEMESTER TEXT NOT NULL,
  YEAR INT NOT NULL,
  CREDITS INT NOT NULL,
  FOREIGN KEY (INSTRUCTOR) REFERENCES INSTRUCTOR(ID)
);"""
crsr.execute(create_table)

def addUser(userType, user):
  query = "INSERT INTO {} VALUES(?, ?, ?, ?, ?, ?);".format(users[userType])
  add = crsr.execute(query, (user["ID"], user["NAME"], user["SURNAME"], user["GRADYEAR"], user["MAJOR"], user["EMAIL"]))
  connection.commit()

def removeUser(userType, userID):
  query = "DELETE FROM {} WHERE ID = ?;".format(users[userType])
  remove = crsr.execute(query, (userID, ))
  connection.commit()

def updateUser(userType, userID, field, userUpdate):
  query = "UPDATE {} SET {} = ? WHERE ID = ?;".format(users[userType], field)
  update = crsr.execute(query, (userUpdate, userID))
  connection.commit()

def addCourse(course):
  query = "INSERT INTO COURSE VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);"
  add = crsr.execute(query, (course["CRN"], course["TITLE"], course["DEPT"], course["INSTRUCTOR"], course["TIME"], course["DAY"], course["SEMESTER"], course["YEAR"], course["CREDITS"]))
  connection.commit()

choice = 0
while choice != 7:
  print('----------Main Menu----------')
  choice = input('Select 1 to print lists\nSelect 2 to add user\nSelect 3 to remove user\nSelect 4 to update user\nSelect 5 to add course\nSelect 6 to search\nSelect 7 to exit\n')
  choice = int(choice)
  if choice == 1:
    role = input('Select 0 for student\nSelect 1 for instructor\nSelect 2 for admin\nSelect 3 for courses\n')
    role = int(role)
    if role == 3:
      crsr.execute("SELECT * FROM COURSE")
    else:
      crsr.execute("SELECT * FROM {};".format(users[role]))
    results = crsr.fetchall()
    for i in results:
      print(i)
  elif choice == 2:
    user = {}
    print('----------Add User----------')
    userType = input('Select 0 for student\nSelect 1 for instructor\nSelect 2 for admin\n')
    userType = int(userType)
    userID = input('Enter ID: ')
    user["ID"] = int(userID)
    user["NAME"] = input('Enter first name: ')
    user["SURNAME"] = input('Enter last name: ')
    user["EMAIL"] = input('Enter email: ')
    if userType == 0:
      user["GRADYEAR"] = input('Enter graduation year: ')
      user["MAJOR"] = input('Enter major: ')
    elif userType == 1:
      user["TITLE"] = input('Enter title: ')
      user["HIREYEAR"] = input('Enter hire year: ')
      user["DEPT"] = input('Enter department: ')
    elif userType == 2:
      user["TITLE"] = input('Enter title: ')
      user["OFFICE"] = input("Enter office locaiton: ")
    addUser(userType, user)
    print("User added!")
    user.clear()
  elif choice == 3:
    print('----------Remove User----------')
    userType = input('Select 0 for student\nSelect 1 for instructor\nSelect 2 for admin\n')
    userType = int(userType)
    userID = input('Enter ID for the user you wish to remove: ')
    userID = int(userID)
    removeUser(userType, userID)
    print("User removed!")
  elif choice == 4:
    print('----------Update User----------')
    userType = input('Select 0 for student\nSelect 1 for instructor\nSelect 2 for admin\n')
    userType = int(userType)
    userID = input('Enter ID for the user you wish to update: ')
    userID = int(userID)
    field = input("Enter what field you would like to update: ")
    userUpdate = input("Enter update: ")
    updateUser(userType, userID, field, userUpdate)
    print("User updated!")
  elif choice == 5:
    course = {}
    print('----------Add Course----------')
    crn = input("Enter CRN: ")
    course["CRN"] = int(crn)
    course["TITLE"] = input("Enter title: ")
    course["DEPT"] = input("Enter department: ")
    query = "SELECT * FROM INSTRUCTOR WHERE DEPT = ?"
    crsr.execute(query, (course["DEPT"],))
    results = crsr.fetchall()
    print("Available intructors for this course: ")
    for i in results:
      print(i)
    instructor = input("Enter instructor ID: ")
    course["INSTRUCTOR"] = int(instructor)
    time = input("Enter time: ")
    course["TIME"] = int(time)
    course["DAY"] = input("Enter day(s): ")
    course["SEMESTER"] = input("Enter semester: ")
    year = input("Enter year: ")
    course["YEAR"] = int(year)
    credit = input("Enter number of credits: ")
    course["CREDITS"] =int(credit)
    addCourse(course)
    print("Course added!")
    course.clear()
  elif choice == 6:
    query = input("Enter your query: ")
    crsr.execute(query)
    results = crsr.fetchall()
    for i in results:
      print(i)
  elif choice == 7:
    connection.close()
    break
