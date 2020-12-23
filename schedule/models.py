from django.db import models


COURSES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
]

MAX_LESSONS = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7')
]

SUBJECTS = [
    ('Mathematics', 'Mathematics'),
    ('Computer Science', 'Computer Science'),
    ('Physics', 'Physics'),
    ('Russian Language', 'Russian Language'),
]

class Department(models.Model):
    department_name = models.CharField(max_length = 50)


    def __str__(self):
        return self.department_name


class Course(models.Model):
    department = models.ForeignKey(Department, on_delete = models.CASCADE, related_name = 'course')
    course = models.CharField(max_length = 30, choices = COURSES)
    quantity_of_groups = models.PositiveIntegerField()


    def __str__(self):
        return  self.course + " course of " + str(self.department) + " department " + str(self.pk)


class Teacher(models.Model):
    name = models.CharField(max_length = 30)
    surname = models.CharField(max_length = 30)

    def __str__(self):
        return self.name + " " + self.surname


class Subject(models.Model):
    sub_name = models.CharField(max_length = 30, choices = SUBJECTS)
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE, related_name = 'subject')
    course = models.ForeignKey(Course, on_delete = models.CASCADE, related_name = 'subject')
    lessons_per_week = models.CharField(max_length = 30, choices = MAX_LESSONS)


    def __str__(self):
        return self.sub_name