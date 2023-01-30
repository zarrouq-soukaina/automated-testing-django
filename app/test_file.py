import pytest    
from app.models import Student, Assignment    
from app.views import RetreiveStudents
from django.test.client import RequestFactory
from django.urls import reverse
from django.test import Client, TestCase

@pytest.mark.django_db #give test access to database  
def test_student_create():    
    # Create dummy data       
    student = Student.objects.create(first_name="chaima",last_name="zarrouq",town="rabat")    
    # Assert the dummy data saved as expected       
    assert student.first_name=="chaima"      
    assert student.last_name=="zarrouq"
    assert student.town=="rabat"

@pytest.mark.django_db #give test access to database  
def test_assignment_create():    
    # Create dummy data       
    assignment = Assignment.objects.create(name="Python",difficulty="0.5")    
    # Assert the dummy data saved as expected       
    assert assignment.name=="Python"      
    assert assignment.difficulty=="0.5"


class Test_views(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.list_students=reverse('RetreiveStudents')  
        #self.grade_student=reverse('StudentGrades', args=[])  
    def test_student_list_GET(self):
        response = self.client.get(self.list_students)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'student_project/RetreiveStudents.html')  

    


    
    
