'''
You are a developer/student for a university. Your current project is to develop a system for students to find courses they share with
friends. The university has a system for querying courses students are enrolled in, returned as a list of (ID, course) pairs.

Write a function that takes in a collection of (student ID number, course name) pairs and returns, for every pair of students, a 
collection of all courses they share.


Sample Input:

enrollments1 = [
  ["518", "Image Processing"],
  ["914", "CPP"],
  ["914", "Operating Systems"],
  ["171", "Data Structures"],
  ["518", "SAD"],
  ["518", "Computer Graphics"],
  ["171", "Image Processing"],
  ["171", "Software Engineering"],
  ["914", "Computer Graphics"],
  ["125", "Computer Graphics"],
  ["518", "Data Structures"],
]

Sample Output (pseudocode, in any order):

find_pairs(enrollments1) =>
{
"125,171": []
"125,518": ['Computer Graphics']
"125,914": ['Computer Graphics']
"171,518": ['Data Structures', 'Image Processing']
"171,914": []
"518,914": ['Computer Graphics']
}



All Test Cases:
find_pairs(enrollments1)


'''



def find_pairs(enrollments):
    # Create a dictionary to store course enrollments for each student
    student_courses = {}

    # Iterate through the enrollments and populate the student_courses dictionary
    for student_id, course in enrollments:
        if student_id not in student_courses:
            student_courses[student_id] = set()
        student_courses[student_id].add(course)
    
    # Create a dictionary to store shared courses for each pair of students
    shared_courses = {}

    # Iterate through the student_courses dictionary to find shared courses
    students = sorted(student_courses.keys())
    
    for i in range(len(students)):
        for j in range(i + 1, len(students)):
            student1 = students[i]
            student2 = students[j]

            # Find courses that both students share
            common_courses = list(student_courses[student1] & student_courses[student2])

            # Sort the student IDs in ascending order to ensure consistent keys
            key = f"{student1},{student2}" if student1 < student2 else f"{student2},{student1}"

            # Store the shared courses in the shared_courses dictionary
            shared_courses[key] = common_courses
   

    return shared_courses

# Sample input
enrollments1 = [
  ["518", "Image Processing"],
  ["914", "CPP"],
  ["914", "Operating Systems"],
  ["171", "Data Structures"],
  ["518", "SAD"],
  ["518", "Computer Graphics"],
  ["171", "Image Processing"],
  ["171", "Software Engineering"],
  ["914", "Computer Graphics"],
  ["125", "Computer Graphics"],
  ["518", "Data Structures"],
]

# Call the function with the sample input
result = find_pairs(enrollments1)

# Print the result
print(result)

