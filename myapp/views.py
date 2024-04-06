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

das = 3

history = []
def time(request):
    return 3
System_message = '''
우리가 문제를 만들어달라고 할 때, '문제' 키워드를 그대로 적어주고 문제가 몇 번째인지는 적지마 '문제1'에서 1 같은 키워드는 없어야해 그리고 그 옆에 반드시 스페이스 두 칸을 띄우고 문제 내용을 적어줘. 이 부분은 한 줄로 처리가 돼야해 그리고 split("  ")으로 구분이 될 수 있게 반드시 문제와 문제 내용 사이에는 두 칸을 띄워줘.
우리가 문제를 만들어달라고 할 때, 문제와 관련된 부분을 제외한 추가적인 대답을 원하지 않아. (ex 네 알겠습니다)
객관식 문제를 만들어달라고 할 때는, 4지선다로만 내주고 선택지마다 1.) 같은 키워드로 순서를 구분해줘 반드시 숫자마다 .) 가 있어야해.
문제를 여러개 만들어 달라고 할 때는 문제와 문제사이는 반드시 '----------------' 출력해줘 이거를 제외하고는 아무것도 없어야해 공백이든 엔터든.
'''
mutiple_question = '''if we want you make problem, you always make five-choice question.'''
write_question = '''if we want you make problem, you always make one Short answer question'''
def get_completion(prompt):     
    history.append({'role':'user','content':prompt}) 
    query = openai.ChatCompletion.create( 
       model="gpt-4",
       messages=[{"role": "system", "content": System_message}, {'role':'user','content':"자바 객관식 문제 만들어줘"}], 
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
    
@api_view(['POST'])
def GenerateProblem(request):
    a, tmp = query_view(request)
    lst = list(tmp.split("\n"))
    rtr = []
    check = False
    idx = 1
    tempt = dict()
    for i in lst:
        if check:
            tempt['question'] = i
            continue
        if i[0:2] == '문제':
            if len(i) == 2:
                check = True
            else:
                b = i[5::]
                tempt['question'] = b
                tempt['options'] = []
        elif len(i) >= 0 and i[0]!= '-' and 1 <= int(i[0]) <= 4:
            b = i[4:]
            tempt['options'].append(b)
            if int(i[0]) == 4:
                tempt['answer'] = 'A'
                rtr.append(tempt)
        else:
            tempt = dict()
            continue
            
            
            
    print(rtr)
    return Response(rtr, status=status.HTTP_200_OK)