from django.db import models
from Login.models import school
class course(models.Model):
    name = models.CharField(max_length=30, unique=True)  # 책의 제목을 저장하는 필드
    def __str__(self):
        # 이 메소드는 모델의 인스턴스를 문자열로 표현할 때 사용됩니다.
        return f"{self.name}"
    
class professor_lecture(models.Model):
    username = models.ForeignKey(school, to_field='username', on_delete=models.CASCADE)
    course_name = models.ForeignKey(course, to_field='name', on_delete=models.CASCADE, related_name='lectures_by_name_professor')
    course_id = models.ForeignKey(course, to_field='id', on_delete=models.CASCADE, related_name='lectures_by_id_professor')

class student_lecture(models.Model):
    username = models.ForeignKey(school, to_field='username', on_delete=models.CASCADE)
    course_name = models.ForeignKey(course, to_field='name', on_delete=models.CASCADE, related_name='lectures_by_name_student')
    course_id = models.ForeignKey(course, to_field='id', on_delete=models.CASCADE,related_name='lectures_by_id_student')
    lecture_id = models.ForeignKey(professor_lecture, on_delete=models.CASCADE)
    
class problem(models.Model):
    professor_id = models.ForeignKey(school, on_delete=models.CASCADE)
    lecture_id = models.ForeignKey(professor_lecture, on_delete=models.CASCADE)
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
    student_id = models.ForeignKey(school, on_delete=models.CASCADE)
    lecture_id = models.ForeignKey(professor_lecture, on_delete=models.CASCADE)
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