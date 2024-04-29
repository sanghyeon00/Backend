from django.db import models
from Login.models import school
class course(models.Model):
    name = models.CharField(max_length=30, unique=True)  # å�� ������ �����ϴ� �ʵ�
    def __str__(self):
        # �� �޼ҵ�� ���� �ν��Ͻ��� ���ڿ��� ǥ���� �� ���˴ϴ�.
        return f"{self.name}"
    
class professor_lecture(models.Model):
    username = models.CharField(max_length=30)
    course_name = models.CharField(max_length=30)
    course_id = models.CharField(max_length=30)
    name = models.CharField(max_length=30)

class student_lecture(models.Model):
    username = models.CharField(max_length=30)
    course_name = models.CharField(max_length=30)
    course_id = models.CharField(max_length=30)
    lecture_id = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    
class problem(models.Model):
    professor_id = models.CharField(max_length=30)
    lecture_id = models.CharField(max_length=30)
    problem_1 = models.CharField(max_length=1000, null=True)
    problem_2 = models.CharField(max_length=1000, null=True)
    problem_3 = models.CharField(max_length=1000, null=True)
    problem_4 = models.CharField(max_length=1000, null=True)
    problem_5 = models.CharField(max_length=1000, null=True)
    problem_6 = models.CharField(max_length=1000, null=True)
    problem_7 = models.CharField(max_length=1000, null=True)
    problem_8 = models.CharField(max_length=1000, null=True)
    problem_9 = models.CharField(max_length=1000, null=True) 
    problem_10 = models.CharField(max_length=1000, null=True)
    
class answer(models.Model):
    student_id = models.CharField(max_length=30)
    lecture_id = models.CharField(max_length=30)
    answer_1 = models.CharField(max_length=1000, null=True)
    answer_2 = models.CharField(max_length=1000, null=True)
    answer_3 = models.CharField(max_length=1000, null=True)
    answer_4 = models.CharField(max_length=1000, null=True)
    answer_5 = models.CharField(max_length=1000, null=True)
    answer_6 = models.CharField(max_length=1000, null=True)
    answer_7 = models.CharField(max_length=1000, null=True)
    answer_8 = models.CharField(max_length=1000, null=True)
    answer_9 = models.CharField(max_length=1000, null=True) 
    answer_10 = models.CharField(max_length=1000, null=True)