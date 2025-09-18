#Declare the first bit of information using strings
Full_name = "Jordan Smith"
Stu_email = "jsmith@ncat.edu"
Stu_hometome = "Charlotte, NC"
Grad_year = "Spring 2028"
Stu_major = "Computer Science"

#organize academic info using list
Current_course = ['COMP 163','MATH 150','ENG 101','HIS 105']
Credit_hours = [3,3,3,3]
Semester_GPA = [3.2,3.6,3.4,3.7]
#make sure to keep these values floated
Finished_courses = ['Biology','Chemistry','Calculus','Spanish II','World History']

#Using Tuples gather contact information
Emer_Contact = ("Mom", "Hannah Smith","704-555-0199")
Address = ('456 Oak Street','Charlotte','NC',"28202")
Insta = ('Instagram','@jordan_codes',312)
Twitter = ('Twitter','@jordandev',127)
B_Day = ("Birthday",'5','22','2006')

#Do the same thing but ur using SETs now :)
Current_skills = {'Python basics','HTML','Problem solving','Time management','Photography'}
Dream_skills = {'JavaScript','Data structures','Git','Web design','Public speaking'}
Dream_career = {'Software development','Web development','Data science','Game development'}
Hobbies = {'Gaming','Photography','Reading','Soccer','Music'}
Sad_things = {'One Piece','Barry','Life',"Incantation","Momento"}
#Both one piece and life bring me to tears because they both lowkey suck 

#You know the drill but for DICTIONARIES now
Course_credits = {"COMP 163" : 3,"MATH 150" : 3,"ENG 101" : 3,"HIS 105" : 3}
numCourses = len(Current_course)
Course_professors = {"COMP 163" : "Prof. Rhodes","MATH 150" : "Dr. Lee","ENG 101" : "Dr. Martinez","HIS 105" : "Dr. Brown"}
Course_room = {"COMP 163" : "M-Eric 300","MATH 150" : "Marteena 201","ENG 101" : "Crosby 121","HIS 105" : "Crosby 210"}
Monthly_budget = {"Food" : 450, "Entertainment" : 200, "Books" : 125, "Transportation" : 100}
Study_HS = {"Programming" : 10, "Math" : 8, "English" : 4, "History" : 3}
Contact ={"Mom" : "704-55-0199", "Roomate" : "336-55-7821", "Academic Advisor" : "336-334-5000"}

#Variable to make Calculations less death inducing
numCourse_credits = Course_credits["COMP 163"] + Course_credits["MATH 150"] + Course_credits["ENG 101"] + Course_credits["HIS 105"]
avg_gpa = float((Semester_GPA[0] + Semester_GPA[1] + Semester_GPA[2] + Semester_GPA[3]) / len(Current_course))
numStudy_hours = Study_HS["Programming"] + Study_HS["Math"] + Study_HS["English"] + Study_HS["History"]
monthbudget = Monthly_budget["Food"] + Monthly_budget["Entertainment"] + Monthly_budget["Books"] + Monthly_budget["Transportation"]
numBookcost = Monthly_budget["Books"]
#Calculations
Average_GPA = avg_gpa
Completed_courses = len(Finished_courses)
Weekly_study_hours = numStudy_hours
AcademicLoad = Credits_plus_studyhours = numCourse_credits + numStudy_hours
Monthly_budget_total = monthbudget
Daily_food = Monthly_budget["Food"] / 30
# round to 2 decimals later
Annual_budget = Monthly_budget_total * 12
Study_costPERhour = numBookcost / numStudy_hours
#round to 2 decimal places

#Ugh a bunch of random calculations you got this tho last step for calulations!
Total_follows = Insta[2] + Twitter[2]
Entertainment_backlog = len(Sad_things)
Skill_have = len(Current_skills)
Skills_want = len(Dream_skills)

#DEBUG SECTION
#print(f"{avg_gpa:.2f}")
#print(numCourse_credits)
#print(Course_credits["COMP 163"])
#print(type(Current_skills))
#print(Current_skills)
#print(len(Address))
#print(type(Emer_Contact))
#print(Emer_Contact[1])
#DEBUG SECTION END

#Now... It begins!
#F strings carry lol great idea utilizing them Mariyah. Thanks Mariyah (Professor please ignore this this is how I work lol )
print("================================================================")
print("              PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("================================================================")
print(f"Student: {Full_name} | Email: {Stu_email}")
print(f"From: {Stu_hometome} | Graduating: {Grad_year}")
print(f"Major: {Stu_major}")
#First part of cases complete!

print("")

print("=== ACADEMIC PROFILE ===")
print(f"Current Semester: {numCourse_credits} credits across {numCourses} courses")
print(f"Cumulative GPA: {Average_GPA:.2f}")
print(f"Weekly Study Time: {Weekly_study_hours} hours")
print(f"Academic Investment: ${Study_costPERhour} per study hour")
#End of this section this student should honestly take another class they need to struggle more 
print("")

print("Current Courses:")
print(f"{Current_course[0]} - {Credit_hours[0]} credits - {Course_professors["COMP 163"]} - {Course_room["COMP 163"]}")
print(f"{Current_course[1]} - {Credit_hours[1]} credits - {Course_professors["MATH 150"]} - {Course_room["MATH 150"]}")
print(f"{Current_course[2]} - {Credit_hours[2]} credits - {Course_professors["ENG 101"]} - {Course_room["ENG 101"]}")
print(f"{Current_course[3]} - {Credit_hours[3]} credits - {Course_professors["HIS 105"]} - {Course_room["HIS 105"]}")
#easy peasy
print("")

print("=== PERSONAL DEVELOPMENT ===")
print(f"Current Skills: {Current_skills}")
print(f"Learning Goals: {Dream_skills}")
print(f"Career Interests: {Dream_career}")
print(f"Skills Currently Have: {Skill_have}")
print(f"Skills Want to Learn: {Skills_want}")
print("")

print("=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${Monthly_budget_total}")
print(f"Food: ${Monthly_budget["Food"]} (${Daily_food:.1f}/day)")
print(f"Entertainment: ${Monthly_budget["Entertainment"]}")
print(f"Books: ${Monthly_budget["Books"]}")
print(f"Transportation: ${Monthly_budget["Transportation"]}")
print(f"Annual Projection: ${Annual_budget}")

print("")

print("=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: {Emer_Contact[1]} ({Emer_Contact[0]}) - {Emer_Contact[2]}")
print(f"Home Address: {Address[0]}, {Stu_hometome} {Address[3]}")
print(f"Social Media Presence: {Insta[2] + Twitter[2]} followers across 2 platforms")
print(f"Key Contacts: {len(Contact)} people in directory")

print("")

print("=== LIFE STATISTICS ===")
print(f"Total Courses Completed: {len(Finished_courses)}")
print(f"Current Academic Load: {AcademicLoad} weekly commitments")
print(f"Entertainment Backlog: {len(Sad_things)} items")
print(f"Current Hobbies: {len(Hobbies)} activities")

print("================================================================")
