def calculate_gp():
    '''
        This functions takes in the number of courses offered, unit of each course and 
        the grades and returns a GPA using 5-point scale
    '''
    grades = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}
    student_grade = 0
    units = 0
    num_of_courses = int(input('How many courses did you offer: '))
    for i in range(num_of_courses):
        grade = input('Enter your grade in a course (A-F): ').upper()
        unit = int(input('How many units was the course: '))
        student_grade += grades[grade]*unit
        units += unit
    gp = student_grade/units 

    print('Your GPA is ',round(gp,2))

calculate_gp()
