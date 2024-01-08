from django.contrib import admin
from foreignkeyapp.models import Course
from foreignkeyapp.models import Student

admin.site.register(Course)
admin.site.register(Student)


# Register your models here.
