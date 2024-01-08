from django.shortcuts import render,redirect
from foreignkeyapp.models import Course
from foreignkeyapp.models import Student


# Create your views here.
def home(request):
    return render(request,'home.html')

def course(request):
    return render(request,'course.html')

def student(request):
    courses=Course.objects.all()
    return render(request,'student.html',{'course':courses})


def add_course(request):
    if request.method=='POST':
        course_name=request.POST['course']
        course_fee=request.POST['fee']
        course=Course(course_name=course_name,fee=course_fee)
        course.save()
        return redirect('course')
    
def add_student(request):
    if request.method=='POST':
        student_name=request.POST['name']
        student_address=request.POST['address']
        age=request.POST['age']
        jdate=request.POST['jdate']
        sel=request.POST['sel']
        course1 = Course.objects.get(id=sel)
        student = Student(student_name=student_name, student_address=student_address, student_age=age, joining_date=jdate, course=course1)
        student.save()
        return redirect('student')
    
def show(request):
    student=Student.objects.all()
    return render(request,'show.html',{'students':student})

def edit(request,pk):
    student=Student.objects.get(id=pk)
    course=Course.objects.all()
    return render(request,'edit.html',{'stud':student,'course':course})

def editdb(request,pk):
    if request.method=='POST':
        student=Student.objects.get(id=pk)
        student.student_name=request.POST['name']
        student.student_address=request.POST['address']
        student.student_age=request.POST['age']
        student.joining_date=request.POST['jdate']
        sel=request.POST['sel']
        course1 = Course.objects.get(id=sel)
        student.course=course1
        student.save()
        return redirect('show')
    return render(request,'edit.html')

def delete(request,pk):
    stud=Student.objects.get(id=pk)
    stud.delete()
    return redirect('show')
    
