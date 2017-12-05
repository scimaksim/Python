# -----------------------------------------------------------------------------
# Name:        college
# Purpose:     class definitions for a college environment
#
# Author:      Maksim Nikiforov
#
# -----------------------------------------------------------------------------
"""
Module to describe a college setting.

"""


class Person(object):
    """
    Represent a person affiliated with the college.

    Arguments:
    name (string): person's name
    cid (int): college id number - 8 digits
    email (string): email address - defaults to the empty string

    Attributes:
    name (string): person's name
    cid (int): college id number - 8 digits
    email (string): email address
    """

    def __init__(self, name, cid, email=''):
        self.name = name
        self.cid = cid
        self.email = email

    def __str__(self):
        result = 'NAME: {}\n ID: {}\n EMAIL: {} \n'.format(self.name,
                                                           self.cid,
                                                           self.email)
        return result


class Student(Person):
    """
    Represent a student affiliated with the college.

    Arguments:
    name (string): person's name
    cid (int): college id number - 8 digits
    email (string): email address - defaults to the empty string

    Attributes:
    name (string): person's name
    cid (int): college id number - 8 digits
    email (string): email address
    courses (dictionary): key is the unique course id (string), value is the
    grade earned in the course
    """

    def __init__(self, name, cid, email=''):
        self.courses = {}
        super().__init__(name, cid, email)

    def add_course(self, course):
        """
        Add a given course to the student's courses

        Parameter:
        course (string): the unique course ID
        Returns:
        the modified student object
        """
        try:
            # Check if student is already enrolled in the course
            if course in self.courses:
                raise NameError('Student is already registered '
                                'for this course')
            else:
                self.courses[course] = 0
        except NameError:
            raise
        return self

    @staticmethod
    def valid_grade(grade):
        """
        Verify that a given grade is valid (between 0 and 4 inclusive)

        Parameter:
        grade (int): grade for a given course
        Returns:
        boolean based on validity of entered grade
        """
        if 0 <= grade <= 4:
            return True
        else:
            return False

    def update_grade(self, course, grade):
        """
        Update the student's grade in a given course

        Parameter:
        course (string): the unique course ID
        grade (int): grade for the given course
        Returns:
        the modified student object
        """
        try:
            if course in self.courses:
                # Check that grade is between 0 and 4 before updating course
                if self.valid_grade(grade):
                    self.courses[course] = grade
                else:
                    raise ValueError('Grade specified is invalid')
            else:
                raise NameError('Student is not registered for this course')
        except ValueError:
            raise
        return self

    @property
    def gpa(self):
        """ Calculate the gpa of a given student on the fly """
        if self.courses:
            return sum(self.courses.values()) / len(self.courses)
        else:
            return 0


