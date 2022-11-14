from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from .models import Student, Assignment, AssignmentResult, Course
from statistics import mean, median, stdev
from django.contrib import messages
from.filters import *
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.

class AddStudent(TemplateView):
    template_name = "student_project/AddStudent.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,{})

    def post(self,request):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        town = request.POST["town"]
        student = Student()
        student.first_name = first_name
        student.last_name = last_name
        student.town = town
        student.save()
        messages.success(request, "student added successfuly", extra_tags= 'succes')
        url_list="RetreiveStudents"
        # return render(request, self.template_name,{})
        return redirect(url_list)

class RetreiveStudents(TemplateView):
    template_name = "student_project/RetreiveStudents.html"
    def get(self, request, *args, **kwargs):
        students=Student.objects.all()
        return render(request, self.template_name,{'students':students})
    
    
class updateStudent(TemplateView):
    template_name = "student_project/updateStudent.html"
    def get(self, request,pk, *args, **kwargs):
        student=Student.objects.get(id=pk)
        return render(request, self.template_name,{'student':student})

    def post(self,request,pk):
        student=Student.objects.get(id=pk)
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        town = request.POST["town"]
        student.first_name = first_name
        student.last_name = last_name
        student.town = town
        student.save()
        messages.success(request, "student updated successfuly", extra_tags= 'succes')
        url_list="RetreiveStudents"
        
        return redirect(url_list)

        

        

class deleteStudent(TemplateView):
    template_name = "student_project/deleteStudent.html"
    def get(self, request,pk, *args, **kwargs):
        student=Student.objects.get(id=pk)
        return render(request, self.template_name,{'student':student})

    def post (self,request,pk):
        Student.objects.get(id=pk).delete()
        messages.success(request, "Student deleted successfuly", extra_tags= 'succes')
        url_list="RetreiveStudents"
        return redirect(url_list)
    
########################assignment
class AddAssignment(TemplateView):
    template_name = "assignment_project/AddAssignment.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,{})

    def post(self,request):
        name = request.POST["name"]
        difficulty = request.POST["difficulty"]
        
        assignment = Assignment()
        assignment.name = name
        assignment.difficulty = difficulty
       
        assignment.save()
        messages.success(request, "Assignment added successfuly", extra_tags= 'succes')
        url_list="RetreiveAssignments"
        # return render(request, self.template_name,{})
        return redirect(url_list)

class RetreiveAssignments(TemplateView):
    template_name = "assignment_project/RetreiveAssignment.html"
    def get(self, request, *args, **kwargs):
        assignments=Assignment.objects.all()
        return render(request,self.template_name,{'assignments':assignments})

class RetreiveAssignmentsFilter(TemplateView):
    template_name = "assignment_project/RetreiveAssignment.html"
    def get(self, request, *args, **kwargs):
        assignments=Assignment.objects.all()
        return render(request,self.template_name,{'assignments':assignments})
    def post(self,request):
        key = request.POST["key"]
        assignments=Assignment.objects.filter(Q(name__icontains=key))
        
        return render(request, self.template_name,{'assignments':assignments})
class deleteAssignment(TemplateView):
    template_name = "assignment_project/deleteAssignment.html"
    def get(self, request,pk, *args, **kwargs):
        assignment=Assignment.objects.get(id=pk)
        return render(request, self.template_name,{'assignment':assignment})
   
    def post (self,request,pk):
        Assignment.objects.get(id=pk).delete()
        messages.success(request, "Assignment deleted successfuly", extra_tags= 'succes')
        url_list="RetreiveAssignments"
        return redirect(url_list)
class updateAssignment(TemplateView):
    template_name = "assignment_project/updateAssignment.html"
    def get(self, request,pk, *args, **kwargs):
        assignment=Assignment.objects.get(id=pk)
        return render(request, self.template_name,{'assignment':assignment})

    def post(self,request,pk):
        
        name = request.POST["name"]
        difficulty = request.POST["difficulty"]
        
        assignment = Assignment.objects.get(id=pk)
        assignment.name = name
        assignment.difficulty = difficulty
        assignment.save()
        messages.success(request, "assignment updated successfuly", extra_tags= 'succes')
        url_list="RetreiveAssignments"
        return redirect(url_list)
