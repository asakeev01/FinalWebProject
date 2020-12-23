from django.shortcuts import render

from .models import *


def departments_list(request):
    departments = Department.objects.all()
    return render(request, 'departments.html', locals())


def department(request, pk):
    department = Department.objects.get(pk = pk)
    courses = department.course.all().order_by('course')
    days_of_week = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY']
    return render(request, 'main.html', locals())
