
# coding: utf-8

# Name: Minh Quang Duong
# 
# Course: ECON 8320
# 
# Professor: Dustin White
# 
# Assignment: #3

# We will create a class to record student academic information:
# 
# 1.  A class should contain attributes for recording
# • Name (First and Last separately)
# • Date of Birth
# • High School (name and city separately)
# • Degree program
# • Address
# • Grade history.  is should be of a type that allows the storage of the course name, grade in the course, the number of credits assigned to the course, and the semester and year taken.
# 
# 2.  A class should include methods to
# • Calculate cumulative GPA
# • Calculate semester GPA
# • Count the number of credits a student has accumulated
# • Add a course to the grade history
# • DeterminescholarshipeligibilitybasedonthefollowingGPA cutoffs: ≥ 3.9 for a full-ride, ≥ 3.63 for a half-tuition schol- arship, and ≥ 3.3 for a 1/4 tuition scholarship. All GPA’s below the minimum scholarship cutoff receive no reward.

# In[1]:


class CourseInformation(object):
    """The CourseInformation class is designed to complete both tasks. Inside the class, there are a few functions, including
    init, add, aggGPA, semGPA, creditcount, scholarship and str"""
    def __init__(self, fname = "Minh", lname = "Duong", 
                 dob = "24 March 1990", hschool_name = "High School for the Gifted", 
                 hschool_city = "Ho Chi Minh", degree = "MBA & MIS", 
                 address = "210 South 16th Street, Omaha, NE, 68102"):
        """This function is to input personal information by default. The gradehistory is left blank so that
        course information will be added later on"""
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.hschool_name = hschool_name
        self.hschool_city = hschool_city
        self.degree = degree
        self.address = address
        self.gradehistory = []
    def __add__(self, course):
        """This function is used to add courses to gradehistory. Each course will be a dictionary with the following keys:
        Course Name
        Grade
        Number of Credits
        Semester
        Year
        In that exact order
        
        A slew of if functions are used to unit test the input"""
        
        if (isinstance(course["Grade"], str)): #test to see if Grade is a string. If yes, it is an error
            raise RuntimeError("Wrong Grade type")
        if (course["Grade"] <0) or (course["Grade"] > 4): #test to see if Grade is between 0 and 4. If yes, it is an error
            raise RuntimeError("Grade out of range. It has to be in the range of 0 and 4")
        if (isinstance(course["Number of Credits"], str)): #test to see if the number of credits is a string. If yes, it is an error
            raise RuntimeError("Wrong Number of Credits input")
        if (course["Number of Credits"] < 1) or (course["Number of Credits"] > 3): #test to see if number of credits is between 1 and 3. If not, it is an error
            raise RuntimeError("Number of Credits is out of range. It has to be in the range of 1 and 3")
            #if not (isinstance(self.gradehistory[i]["Grade"], int)):
            #    raise RuntimeError("Number of Credits has to be an integer")
        if not (isinstance(course["Year"], int)): #test to see if the year is an integer. If not, it is an error
            raise RuntimeError("Year has to be a valid integer") 
        if (course["Year"] != 2017) and (course["Year"] != 2018): #test to see if the year is not either 2017 or 2018. If yes, it is an error
            raise RuntimeError("Year has to be 2017 or 2018")
        if not (isinstance(course["Semester"], str)): #test to see if the semester is a string. If not, it is an error
            raise RuntimeError("Semester has to be a String")            
        if (course["Semester"] != "Fall") and (course["Semester"] != "Spring"): #test to see if the semester is either Spring or Fall. If not, it is an error
            raise RuntimeError("Semester has to be either Fall or Spring")
        return self.gradehistory.append(course) #add course    
    def aggGPA (self):
        """This function is used to calculate the aggregate/cumulative GPA. It is equal to the sum of all grades
        divided by the number of courses, which is the length of the list gradehistory"""
        totalgrade = 0
        totalcourses = len(self.gradehistory)
        for i in range(len(self.gradehistory)):    
            totalgrade += self.gradehistory[i]["Grade"]
        if totalcourses == 0: #test to see if the denominator is equal to zero
            aggre = 0.0
        else:
            aggre = totalgrade/totalcourses
        return aggre
    def semGPA (self, year, semester):
        """This function is used to calculate the semester GPA
        In this example, only two semesters are considered Fall2017 and Spring2018
        The function will receive two variables: year and semester. It will check and match the input with the course information to calculate the relevant GPA"""
        semgrade = 0
        semcredit = 4 #students can take 4 courses per semester
        for i in range(len(self.gradehistory)):
            if self.gradehistory[i]["Semester"] == semester and self.gradehistory[i]["Year"] == year: #match input with course information
                semgrade += self.gradehistory[i]["Grade"]
        if semcredit == 0: #check to see if the denominator is equal to zero
            semGPA = 0.0
        else:
            semGPA = semgrade/semcredit
        return semGPA         
    def creditcount (self):
        """This function is to determine the total number of credits. It is equal to the sum of
        all credits"""
        creditcount = 0
        for i in range(len(self.gradehistory)):
            creditcount += self.gradehistory[i]["Number of Credits"]
        return creditcount
    def scholarship(self):
        """This function is to determine the level of scholarship a student can get by comparing overall GPA 
        with predetermined thresholds"""
        if self.aggGPA() >= 3.9:
            result = "Full ride"
        elif self.aggGPA() >= 3.63:
            result = "Half tuition"
        elif self.aggGPA () >= 3.3:
            result = "1/4 scholarship"
        else:
            result = "No scholarship"
        return result
    def __str__(self):
        """This is to print out the result"""
        return "Name is %s %s\n All the courses are %s\n Overall GPA is %s\n Fall2017 GPA is %s\n Spring2018 GPA is %s\n Total credits are %s\n Scholarship type is %s" % (self.fname, self.lname, self.gradehistory, self.aggGPA(), 
                                           self.semGPA(2017, "Fall"), self.semGPA(2018, "Spring"), self.creditcount(), self.scholarship())

"""There are a lot of errors in these input values. They are meant to unit test"""

course1 = {"Course Name": "Tool for Data Analysis", "Grade" : -1.0, 
                      "Number of Credits": 0.0, "Semester": "Spring", "Year": 2019}
course2 = {"Course Name": "Data Communications", "Grade" : 4.0, 
                      "Number of Credits": 3.0, "Semester": "Spring", "Year": 'aa'}
course3 = {"Course Name": "Management of Software Development", "Grade" : 3.7, 
                      "Number of Credits": 3.0, "Semester": "Spring", "Year": 2018}
course4 = {"Course Name": "Business Analytics", "Grade" : 5.0, 
                      "Number of Credits": 4.0, "Semester": "Spring", "Year": 2018}
course5 = {"Course Name": "Advanced Statistics", "Grade" : 4.0,
                      "Number of Credits": 3.0, "Semester": "Fall", "Year": 2017}
course6 = {"Course Name": "Overview of Systems Development", "Grade" : 'B+',
                      "Number of Credits": 'a', "Semester": "Fall", "Year": 2017}
course7 = {"Course Name": "Decision Support Systems", "Grade" : 4.0,
                      "Number of Credits": 3.0, "Semester": 2018, "Year": 2017}
course8 = {"Course Name": "Data Visualization", "Grade" : 4.0,
                      "Number of Credits" : 3.0, "Semester": "Summer", "Year": 2017}

a = CourseInformation()
a + course1
a + course2
a + course3
a + course4
a + course5
a + course6
a + course7
a + course8
print (a)

