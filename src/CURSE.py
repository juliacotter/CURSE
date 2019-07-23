from array import *
import copy
import random



students = []
instructors = []
admins = []
courses = []


choice = 0
userEmail = "NULL"
userPW = "NULL"
string = "ROLE"
quitter = 0
loggedIn = 0

#---------------example objects-----------------




while loggedIn != 1:
	print("------------Login Menu---------------")
	userEmail = input("Enter email: ")
	userPW = input("Enter password: ")
	
	for s in students:
		if (userEmail == s.email)&(userPW == s.password):
			currentUser = s
			loggedIn = 1
			break
			
	if loggedIn == 1:
		break

	for i in instructors:
		if (userEmail == i.email)&(userPW == i.password):
			currentUser = i
			loggedIn = 1
			break
	if loggedIn == 1:
		break
		
	for a in admins:
		if (userEmail == a.email)&(userPW == a.password):
			currentUser = a
			loggedIn = 1
			break
	if loggedIn == 1:
		break
	print("Invalid email or password.")

if(currentUser.role == "Admin"):
	while(loggedIn == 1):
		print( "---------------ADMIN MENU----------------")
		choice = input("Type 1 to check a roster, type 2 to edit a course, type 3 to edit a student, or type 9 to Logout.")
		if(choice == 1):
			currentUser.checkRoster()
		
		elif(choice == 2):
			currentUser.editCourse()
			
		elif(choice == 3):
			currentUser.editStudent(students, courses)
			
		elif(choice == 9):
			currentUser = NULL
			loggedIn = 0
		
		else: 
			print("Sorry, that was not one of the choices. Please try again.")
			
		
elif(currentUser.role == "Student"):
	while(loggedIn == 1):
		print("---------------STUDENT MENU----------------")
		choice = input("Type 1 to enter course registration, tpye 2 to check all available courses, type 3 to check your schedule, or type 9 to Logout.")
		
		if(choice == 1):
			currentUser.courseRegister(courses)
		
		elif(choice == 2):
			for c in courses:
				print(c.title, c.CRN, c.time, c.day)
			
		elif(choice == 3):
			currentUser.checkSchedule()
			
		elif(choice == 9):
			currentUser = NULL
			loggedIn = 0
			
		else: 
			print("Sorry, that was not one of the choices. Please try again.")

elif(currentUser.role == "Instructor"):
	while(loggedIn == 1):
		print("---------------INSTRUCTOR MENU----------------")
		choice = input("Type 1 to check a roster, type 2 to check your courses, or type 9 to Logout.")
		
		if(choice == 1):
			currentUser.checkRoster()
		
		elif(choice == 2):
			currentUser.checkCourses()
			
		elif(choice == 9):
			currentUser = NULL
			loggedIn = 0
			
		else: 
			print("Sorry, that was not one of the choices. Please try again.")
		
else:
	print("Sorry, it seems you are an unauthorized user. Please check with your Administrator to gain privileges.")
		
		
		
		
		
		
		
#--------------------USER CLASS---------------------------
class course:
	
	def __init__(self, t, d, i, s, crn, c, tm, dy):
		self.title = t
		self.department = d
		self.instructor = i
		self.semester = s
		self.CRN = crn
		self.credits = c
		self.time = tm
		self.day = dy
		self.regStudents = []
		
		
		
		
#--------------------USER CLASS---------------------------
class user:
	
	def __init__(self, fn, ln, em, pw):
		self.wNumber = 0
		self.firstName = fn
		self.lastName = ln
		self.email = em
		self.password = pw
		self.role = "NULL"
		
		
#--------------------STUDENT CLASS---------------------------
class student(user):
	
	def __init__(self, fn, ln, em, pw, mj, gy):
		user.__init__(fn, ln, em, pw)
		self.major = mj
		self.graduationYear = gy
		self.regCourses = []
		self.role = "Student"
		
	def checkSchedule(self):
		if(len(self.regCourses) != 0):
			for c in self.regCourses:
				print(c.CRN, c.title, c.time, c.day)
		
		else:
			print("You are not registered for any courses.")
			return
			
		
	def courseRegister(self, c):
		dropAdd = input("Type 1 to Add and 2 to Drop.")
		
		if(dropAdd == 1):
			if(len(self.regCourses) == 5):
				print("Sorry, you have registered for too many courses.")
				return
			
			else:
				crnInput = input("Please enter the CRN for the course you wish to register.")
				
				for course in c:
					if(course.CRN == crnInput):
						self.regCourses.append(course)
						course.regStudents.append(self)
						print("You have been enrolled in ", course.CRN, course.title)
						return
		
		elif(dropAdd == 2):
			if(len(self.regCourses) == 0):
				print("Sorry, you have not registered for any courses yet.")
				return
				
			else:
				crnInput = input("Please enter the CRN you wish to remove.")
				
				for course in self.regCourses:
					if(course.CRN == crnInput):
						course.regStudents = [elem for elem in course.regStudents if elem != self]
						self.regCourses = [elem for elem in self.regCourses if elem != course]
						return
							


#--------------------INSTRUCTOR CLASS---------------------------	
class instructor(user):
	
	def __init__(self, fn, ln, em, pw, t, ol):
		user.__init__(fn, ln, em, pw)
		self.title = t
		self.officeLocation = ol
		self.offeredCourses = []
		self.roster = []
		self.role = "Instructor"
	def checkRoster(self):
		return
	
	def checkCourses(self):
		return
		
		
		
		
		
		
		
#--------------------ADMIN CLASS---------------------------
class admin(user):
	
	def __init__(self, fn, ln, em, pw, t, ol):
		user.__init__(fn, ln, em, pw)
		self.title = t
		self.officeLocation = ol
		
		self.role = "Admin"
		
		
	def checkRoster(self):
		return
	
	def editCourse(self):
		return
	
	def editStudent(self, s, c):
		return
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		