########################assignmentResult
class AddAssignmentResult(TemplateView):
    template_name = "assignmentResult_project/AddAssignmentResult.html"
    def get(self, request, *args, **kwargs):
        assignments= Assignment.objects.all()
        students= Student.objects.all()
        return render(request, self.template_name,{'assignments':assignments,'students':students})

    def post(self,request):
        id_student = request.POST["student"]
        assignment = request.POST["assignment"]
        grade = request.POST["grade"]
        
        assignmentResult = AssignmentResult()
        assignmentResult.id_student = Student.objects.get(id=id_student)
        assignmentResult.assignment = Assignment.objects.get(id=assignment)
        assignmentResult.grade = grade
       
        assignmentResult.save()
        messages.success(request, "Assignment result added successfuly", extra_tags= 'succes') 
        url_list="RetreiveAssignmentResults"
        # return render(request, self.template_name,{})
        return redirect(url_list)

class RetreiveAssignmentResults(TemplateView):
    template_name = "assignmentResult_project/RetreiveAssignmentResults.html"
    def get(self, request, *args, **kwargs):
        assignmentResults=AssignmentResult.objects.all()
        return render(request,self.template_name,{'assignmentResults':assignmentResults})

class RetreiveAssignmentsResultsFilter(TemplateView):
    template_name = "assignmentResult_project/RetreiveAssignmentResults.html"
    def get(self, request, *args, **kwargs):
        assignmentResults=AssignmentResult.objects.all()
        return render(request,self.template_name,{'assignmentResults':assignmentResults})
    def post(self,request):
        key = request.POST["key"]
        assignmentResults=AssignmentResult.objects.filter(Q(assignment__icontains=key))
 
        return render(request, self.template_name,{'assignmentResults':assignmentResults})
class deleteAssignmentResult(TemplateView):
    
    template_name = "assignmentResult_project/deleteAssignment.html"
    def get(self, request,pk, *args, **kwargs):
        assignment=AssignmentResult.objects.get(id=pk)
        return render(request, self.template_name,{'assignment':assignment})
   
   
    def post (self,request,pk):
        AssignmentResult.objects.filter(id=pk).delete()
        messages.success(request, "Assignment Result deleted successfuly", extra_tags= 'succes')
        url_list="RetreiveAssignmentResults"
        return redirect(url_list)

class updateAssignmentResult(View):
    template_name = "assignmentResult_project/updateAssignment.html"
    def get(self, request,pk, *args, **kwargs):
        assignment=AssignmentResult.objects.get(id=pk)
        return render(request, self.template_name,{'assignment':assignment})

    def post(self,request,pk):
        
        id_student = request.POST["student"]
        assignment = request.POST["assignment"]
        grade = request.POST["grade"]

        assignmentResult = AssignmentResult.objects.get(id=pk)
        assignmentResult.id_student = Student.objects.get(id=id_student)
        assignmentResult.assignment = Assignment.objects.get(id=assignment)
        assignmentResult.grade = grade
        assignmentResult.save()
        messages.success(request, "assignment updated successfuly", extra_tags= 'succes')
        url_list="RetreiveAssignments"
        return redirect(url_list)
class StudentGrades(TemplateView):
    template_name = "student_project/StudentGrades.html"
    def get(self, request,pk, *args, **kwargs):
        
        assignmentResults= AssignmentResult.objects.filter(id_student=pk)
        result_grades=[]
        average=0
        for assignmentResult in assignmentResults:
                result_grades.append(assignmentResult.grade)
        if len(result_grades)>= 2:
            min_grade = min(result_grades)
            grades = [x for x in result_grades if x != min_grade]
            if len(grades)==0:
                grades = [min_grade]
            average= mean(grades)
        elif  len(result_grades)==0:
            average= 0
        elif len(result_grades)==1:
            average= round(result_grades[0],1)
        return render(request,self.template_name,{'assignmentResults':assignmentResults,'average': average})



    

