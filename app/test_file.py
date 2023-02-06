import pytest    
from app.models import Student, Assignment    
from app.views import RetreiveStudents
from django.urls import reverse
from django.test import Client, TestCase

@pytest.mark.django_db #give test access to database  
def test_student_create():    
    # Create  data       
    student = Student.objects.create(first_name="chaima",last_name="zarrouq",town="rabat")    
    # Assert the  data saved as expected       
    assert student.first_name=="chaima"      
    assert student.last_name=="zarrouq"
    assert student.town=="rabat"

@pytest.mark.django_db 
def test_assignment_create():          
    assignment = Assignment.objects.create(name="Python",difficulty="0.5")          
    assert assignment.name=="Python"      
    assert assignment.difficulty=="0.5"
    
class Test_views(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.list_students=reverse('RetreiveStudents')
        self.list_courses=reverse('RetreiveCourses')
        self.list_assignments=reverse('RetreiveAssignments')
        self.list_assignmentsresult=reverse('RetreiveAssignmentResults') 
        self.student1= Student.objects.create(first_name="chaima",last_name="zarrouq",town="rabat")
        
    def test_student_list_GET(self):
        response = self.client.get(self.list_students)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'student_project/RetreiveStudents.html')

    def test_courses_list_GET(self):
        response = self.client.get(self.list_courses)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'course_project/RetreiveCourses.html')

    def test_assignments_list_GET(self):
        response = self.client.get(self.list_assignments)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'assignment_project/RetreiveAssignment.html') 

    def test_assignmentsresult_list_GET(self):
        response = self.client.get(self.list_assignmentsresult)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'assignmentResult_project/RetreiveAssignmentResults.html')  

    def test_student_Grade_GET(self):
        response = self.client.get()
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'student_project/')
        
    def test_Statistics_Course_GET(self):
        response = self.client.get()
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'student_project/')

    def test_POST_add_AssignmentResult(self):
        pass

    def test_POST_add_Student_to_Course(self):
        pass

    def test_DEL_delete_AssignmentResult(self):
        pass


    def test_PUT_update_AssignmentResult(self):
        pass

    

    
  

    


    
    
