# -----------------------------------------------------------------------------
# Name:        Grades
# Purpose:     Grade calculator - assignment #2
#
# Author:      Maksim Nikiforov
# Date:        10/09/2016
# -----------------------------------------------------------------------------
"""
Computes the letter grade earned in a fictional course.

This program prompts the user to enter grades earned on different
components of a course. The program will keep prompting for grades
until the user presses 'Enter' without typing any grade.
"""

input_not_blank = True                      # Initiate variable for while loop
all_grades = []                             # Initiate empty list of all grades
min_grade = 0                               # Initiate min. grade at 0

while input_not_blank:
    grade = input("Please enter a grade: ")
    if grade and 0 <= float(grade) <= 100:  # Ensure grade is in valid range
        all_grades.append(float(grade))     # Add valid grades to list
    elif grade and 0 > float(grade) > 100:  # Discard out-of-range grades
        continue
    elif not grade and len(all_grades) < 1: # Ask for at least 1 grade
        print("Error: Please enter at least 1 grade!")
    if not grade and len(all_grades) >= 1:  # Stop loop when list has 1+ grades
        input_not_blank = False             # and user input is empty

if len(all_grades) >= 4:                    # Check if list has 4 grades
    min_grade = min(all_grades)             # Save value of lowest grades
    all_grades.remove(min_grade)            # Remove lowest grade from list
course_average = round(sum(all_grades)/len(all_grades), 1)  # Calc. course avg.

if course_average >= 90:                    # Letter grade conditions
    letter_grade = 'A'
elif course_average >= 80 <= 89.9:
    letter_grade = 'B'
elif course_average >= 70 <= 79.9:
    letter_grade = 'C'
elif course_average >= 60 <= 69.9:
    letter_grade = 'D'
else:
    letter_grade = 'F'

if min_grade:                               # Print lowest grade when available
    print("The lowest grade dropped:", min_grade)

print("Course average:", course_average)    # Print grade statistics
print("Letter grade:", letter_grade)

print("Based on the following grades:")     # Loop through and print all grades
for grade in all_grades:
    print(grade)
