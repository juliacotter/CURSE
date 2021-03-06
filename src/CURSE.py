from array import *
import copy
import random


# --------------------COURSE CLASS---------------------------
class course:

    def __init__(self, crn, t, d, i, tm, dy, s, y, c):
        self.CRN = crn
        self.title = t
        self.department = d
        self.instructor = i
        self.time = tm
        self.day = dy
        self.semester = s
        self.year = y
        self.credits = c
        self.regStudents = []


# --------------------USER CLASS---------------------------
class user:
    def __init__(self, wn, fn, ln, em, pw):
        self.wNumber = wn
        self.firstName = fn
        self.lastName = ln
        self.email = em
        self.password = pw
        self.role = "NULL"


# --------------------STUDENT CLASS---------------------------
class student(user):

    def __init__(self, wn, fn, ln, em, pw, mj, gy):
        user.__init__(self, wn, fn, ln, em, pw)
        self.major = mj
        self.graduationYear = gy
        self.regCourses = []
        self.role = "Student"

    def checkSchedule(self, semester, year):
        if (len(self.regCourses) != 0):
            for c in self.regCourses:
                if(c.semester == semester and c.year == year):
                    print(c.CRN, c.title, c.time, c.day)
                else:
                    print("You are not registered for any courses this semester.")

        else:
            print("You are not registered for any courses.")
            return

    def courseRegister(self, c, semester, year):
        dropAdd = int(input("Type 1 to Add and 2 to Drop."))

        if (dropAdd == 1):
            semesterCourses = [course for course in c if course.semester == semester and course.year == year]
            if (len(semesterCourses) == 5):
                print("Sorry, you have registered for too many courses.")
                return

            else:
                crnInput = int(input("Please enter the CRN for the course you wish to register."))
                for rc in self.regCourses:
                    if(rc.CRN == crnInput):
                        print("You have already registered for this course.")
                        return
                for course in c:
                    if (course.CRN == crnInput and course.semester == semester and course.year == year):
                        self.regCourses.append(course)
                        course.regStudents.append(self)
                        print("You have been enrolled in ", course.CRN, course.title)
                        return
                print("Sorry, there was no course found with that CRN during that semester.")

        elif (dropAdd == 2):
            if (len(self.regCourses) == 0):
                print("Sorry, you have not registered for any courses yet.")
                return

            else:
                crnInput = int(input("Please enter the CRN you wish to remove."))

                for course in range(len(c)):
                    if (c[course].CRN == crnInput and course.semester == semester and course.year == year):
                        c[course].regStudents.remove(self)
                        self.regCourses = [elem for elem in self.regCourses if elem != course]
                        return

                    print("Sorry, there was no course found with that CRN during that semester.")


# --------------------INSTRUCTOR CLASS---------------------------
class instructor(user):

    def __init__(self, wn, fn, ln, em, pw, t, hy, d):
        user.__init__(self, wn, fn, ln, em, pw)
        self.title = t
        self.hireYear = hy
        self.dept = d
        self.offeredCourses = [c for c in courses if self.wNumber == c.instructor]
        self.role = "Instructor"

    def checkRoster(self, courses):
        if (len(self.offeredCourses) == 0):
            print("You aren't teaching any courses!")
            return
        COURSE = int(input("Please enter a courses CRN to view it's roster. "))
        for c in self.offeredCourses:
            if (c.CRN == COURSE):
                print(c.title, c.CRN)
                for course in courses:
                    if (course.CRN == c.CRN):
                        for s in course.regStudents:
                            print(s.wNumber, s.firstName, s.lastName)
                        return
        print("Sorry, you do not teach any courses with that CRN.")
        return

    def checkCourses(self):
        if (len(self.offeredCourses) == 0):
            print("You aren't teaching any courses!")
            return
        for c in self.offeredCourses:
            print(c.title, c.CRN, ":")
            for course in courses:
                if(course.CRN == c.CRN):
                    if(len(course.regStudents) == 0):
                        print("No students in this course.")
                        continue
                    for s in course.regStudents:
                        print(s.wNumber, s.firstName, s.lastName)
                    print("--------------------")


