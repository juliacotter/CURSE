from array import *
import copy
import random

#--------------------COURSE CLASS---------------------------
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
		
		
#--------------------USER CLASS---------------------------
class user:
	def __init__(self, wn, fn, ln, em, pw):
		self.wNumber = wn
		self.firstName = fn
		self.lastName = ln
		self.email = em
		self.password = pw
		self.role = "NULL"
		
		
#--------------------STUDENT CLASS---------------------------
class student(user):
	
	def __init__(self, wn, fn, ln, em, pw, mj, gy):
		user.__init__(self, wn, fn, ln, em, pw)
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
		dropAdd = int(input("Type 1 to Add and 2 to Drop."))

		
		if(dropAdd == 1):
			if(len(self.regCourses) == 5):
				print("Sorry, you have registered for too many courses.")
				return
			
			else:
				crnInput = int(input("Please enter the CRN for the course you wish to register."))
				
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
				crnInput = int(input("Please enter the CRN you wish to remove."))
				
				for course in self.regCourses:
					if(course.CRN == crnInput):
						course.regStudents = [elem for elem in course.regStudents if elem != self]
						self.regCourses = [elem for elem in self.regCourses if elem != course]
						
						return							


#--------------------INSTRUCTOR CLASS---------------------------	
class instructor(user):
	
	def __init__(self, wn ,fn, ln, em, pw, t, hy, d):
		user.__init__(self, wn, fn, ln, em, pw)
		self.title = t
		self.hireYear = hy
		self.dept = d
		self.offeredCourses = []
		self.role = "Instructor"
	def checkRoster(self):
		for c in self.offeredCourses:
			print(c.title, c.crn)
			for s in c.regStudents:
				print(s.wNumber, s.firstName, s.lastName)
			print()
		return
	
	def checkCourses(self):
		return
		
		
#--------------------ADMIN CLASS---------------------------
class admin(user):
	
	def __init__(self, wn, fn, ln, em, pw, t, ol):
		user.__init__(self, wn, fn, ln, em, pw)
		self.title = t
		self.officeLocation = ol
		
		self.role = "Admin"
		
		
	def checkRoster(self):
		crnInput = int(input("Please enter the CRN for the course roster you wish to view."))
		for c in courses:
			if(c.CRN == crnInput):
				print("The students in this course are :")
				for s in c.regStudents:
					print(s.wNumber, s.firstName, s.lastName)
				print("~END OF COURSE LIST~")
				return
				print("Sorry, no course was found with that CRN.")
		return
	
	def editCourse(self):
		choice = int(input("Type 1 to add a course, 2 to delete a course, and 3 to edit a course"))
		
		if choice == 1:
			pass
		
		elif choice == 2:
			pass
		
		elif choice == 3:
			pass

		else:
			print("Invalid input")
	
	# julia
	def editStudent(self, students, courses):
		choice = int(input("Type 1 to add a student, 2 to delete a student, or 3 to edit a student: "))

		if choice == 1:
			WNUMBER = int(input("Enter WNumber: "))
			FIRSTNAME = input("Enter first name: ")
			LASTNAME = input("Enter last name: ")
			EMAIL = input("Enter email: ")
			PASSWORD = input("Enter password: ")
			MAJOR = input("Enter major: ")
			GRADYEAR = int(input("Enter graduation year: "))
			newStudent = student(WNUMBER, FIRSTNAME, LASTNAME, EMAIL, PASSWORD, MAJOR, GRADYEAR)
			students.append(newStudent)
			for s in students:
				print(s.wNumber)

		elif choice == 2:
			WNUMBER = int(input("Enter student's W Number: "))
			for s in students:
				if(s.wNumber == WNUMBER):
					for c in courses:
						if(c in s.regCourses):
							c.regStudents = [elem for elem in c.regStudents if elem != s]
					students = [elem for elem in students if elem != s]
		
		elif choice == 3:
			editChoice = int(input("Type 1 to add student to course, 2 to drop student from course, or 3 to update student information: "))
			STUDENT = int(input("Enter student's W Number: "))
			if editChoice == 1:
				CRN = int(input("Enter the CRN you wish to add: "))
				for s in students:
					if s.wNumber == STUDENT:
						for c in courses:
							if(c.CRN == CRN):
								s.regCourses.append(c)
								c.regStudents.append(s)
								print("Student added to course!")
			elif editChoice == 2:
				CRN = int(input("Enter the CRN you wish to drop: "))
				for s in students:
					if s.wNumber == STUDENT:
						for c in s.regCourses:
							if c.CRN == CRN:
								s.regCourses = [elem for elem in s.regCourses if elem != c]
				for c in courses:
					if c.CRN == CRN:
						for s in c.regStudents:
							if s.wNumber == STUDENT:
								c.regStudents = [elem for elem in c.regStudents if elem != s]
								print("Student dropped from course!")
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
	student(10011, 'Julia', 'Cotter', 'cotterj@wit.edu', 'asdfghjkl', 'BSCO',2020),
	student(10012, 'Wilson', 'Ochoa', 'ochoaw@wit.edu', 'asdfghjkl', 'BSCO', 2020)
]
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
courses = [
	course(40001, 'Computer Architecture', 'BSEE', 20001, 800, 'TR', 'Summer', 2019, 3),
	course(40002, 'Ethics', 'HUSS', 20002, 1300, 'TR', 'Summer', 2019, 4),
	course(40003, 'Data Structures', 'BCOS', 20005, 1230, 'WF', 'Summer', 2019, 4),
	course(40004, 'Thermodynamics I', 'BSME', 20006, 1000, 'TR', 'Summer', 2019, 4),
	course(40005, 'Computer Networks', 'BSCO', 20004, 800, 'WF', 'Summer', 2019, 4)
]

