import student_management_app
from django.http import response
from django.test import TestCase,Client, client
from django.urls import reverse
from student_management_app.models import *
import json


class TestView(TestCase):

    def test_dologin(self):
        client = Client()
        response = client.post(reverse('doLogin'))
        self.assertEquals(response.status_code,302)
        self.assertTemplateNotUsed(response,'student_management_app/login.html')



    def test_editstaff(self):
        client = Client()
        response = client.post(reverse('edit_staff_save'))
        self.assertEquals(response.status_code,302)
        self.assertTemplateNotUsed(response,'student_management_app/edit_staff_template.html')




    def test_staff_apply_leave_save(self):
        client = Client()
        response = client.post(reverse('staff_apply_leave_save'))
        self.assertEquals(response.status_code,302)
        self.assertTemplateNotUsed(response,'student_management_app/edit_staff_template.html')


    
    
    def test_student_feedback_save(self):
        client = Client()
        response = client.post(reverse('student_feedback_save'))
        self.assertEquals(response.status_code,302)
        self.assertTemplateNotUsed(response,'student_management_app/edit_staff_template.html')