# --------------------ADMIN CLASS---------------------------
class admin(user):

    def __init__(self, wn, fn, ln, em, pw, t, ol):
        user.__init__(self, wn, fn, ln, em, pw)
        self.title = t
        self.officeLocation = ol

        self.role = "Admin"

    def checkRoster(self):
        crnInput = int(input("Please enter the CRN for the course roster you wish to view."))
        for c in courses:
            if (c.CRN == crnInput):
                if(len(c.regStudents) == 0):
                    print("This course is currently empty!")
                    return
                else:
                    print("The students in this course are :")
                    for s in c.regStudents:
                        print(s.wNumber, s.firstName, s.lastName)
                    print("~END OF COURSE LIST~")
                    return
        print("Sorry, no course was found with that CRN.")
        return

    def editCourse(self, students, courses, instructors):
        choice = int(input("Type 1 to add a course, 2 to delete a course, and 3 to edit a course. "))

        if choice == 1:
            COURSE = int(input("Please enter the CRN for the course you would like to add. "))
            for c in courses:
                if (c.CRN == COURSE):
                    print("Sorry, that CRN is already assigned to a course.")
                    return
            TITLE = input("Enter the course title. ")
            DEPARTMENT = input("Enter the course department. ")
            print("-----INSTRUCTOR LIST-----")
            for i in instructors:
                if(i.dept == DEPARTMENT):
                    print(i.wNumber, i.firstName, i.lastName)
            INSTRUCTOR = int(input("Enter the instructors W Number for this class."))
            for i in instructors:
                if(i.wNumber == INSTRUCTOR):
                    TIME = input("Enter the course time. (ex. 8:00 = 0800) ")
                    DAY = input("Enter the course day(s). ")
                    SEMESTER = input("Enter the course semester. ")
                    YEAR = int(input("Enter the course year. "))
                    CREDITS = input("Enter the course credits. ")
                    newCourse = course(COURSE, TITLE, DEPARTMENT, INSTRUCTOR, TIME, DAY, SEMESTER, YEAR, CREDITS)
                    courses.append(newCourse)
                    i.offeredCourses.append(newCourse)
                    print(newCourse.CRN, newCourse.title, "has been created.")
                    return
            print("Sorry, there was no instructor with that W Number.")
            return

        elif choice == 2:
            COURSE = int(input("Please enter the CRN for the course you would like to delete. "))
            for c in range(len(courses)):
                if (courses[c].CRN == COURSE):
                    for s in range(len(students)):
                        if courses[c] in students[s].regCourses:
                            students[s].regCourses.remove(courses[c])

                    for i in range(len(instructors)):
                        if courses[c] in instructors[i].offeredCourses:
                            instructors[i].offeredCourses.remove(courses[c])

                    print(courses[c].CRN, courses[c].title, "has been removed.")
                    courses.remove(courses[c])
                    return
            print("Sorry, there was no course found with that CRN.")
            return
        elif choice == 3:
            print("1 to edit ")
            print("1 to edit ")
            print("1 to edit ")
            print("1 to edit ")
            print("1 to edit ")

        else:
            print("Invalid input")

    # julia
    def editStudent(self, students, courses):
        choice = int(input("Type 1 to add a student, 2 to delete a student, or 3 to edit a student: "))

        if choice == 1:
            WNUMBER = int(input("Enter WNumber: "))
            for s in students:
                if s.wNumber == WNUMBER:
                    print("Sorry, a student is already assigned to that W Number.")
                    return
            FIRSTNAME = input("Enter first name: ")
            LASTNAME = input("Enter last name: ")
            for s in students:
                if (s.firstName == FIRSTNAME) & (s.lastName == LASTNAME):
                    print("The student that you entered matches an existing student.")
                    print(s.wNumber, s.firstName, s.lastName, s.email, s.major, s.graduationYear)
                    yn = input("Does this match the student you wish to add? (y/n)")
                    if yn == 'y':
                        return
            EMAIL = input("Enter email: ")
            for s in students:
                if s.email == EMAIL:
                    print("Sorry, a student is already registered to that email.")
                    return
            PASSWORD = input("Enter password: ")
            MAJOR = input("Enter major: ")
            GRADYEAR = int(input("Enter graduation year: "))
            newStudent = student(WNUMBER, FIRSTNAME, LASTNAME, EMAIL, PASSWORD, MAJOR, GRADYEAR)
            students.append(newStudent)
            print(newStudent.wNumber, newStudent.firstName, newStudent.lastName, "has been created.")

        elif choice == 2:
            WNUMBER = int(input("Enter student's W Number: "))
            for s in range(len(students)):
                if (students[s].wNumber == WNUMBER):
                    for c in range(len(courses)):
                        if (courses[c] in students[s].regCourses):
                            courses[c].regStudents.remove(students[s])
                    print("Deleting", students[s].wNumber, students[s].firstName, students[s].lastName)
                    students.remove(students[s])
                    return
            print("Sorry, there was no student found with that W Number.")
            return
        elif choice == 3:
            editChoice = int(input("Type 1 to add student to course, 2 to drop student from course, or 3 to update student information: "))
            STUDENT = int(input("Enter student's W Number: "))
            if editChoice == 1:
                CRN = int(input("Enter the CRN you wish to add: "))
                for s in range(len(students)):
                    if students[s].wNumber == STUDENT:
                        for c in range(len(courses)):
                            if (courses[c].CRN == CRN):
                                students[s].regCourses.append(courses[c])
                                courses[c].regStudents.append(students[s])
                                print("Student added to course!")
                                return

                        print("Sorry, there was no course found with that CRN.")
                        return
                print("Sorry, there was no student found with that W Number.")
                return
            elif editChoice == 2:
                CRN = int(input("Enter the CRN you wish to drop: "))
                for s in range(len(students)):
                    if students[s].wNumber == STUDENT:
                        for rc in range(len(students[s].regCourses)):
                            if students[s].regCourses[rc].CRN == CRN:
                                students[s].regCourses.remove(students[s].regCourses[rc])

                                for c in range(len(courses)):
                                    if courses[c].CRN == CRN:
                                        for rs in range(len(courses[c].regStudents)):
                                            if courses[c].regStudents[rs].wNumber == STUDENT:
                                                courses[c].regStudents.remove(courses[c].regStudents[rs])
                                                print("Student dropped from course!")
                                                return
                        print("Sorry, that student was not registered for a course with that CRN.")
                        return
                print("Sorry, no student was found with that W Number.")
                return
            elif editChoice == 3:
                field = input("Enter what field you would like to update: ")
                update = input("Enter update: ")
                for s in students:
                    if s.wNumber == STUDENT:
                        setattr(s, field, update)
                        print("Updated!")
            else:
                print("Invalid input")
        else:
            print("Invalid input")

