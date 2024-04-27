from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken  # Refresh 토큰 생성을 위한 클래스
from rest_framework import status  # HTTP 상태 코드
from rest_framework.response import Response  # DRF 응답 클래스
from rest_framework.views import APIView  # DRF API 뷰 클래스
from django.contrib.auth import authenticate  # Django의 인증 함수

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
        return Response({'message': 'Fail'}, status=status.HTTP_200_OK)
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


@api_view(['POST'])
def id_check(request):
    check_name_id = request.data.get('name_id')
    try:
        MyModel.objects.get(name_id = check_name_id)
        return Response({'message': 'Fail'}, status=409)
    except:
        return Response({'message': 'Success'}, status=status.HTTP_200_OK)
    
class CustomTokenObtainPairView(APIView):
    def post(self, request, *args, **kwargs):
        # 요청에서 username과 password를 가져옵니다.
        print(3)
        username = request.data.get('username')
        password = request.data.get('password')
        
        # Django의 authenticate 함수를 사용하여 사용자 인증을 시도합니다.
        try:
            user = MyModel.objects.get(id = username)

        # 사용자 인증이 성공한 경우
            if user.password == password:
                # 사용자를 위한 새로운 refresh 토큰과 access 토큰을 생성합니다.
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),  # Refresh 토큰
                    'access': str(refresh.access_token),  # Access 토큰
                }, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)