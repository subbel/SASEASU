from django.test import TestCase

from .models import Student, Event

class StudentModelTest(TestCase):
    def testStudentCreated(self):
        temp_stud = Student()
        temp_stud.firstname =  "Subbel"
        self.assertIs(temp_stud.firstname, "Subbel")

# Create your tests here.
