from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.views import LogoutView
from django.views.generic.base import TemplateView

from .views import RetreiveStudents,AddStudent,RetreiveCourses,AddCourse,RetreiveAssignments,RetreiveAssignmentResults,addStudentCourse,studentsCourse,AddAssignment,StudentGrades,AddAssignmentResult,StatisticsCourse,AssignStudent,SleepStudent,AssignStudentCourse,StudentCourses,deleteStudent,RetreiveCoursesFilter,deleteCourse,deleteAssignment,deleteAssignmentResult,RetreiveAssignmentsFilter,RetreiveAssignmentsResultsFilter, deleteStudentCourse,updateStudent,updateAssignment,updateAssignmentResult
urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("logout", LogoutView.as_view(next_page="home"), name='logout'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('AddStudent', AddStudent.as_view(), name='AddStudent'),
    path('RetreiveStudents', RetreiveStudents.as_view(), name='RetreiveStudents'),
    path('StudentGrades/<int:pk>', StudentGrades.as_view(), name='StudentGrades'),
    path('deleteStudent/<int:pk>', deleteStudent.as_view(), name='deleteStudent'),
    path('updateStudent/<int:pk>', updateStudent.as_view(), name='updateStudent'),
    path('AssignStudent/<int:pk>', AssignStudent.as_view(), name='AssignStudent'),
    path('SleepStudent/<int:pk>', SleepStudent.as_view(), name='SleepStudent'),
    path('StudentCourses/<int:pk>', StudentCourses.as_view(), name='StudentCourses'),

    path('RetreiveCourses', RetreiveCourses.as_view(), name='RetreiveCourses'),
    path('RetreiveCoursesFilter', RetreiveCoursesFilter.as_view(), name='RetreiveCoursesFilter'),
    path('AddCourse', AddCourse.as_view(), name='AddCourse'),
    path('addStudentCourse/<int:pk>', addStudentCourse.as_view(), name='addStudentCourse'),
    path('studentsCourse/<int:pk>', studentsCourse.as_view(), name='studentsCourse'),
    path('StatisticsCourse/<int:pk>', StatisticsCourse.as_view(), name='StatisticsCourse'),
    path('deleteCourse/<int:pk>', deleteCourse.as_view(), name='deleteCourse'),
    path('deleteStudentCourse/<int:id>/<int:pk>', deleteStudentCourse.as_view(), name='deleteStudentCourse'),
    path('AssignStudentCourse/<int:pk>', AssignStudentCourse.as_view(), name='AssignStudentCourse'),


    path('RetreiveAssignments', RetreiveAssignments.as_view(), name='RetreiveAssignments'),
    path('RetreiveAssignmentsFilter', RetreiveAssignmentsFilter.as_view(), name='RetreiveAssignmentsFilter'),
    path('AddAssignment', AddAssignment.as_view(), name='AddAssignment'),
    path('deleteAssignment/<int:pk>', deleteAssignment.as_view(), name='deleteAssignment'),
     path('updateAssignment/<int:pk>', updateAssignment.as_view(), name='updateAssignment'),


    path('RetreiveAssignmentResults', RetreiveAssignmentResults.as_view(), name='RetreiveAssignmentResults'),
    path('RetreiveAssignmentsResultsFilter', RetreiveAssignmentsResultsFilter.as_view(), name='RetreiveAssignmentsResultsFilter'),
    path('AddAssignmentResult', AddAssignmentResult.as_view(), name='AddAssignmentResult'),
    path('deleteAssignmentResult/<int:pk>', deleteAssignmentResult.as_view(), name='deleteAssignmentResult'),
    path('updateAssignmentResult/<int:pk>',updateAssignmentResult.as_view(), name='updateAssignmentResult'),





    


]
