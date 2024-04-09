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
from myapp import gpt_prompt
import openai
import os

openai.api_key = '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'
history = []

Quest_dict = {'객관식-빈칸': 1, '객관식-단답형': 2, '객관식-문장형': 3, '단답형-빈칸': 4, '단답형-문장형': 5, 'OX선택형-O/X': 6, '서술형-코딩': 7}
def get_completion(prompt, numberKey,count):     
    history.append({'role':'user','content':gpt_prompt.prompt_1}) 
    query = openai.ChatCompletion.create( 
       model="gpt-4",
       messages=[{"role": "system", "content": gpt_prompt.System_lst[numberKey]}, {'role':'user','content':gpt_prompt.prompt_lst[numberKey](count)}], 
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
    
def query_view(request,numberKey, count): 
    prompt = request.data.get('username') 
    prompt=str(prompt)
    response = get_completion(prompt, numberKey,count)
    return JsonResponse({'response': response}), response 

@api_view(['POST'])
def login_view(request):
    global user_data
    username = request.data.get('username')
    password = request.data.get('password')
    check = True
    print(username)
    a, tmp= query_view(request)
    print()
    print(a)
    if username not in user_data:
        user_data[username] = password
        check = True
    else:
        check = False
        
    if check:
        # �α��� ���� ó��
        return Response({'message': 'Success'}, status=status.HTTP_200_OK)
    else:
        # �α��� ���� ó��
        return Response({'message': 'Fail'}, status=status.HTTP_401_UNAUTHORIZED)

def GenerateWriteProblem(tmp):
    lst = list(tmp.split("\n"))
    rtr = []
    check = False
    tempt = dict()
    for i in lst:
        if check:
            id = 0
            while i[id] == ' ' or i[id] == '.' or i[id] == '1' or i[id] == '2' or i[id] == '3' or i[id] == '4':
                id += 1 
            tempt['content'] = i[id::]
            check = False
            continue
        if i[0:2] == '문제':
            if len(i) == 2:
                check = True
                continue
            else:
                id = 2
                while id <len(i) and i[id] == ' ':
                    id += 1
                if len(i) == id:
                    check = True
                    continue
                b = i[id::]
                tempt['content'] = b
        elif i[0:2] == '정답':
            tempt['answer'] = i[4::]
            rtr.append(tempt)
            tempt = dict()
    print(rtr)
    return rtr
                

def GenerateMultipleProblem(tmp):
    lst = list(tmp.split("\n"))
    rtr = []
    check = False
    idx = 1
    tempt = dict()
    for i in lst:
        if check:
            id = 0
            while i[id] == ' ' or i[id] == '.' or i[id] == '1' or i[id] == '2' or i[id] == '3' or i[id] == '4':
                id += 1 
            tempt['content'] = i[id::]
            check = False
            continue
        if i[0:2] == '문제':
            if len(i) == 2:
                check = True
            else:
                id = 2
                while id <len(i) and i[id] == ' ':
                    id += 1
                if len(i) == id:
                    check = True
                    continue
                b = i[id::]
                tempt['content'] = b
                tempt['options'] = []
        elif len(i) > 0 and i[0]!= '-' and i[0] != ' ' and i[0:2] != '정답' and 1 <= int(i[0]) <= 4:
            b = i[4:]
            tempt['options'].append(b)
        elif i[0:2] == '정답':
            tempt['answer'] = i
            for j in i:
                if i == '1' or i == '2' or i == '3' or i == '4' :tempt['answer_number'] = int(i)
            rtr.append(tempt)
            tempt = dict()
            continue
    print(rtr)
    return rtr

@api_view(['POST'])
def GenerateQuestion(request):
    print(request.data.get('selections'))
    answer = {}
    answer['questions'] = []
    for tempt in request.data.get('selections'):
        if 1 <= Quest_dict[tempt] <= 3:
            tmp = dict()
            tmp['type'] = Quest_dict[tempt]
            a, t = query_view(request,Quest_dict[tempt], request.data.get('selections')[tempt])
            tmp['items'] = GenerateMultipleProblem(t)
            tmp['count'] = request.data.get('selections')[tempt]
            answer['questions'].append(tmp)
        elif 4 <= Quest_dict[tempt] <= 6:
            tmp = dict()
            tmp['type'] = Quest_dict[tempt]
            a, t = query_view(request,Quest_dict[tempt], request.data.get('selections')[tempt])
            tmp['items'] = GenerateWriteProblem(t)
            tmp['count'] = request.data.get('selections')[tempt]
            answer['questions'].append(tmp)
            
            
            
    return Response(answer, status=status.HTTP_200_OK)
    