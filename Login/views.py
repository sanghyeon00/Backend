from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


user_data = dict()


from django.shortcuts import render 
from django.http import JsonResponse
from myapp import gpt_prompt
import os
# Create your views here.
from .models import MyModel
def index(request):
    return HttpResponse("Communication start")


@api_view(['POST'])
def sign_up(request):
    check_name_id = request.data.get('id')
    try:
        MyModel.objects.get(id = check_name_id)
        return Response({'message': 'Fail'}, status=409)
    except:
        sign_name_id = request.data.get('id')
        sign_password = request.data.get('password')
        sign_password_2 = request.data.get('passwordcheack')
        sign_name = request.data.get('name')
        sign_student_id = request.data.get('studentid')
        sign_e_mail = request.data.get('email')
        sign_phone_number = request.data.get('phone')
        sign_year = request.data.get('year')
        sign_month = request.data.get('month')
        sign_day = request.data.get('day')
        sign_gender = request.data.get('gender')
        instance = MyModel(id = sign_name_id, password  = sign_password, name = sign_name, studentid  = sign_student_id, email  = sign_e_mail, phone = sign_phone_number, year = sign_year, month = sign_month, day = sign_day, gender = sign_gender)
        instance.save()
        return Response({'message': 'Success'}, status=status.HTTP_200_OK)
    sign_name_id = request.data.get('id')
    sign_password = request.data.get('password')
    sign_password_2 = request.data.get('passwordcheack')
    sign_name = request.data.get('name')
    sign_student_id = request.data.get('studentid')
    sign_e_mail = request.data.get('email')
    sign_phone_number = request.data.get('phone')
    sign_year = request.data.get('year')
    sign_month = request.data.get('month')
    sign_day = request.data.get('day')
    sign_gender = request.data.get('gender')
    instance = MyModel(name_id = sign_name_id, password  = sign_password, name = sign_name, student_id  = sign_student_id, e_mail  = sign_e_mail, phone_number = sign_phone_number, year = sign_year, month = sign_month, day = sign_day, gender = sign_gender)
    instance.save()


@api_view(['POST'])
def id_check(request):
    check_name_id = request.data.get('name_id')
    try:
        MyModel.objects.get(name_id = check_name_id)
        return Response({'message': 'Fail'}, status=409)
    except:
        return Response({'message': 'Success'}, status=status.HTTP_200_OK)
