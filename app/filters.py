import django_filters
from.models import Student, Course

class CourseFilter(django_filters.FilterSet):
    class Meta:
        model = Course
        fields= ('name',)
        