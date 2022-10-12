from django.conf.urls import url
from django.test import SimpleTestCase
from django.urls import resolve,reverse
from student_management_app.views import doLogin,loginPage,get_user_details,logout_user
from student_management_app.HodViews import *
from student_management_app.StaffViews import *
from student_management_app.StudentViews import *



class TestUrls(SimpleTestCase):

    def test_login_url(self):
        url=reverse('login') 
        self.assertEquals(resolve(url).func,loginPage)



    def test_home_url(self):
        url=reverse('doLogin') 
        self.assertEquals(resolve(url).func,doLogin)



    def test_userdetails_url(self):
        url=reverse('get_user_details') 
        self.assertEquals(resolve(url).func,get_user_details)



    def test_logout_url(self):
        url=reverse('logout_user') 
        self.assertEquals(resolve(url).func,logout_user)



    def test_editstudent_url(self):
        url=reverse('edit_student_save') 
        self.assertEquals(resolve(url).func,edit_student_save)



    def test_addsubject_url(self):
        url=reverse('add_subject') 
        self.assertEquals(resolve(url).func,add_subject)