courses = [
    course(40001, 'Computer Architecture', 'BSEE', 20001, 800, 'TR', 'Summer', 2019, 3),
    course(40002, 'Ethics', 'HUSS', 20002, 1300, 'TR', 'Summer', 2019, 4),
    course(40003, 'Data Structures', 'BCOS', 20005, 1230, 'WF', 'Summer', 2019, 4),
    course(40004, 'Thermodynamics I', 'BSME', 20006, 1000, 'TR', 'Summer', 2019, 4),
    course(40005, 'Computer Networks', 'BSCO', 20004, 800, 'WF', 'Summer', 2019, 4)
]
students = [
    student(10001, 'Isaac', 'Newton', 'newtoni@wit.edu', "asdfghjkl", 'BSAS', 1668),
    student(10002, 'Marie', 'Curie', 'curiem@wit.edu', "asdfghjkl,", "BSAS", 1903),
    student(10003, 'Nikola', 'Tesla', 'telsan@wit.edu', "asdfghjkl", "BSEE", 1878),
    student(10004, 'Thomas', 'Edison', 'notcool@wit.edu', "asdfghjkl", 'BSEE', 1879),
    student(10005, 'John', 'von Neumann', 'vonneumannj', 'asdfghjkl', 'BSCO', 1923),
    student(10006, 'Grace', 'Hopper', 'hopperg@wit.edu', 'asdfghjkl', 'BCOS', 1928),
    student(10007, 'Mae', 'Jemison', 'jemisonm@wit.edu', 'asdfghjkl', 'BSCH', 1981),
    student(10008, 'Mark', 'Dean', 'deanm@wit.edu', 'asdfghjkl', 'BSCO', 1979),
    student(10009, 'Michael', 'Faraday', 'faradaym@wit.edu', 'asdfghjkl', 'BSAS', 1812),
    student(10010, 'Ada', 'Lovelace', 'lovelacea@wit.edu', 'asdfghjkl', 'BCOS', 1832),
    student(10011, 'Julia', 'Cotter', 'cotterj@wit.edu', 'asdfghjkl', 'BSCO', 2020)
]
me = student(10012, 'Wilson', 'Ochoa', 'ochoaw@wit.edu', 'asdfghjkl', 'BSCO', 2020)
students.append(me)
instructors = [
    instructor(20001, 'Joseph', 'Fourier', 'fourierj@wit.edu', 'asdfghjkl', 'Full Prof.', 1820, 'BSEE'),
    instructor(20002, 'Nelson', 'Mandela', 'mandelan@wit.edu', 'asdfghjkl', 'Full Prof.', 1994, 'HUSS'),
    instructor(20003, 'Galileo', 'Galilei', 'galileig@wit.edu', 'asdfghjkl', 'Full Prof.', 1600, 'BSAS'),
    instructor(20004, 'Alan', 'Turing', 'turinga@wit.edu', 'asdfghjkl', 'Associate Prof.', 1940, 'BSCO'),
    instructor(20005, 'Katie', 'Bouman', 'boumank@wit.edu', 'asdfghjkl', 'Assistant Prof.', 2019, 'BCOS'),
    instructor(20006, 'Daniel', 'Bernoulli', 'bernoullid@wit.edu', 'asdfghjkl', 'Associate Prof.', 1760, 'BSME')
]
admins = [
    admin(30001, 'Barack', 'Obama', 'obamab@wit.edu', 'asdfghjkl', 'Past President', 'Dobbs 1600'),
    admin(30002, 'Malala', 'Yousafzai', 'yousafzaim@wit.edu', 'asdfghjkl', 'Registrar', 'Wentworth 101')
]


