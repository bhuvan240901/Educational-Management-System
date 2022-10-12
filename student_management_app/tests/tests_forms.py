from django.test import SimpleTestCase
from student_management_app.forms import *

class TestForms(SimpleTestCase):

    def test_AddStudent(self):
        form = AddStudentForm(data={
            'email': 'bhuvan24@gmail.com',
            'password': 'bhuvan24090',
            'first_name':'Bhuvan',
            'last_name':'P',
            'username':'bhuvan1',
            'address':'Andhra',


        })
        self.assertFalse(form.is_valid())

    def test_no_data(self):
        form=AddStudentForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),9)