class StudentCourses(TemplateView):
    template_name = "student_project/StudentCourses.html"
    def get(self, request,pk, *args, **kwargs):
        courses=Course.objects.filter(students=pk)
        return render(request, self.template_name,{'courses':courses})




class AddCourse(TemplateView):
    template_name = "course_project/AddCourse.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,{})

    def post(self,request):
        name = request.POST["name"]
        course = Course()
        course.name = name
        course.save()
        messages.success(request, "Course added successfuly", extra_tags= 'succes')
        url_list="RetreiveCourses"
        return redirect(url_list)

class RetreiveCourses(TemplateView):
    template_name = "course_project/RetreiveCourses.html"
    def get(self, request, *args, **kwargs):
        courses=Course.objects.all()
        return render(request, self.template_name,{'courses':courses})

class RetreiveCoursesFilter(TemplateView):
    template_name = "course_project/RetreiveCourses.html"
    def get(self, request, *args, **kwargs):
        courses=Course.objects.all()
        return render(request, self.template_name,{'courses':courses})
    def post(self,request):
        key = request.POST["key"]
        course = Course()
        courses=Course.objects.filter(Q(name__icontains=key))
        url_list="RetreiveCourses"
        return render(request, self.template_name,{'courses':courses})
    

class deleteCourse(View):
    template_name = "course_project/deleteCourse.html"
    def get(self, request,pk, *args, **kwargs):
        course=Course.objects.get(id=pk)
        return render(request, self.template_name,{'course':course})
   
    def post (self,request,pk):
        Course.objects.filter(id=pk).delete()
        messages.success(request, "Course deleted successfuly", extra_tags= 'succes')
        url_list="RetreiveCourses"
        return redirect(url_list) 
class deleteStudentCourse(View):
   
    def post (self,request,id,pk):
        student = Student.objects.get(id=id)
        course= Course.objects.get(id=pk)
        course.students.remove(student)
        messages.success(request, "Student deleted successfuly", extra_tags= 'succes')
        url_list="RetreiveCourses"
        return redirect(url_list)     


class addStudentCourse(TemplateView): 
    template_name = "course_project/addStudentCourse.html"
    def get(self, request,pk, *args, **kwargs):
        list_id=[]
        course=Course.objects.get(id=pk) 
        students_course= course.students.all()
        for student in students_course:
            list_id.append(student.id)
        students= Student.objects.filter(~Q(id__in=list_id))
        return render(request, self.template_name,{'students':students})
    def post(self,request,pk):
        course=Course.objects.get(id=pk)

        students = request.POST.getlist('students')
        for student in students:
            #if course.students.get()
            if Student.objects.filter(id=student).exists():
                student = Student.objects.get(id=student)
                course.students.add(student)
        messages.success(request, "Students added successfuly", extra_tags= 'succes')
        url_list="RetreiveCourses"
        return redirect(url_list)

class studentsCourse(TemplateView):
    template_name = "course_project/studentsCourse.html"
    def get(self, request,pk, *args, **kwargs):
        course=Course.objects.get(id=pk)
        students= course.students.all()
        return render(request, self.template_name,{'students':students, 'course':course}) 