choice = 0
userEmail = "NULL"
userPW = "NULL"
string = "ROLE"
quitter = 0
loggedIn = 0

while (1):
    while loggedIn != 1:
        print("------------Login Menu---------------")
        userEmail = input("Enter email: ")
        userPW = input("Enter password: ")

        for s in students:
            if (userEmail == s.email) & (userPW == s.password):
                currentUser = s
                loggedIn = 1
                break

        if loggedIn == 1:
            break

        for i in instructors:
            if (userEmail == i.email) & (userPW == i.password):
                currentUser = i
                loggedIn = 1
                break
        if loggedIn == 1:
            break

        for a in admins:
            if (userEmail == a.email) & (userPW == a.password):
                currentUser = a
                loggedIn = 1
                break
        if loggedIn == 1:
            break
        print("Invalid email or password.")

    if (currentUser.role == "Admin"):
        while (loggedIn == 1):
            print("---------------ADMIN MENU----------------")
            choice = int(input(
                "Type 1 to check a roster, type 2 to edit a course, type 3 to edit a student, or type 9 to Logout."))
            if (choice == 1):
                currentUser.checkRoster()

            elif (choice == 2):
                currentUser.editCourse(students, courses, instructors)

            elif (choice == 3):
                currentUser.editStudent(students, courses)
            elif (choice == 9):
                currentUser = 0
                loggedIn = 0

            else:
                print("Sorry, that was not one of the choices. Please try again.")


    elif (currentUser.role == "Student"):
        semester = None
        year = None
        while (loggedIn == 1):
            print("---------------STUDENT MENU----------------")
            choice = int(input(
                "Type 1 to set semester, type 2 to enter course registration, type 3 to check all available courses, type 4 to check your schedule, or type 9 to Logout."))
            choice = int(choice)

            if (choice == 1):
                semester = input("Enter the semester: ")
                year = int(input("Enter year: "))

            if (choice == 2):
                if (semester is not None and year is not None):
                    currentUser.courseRegister(courses, semester, year)
                else:
                    print("Must set semester")

            elif (choice == 3):
                if (semester is not None and year is not None):
                    for c in courses:
                        if c.semester == semester and c.year == year:
                            print(c.CRN, c.title, c.time, c.day)
                else:
                    print("Must set semester")

            elif (choice == 4):
                if (semester is not None and year is not None):
                    currentUser.checkSchedule(semester, year)
                else:
                    print("Must set semester")

            elif (choice == 9):
                currentUser = 0
                loggedIn = 0

            else:
                print("Sorry, that was not one of the choices. Please try again.")

    elif (currentUser.role == "Instructor"):
        while (loggedIn == 1):
            print("---------------INSTRUCTOR MENU----------------")
            choice = int(input("Type 1 to check a roster, type 2 to check your courses, or type 9 to Logout."))

            if (choice == 1):
                currentUser.checkRoster(courses)

            elif (choice == 2):
                currentUser.checkCourses()

            elif (choice == 9):
                currentUser = 0
                loggedIn = 0

            else:
                print("Sorry, that was not one of the choices. Please try again.")

    else:
        print("Sorry, it seems you are an unauthorized user. Please check with your Administrator to gain privileges.")
