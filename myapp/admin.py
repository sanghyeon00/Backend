from django.contrib import admin

from .models import course, professor_lecture, student_lecture, problem, answer
# Register your models here.
admin.site.register(course)
admin.site.register(professor_lecture)
admin.site.register(student_lecture)
admin.site.register(problem)
admin.site.register(answer)