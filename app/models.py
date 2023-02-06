from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    town = models.CharField(max_length=30)
    energy = models.FloatField(default=0)
    
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Assignment(models.Model):
    name= models.CharField(max_length=30)
    difficulty= models.FloatField()
    def __str__(self):
        return "%s" % (self.name)

class AssignmentResult(models.Model):
    id_student=models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    grade=models.FloatField()


class Course(models.Model):
    name=models.CharField(max_length=30, null=True)
    students= models.ManyToManyField(Student)
    #date_creation= models.DateField(default=datetime)
    def __str__(self):
        return "%s %s" % (self.name)

