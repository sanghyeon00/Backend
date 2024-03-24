from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
#import openai
#import os


user_data = dict()


from django.shortcuts import render 
from django.http import JsonResponse 
import openai
import os

openai.api_key='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' 

history = []

def get_completion(prompt): 
   print(prompt)
   history.append({'role':'user','content':prompt}) 
   query = openai.ChatCompletion.create( 
      model="gpt-4",
      messages=history, 
      max_tokens=1024, 
      n=1, 
      stop=None, 
      temperature=0.5, 
   ) 
   response = query.choices[0].message["content"]
   history.append({'role':'assistant', 'content':response})
   print(response) 
   return response 
def index(request):
    return HttpResponse("Communication start")
    
def query_view(request): 
    prompt = request.data.get('username') 
    prompt=str(prompt)
    response = get_completion(prompt)
    return JsonResponse({'response': response}) 

@api_view(['POST'])
def login_view(request):
    global user_data
    username = request.data.get('username')
    password = request.data.get('password')
    check = True
    print(username)
    a = query_view(request)
    print(a)
    if username not in user_data:
        user_data[username] = password
        check = True
    else:
        check = False
        
    if check:
        # 로그인 성공 처리
        return Response({'message': 'Success'}, status=status.HTTP_200_OK)
    else:
        # 로그인 실패 처리
        return Response({'message': 'Fail'}, status=status.HTTP_401_UNAUTHORIZED)