class StatisticsCourse(TemplateView):
    template_name = "course_project/StatisticsCourse.html"
    def get(self, request,pk, *args, **kwargs):
        course=Course.objects.get(id=pk)
        students= course.students.all()
        grades= []
        for student in students:
            assignmentResults= AssignmentResult.objects.filter(id_student=student)
            for assignmentResult in assignmentResults:
                grades.append(assignmentResult.grade)
        if len(grades) == 0:
            number_student= 'no data'
            mean_grades= 'no data'
            max_grades= 'no data'
            min_grades='no data'
            median_grades='no data'
            stdev_grades= 'no data'

        elif len(grades)>1 :
            number_student= students.count()
            mean_grades= round(mean(grades),1)
            max_grades=round(max(grades),1)
            min_grades=round(min(grades),1)
            median_grades=round(median(grades),1)
            stdev_grades=round(stdev(grades),1)
        else :
            number_student= students.count()
            mean_grades= round(grades[0],1)
            max_grades=round(grades[0],1)
            min_grades=round(grades[0],1)
            median_grades=round(grades[0],1)
            stdev_grades=round(grades[0],1)


        
        return render(request, self.template_name,{'course':course,'number_student':number_student, 'mean_grades':mean_grades, 'max_grades':  max_grades,'min_grades':min_grades,'median_grades':median_grades,'stdev_grades':stdev_grades})


####################### Assign

class AssignStudent(TemplateView):
    template_name = "student_project/AssignStudent.html"
    def get(self, request,pk, *args, **kwargs):
        """list_id =[]
        student=Student.objects.get(id=pk)
        assignmentResults=AssignmentResult.objects.filter(id_student=student)
        if assignmentResults.count()==0:
            assignments= Assignment.objects.all()
        else:
            for  assignmentResult in assignmentResults:
                list_id.append(assignmentResult.id)
        assignments= AssignmentResult.objects.filter(~Q(id__in=list_id))"""
        assignments= Assignment.objects.all()
        return render(request, self.template_name,{'assignments':assignments})

    def post(self,request,pk):
        student=Student.objects.get(id=pk)
        assignment = request.POST["assignment"]
        assignment_objet = Assignment.objects.get(id=assignment)
        grade=  1 -(float(student.energy)*float(assignment_objet.difficulty))
        student.energy= float(student.energy)- (float(student.energy)*float(assignment_objet.difficulty))
    
        if student.energy < 0:
            student.energy=0
        
        assignmentResult = AssignmentResult() 
        assignmentResult.id_student = student
        assignmentResult.assignment = assignment_objet
        assignmentResult.grade = grade
        assignmentResult.save()
        student.save()
        
        messages.success(request, "Assignment added successfuly", extra_tags= 'succes')
        url_list="RetreiveStudents"
        return redirect(url_list)
class SleepStudent(TemplateView):
    template_name = "student_project/SleepStudent.html"
    def get(self, request, *args, **kwargs):
    
        return render(request, self.template_name,{})

    def post(self,request,pk):
        student=Student.objects.get(id=pk)
        hours = request.POST["hours"]
        if float(student.energy)==0.0:
           student.energy=float(hours)*0.1
        else:
            student.energy= float(student.energy)*(1+ float(hours)*0.1)
        if float(student.energy)>1.0:
            student.energy=1.0
        student.save()
        messages.success(request, "energy updated successfuly", extra_tags= 'succes')
        url_list="RetreiveStudents"
        return redirect(url_list)

class AssignStudentCourse(TemplateView):
    template_name = "assignment_project/AddAssignment.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,{})

    def post(self,request,pk):
        name = request.POST["name"]
        difficulty = request.POST["difficulty"]
        
        assignment = Assignment()
        assignment.name = name
        assignment.difficulty = difficulty
       
        assignment.save()
        course=Course.objects.get(id=pk)
        students= course.students.all()
        for student_id in students:
            student= Student.objects.get(id=student_id.id)
            a = student.energy
            b= assignment.difficulty
            grade=  1 -(float(a)*float(b))
            print(grade)
            student.energy= student.energy- (float(student.energy)*float(assignment.difficulty))
            if student.energy < 0:
                student.energy=0
            assignmentResult = AssignmentResult()
            assignmentResult.id_student = student
            assignmentResult.assignment = assignment
            assignmentResult.grade = grade
            assignmentResult.save()
        messages.success(request, "Assignment added successfuly", extra_tags= 'succes')
        url_list="RetreiveCourses"
        return redirect(url_list)



    







    







