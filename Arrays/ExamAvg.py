from arrayADT import Array2D

# Open the text file for reading.
with open( "ExamGrades.txt", "r" ) as gradeFile:
    # Extract the first two values which indicate the size of the array.
    numStudents = int( gradeFile.readline() )
    numExams = int( gradeFile.readline() )
    # Create the 2-D array to store the grades.
    examGrades = Array2D( numStudents, numExams )
    # Extract the grades from the remaining lines.
    i = 0
    for student in gradeFile :
        grades = student.split()
        for j in range(numExams):
            examGrades.__setItem__((i,j), int(grades[j]))
        i += 1
    # Close the text file.

# Compute each student's average exam grade.
for i in range(numStudents) :
    # Tally the exam grades for the ith student.
    total = 0
    for j in range( numExams ) :
        total += examGrades.__getItem__((i,j))
    # Compute average for the ith student.
    examAvg = total / numExams
    print( "%2d:    %6.2f" % (i+1, examAvg) )