choice = 0
userEmail = "NULL"
userPW = "NULL"
string = "ROLE"
quitter = 0
loggedIn = 0

while(1):
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
			choice = int(input("Type 1 to check a roster, type 2 to edit a course, type 3 to edit a student, or type 9 to Logout."))
			if(choice == 1):
				currentUser.checkRoster()
			
			elif(choice == 2):
				currentUser.editCourse()
				
			elif(choice == 3):
				currentUser.editStudent(students, courses)
				
			elif(choice == 9):
				currentUser = 0
				loggedIn = 0
			
			else: 
				print("Sorry, that was not one of the choices. Please try again.")
				
			
	elif(currentUser.role == "Student"):
		while(loggedIn == 1):
			print("---------------STUDENT MENU----------------")
			choice = int(input("Type 1 to enter course registration, type 2 to check all available courses, type 3 to check your schedule, or type 9 to Logout."))
			choice = int(choice)
			
			if(choice == 1):
				currentUser.courseRegister(courses)
			
			elif(choice == 2):
				for c in courses:
					print(c.CRN, c.title, c.time, c.day)
				
			elif(choice == 3):
				currentUser.checkSchedule()
				
			elif(choice == 9):
				currentUser = 0
				loggedIn = 0
				
			else: 
				print("Sorry, that was not one of the choices. Please try again.")

	elif(currentUser.role == "Instructor"):
		while(loggedIn == 1):
			print("---------------INSTRUCTOR MENU----------------")
			choice = int(input("Type 1 to check a roster, type 2 to check your courses, or type 9 to Logout."))
			
			if(choice == 1):
				currentUser.checkRoster()
			
			elif(choice == 2):
				currentUser.checkCourses()
				
			elif(choice == 9):
				currentUser = 0
				loggedIn = 0
				
			else: 
				print("Sorry, that was not one of the choices. Please try again.")
			
	else:
		print("Sorry, it seems you are an unauthorized user. Please check with your Administrator to gain privileges.")
