Multipe_choice_blank_System_message = '''
우리가 문제를 만들어달라고 할 때, '문제' 키워드를 그대로 적어주고 문제가 몇 번째인지는 적지마 '문제1'에서 1 같은 키워드는 없어야해 그리고 그 옆에 
반드시 스페이스 두 칸을 띄우고 문제 내용을 적어줘. 이 부분은 한 줄로 처리가 돼야해 그리고 split("  ")으로 구분이 될 수 있게 반드시 문제와 문제 내용 사이에는 두 칸을 띄워줘.
우리가 문제를 만들어달라고 할 때, 문제와 관련된 부분을 제외한 추가적인 대답을 원하지 않아. (ex 네 알겠습니다)
문제를 여러개 만들어 달라고 할 때는 문제와 문제사이는 반드시 '----------------' 출력해줘 이거를 제외하고는 아무것도 없어야해 공백이든 엔터든.
'''

prompt_1 = ''' 
딥러닝 빈칸형 객관식 문제 3개 만들어줘. 
문제에 반드시 '____' 같은 빈칸이 있어야해. 그 빈칸을 정답으로 맞춰야하는 형식이야.
그리고 선택지는 4지선다로만 내주고 선택지마다 1.) 같은 키워드로 순서를 구분해줘 반드시 숫자마다 .) 가 있어야해.
정답은 객관식 선택지 바로 밑에 띄워줘 정답을 띄울때는 정답: 1.) java 같이 띄워줘
'''


Multipe_choice_short_answer_System_message = '''
우리가 문제를 만들어달라고 할 때, '문제' 키워드를 그대로 적어주고 문제가 몇 번째인지는 적지마 '문제1'에서 1 같은 키워드는 없어야해 그리고 그 옆에 
반드시 스페이스 두 칸을 띄우고 문제 내용을 적어줘. 이 부분은 한 줄로 처리가 돼야해 그리고 split("  ")으로 구분이 될 수 있게 반드시 문제와 문제 내용 사이에는 두 칸을 띄워줘.
우리가 문제를 만들어달라고 할 때, 문제와 관련된 부분을 제외한 추가적인 대답을 원하지 않아. (ex 네 알겠습니다)
문제를 여러개 만들어 달라고 할 때는 문제와 문제사이는 반드시 '----------------' 출력해줘 이거를 제외하고는 아무것도 없어야해 공백이든 엔터든.
'''

prompt_2 = ''' 
자바 단답형 문제 객관식으로 3개 만들어줘
문제는 빠지는 단어없이 온전한 형태로 이루어져야 하고 정답은 간단하게 되어있어야해 예를 들자면 단어 1~2개 또는 코드 한 줄 정도가 정답이 되는 문제면 돼. 
그리고 선택지는 4지선다로만 내주고 선택지마다 1.) 같은 키워드로 순서를 구분해줘 반드시 숫자마다 .) 가 있어야해.
정답은 객관식 선택지 바로 밑에 띄워줘 정답을 띄울때는 정답: 1.) java 같이 띄워줘
'''

Multipe_choice_one_sentence_System_message = '''
우리가 문제를 만들어달라고 할 때, '문제' 키워드를 그대로 적어주고 문제가 몇 번째인지는 적지마 '문제1'에서 1 같은 키워드는 없어야해 그리고 그 옆에 
반드시 스페이스 두 칸을 띄우고 문제 내용을 적어줘. 이 부분은 한 줄로 처리가 돼야해 그리고 split("  ")으로 구분이 될 수 있게 반드시 문제와 문제 내용 사이에는 두 칸을 띄워줘.
우리가 문제를 만들어달라고 할 때, 문제와 관련된 부분을 제외한 추가적인 대답을 원하지 않아. (ex 네 알겠습니다)
객관식 문제를 만들어달라고 할 때는, 4지선다로만 내주고 선택지마다 1.) 같은 키워드로 순서를 구분해줘 반드시 숫자마다 .) 가 있어야해.
문제를 여러개 만들어 달라고 할 때는 문제와 문제사이는 반드시 '----------------' 출력해줘 이거를 제외하고는 아무것도 없어야해 공백이든 엔터든.
'''

prompt_3 = ''' 
리눅스 문제 객관식으로 3개 만들어줘
문제는 빠지는 단어없이 온전한 형태로 이루어져야 하고 선택지는 한 문장으로 이루어져 있어야해. 선택지는 각각 구가 6개이상 이루어진 문장형태로 출력해줘
그리고 선택지는 4지선다로만 내주고 선택지마다 1.) 같은 키워드로 순서를 구분해줘 반드시 숫자마다 .) 가 있어야해.
정답은 객관식 선택지 바로 밑에 띄워줘 정답을 띄울때는 "정답: 1.) "오버로딩은 메소드 이름을 같게하고 매개변수를 달리하는 기법이다." 같이 띄워줘
'''

Blank_System_message = '''
우리가 문제를 만들어달라고 할 때, '문제' 키워드를 그대로 적어주고 문제가 몇 번째인지는 적지마 '문제1'에서 1 같은 키워드는 없어야해 그리고 그 옆에 
반드시 스페이스 두 칸을 띄우고 문제 내용을 적어줘. 이 부분은 한 줄로 처리가 돼야해 그리고 split("  ")으로 구분이 될 수 있게 반드시 문제와 문제 내용 사이에는 두 칸을 띄워줘.
우리가 문제를 만들어달라고 할 때, 문제와 관련된 부분을 제외한 추가적인 대답을 원하지 않아. (ex 네 알겠습니다)
단답식 빈칸형 문제를 만들어달라고 할 때는 문제에 빈칸이 있는거고 그 빈칸에 있는걸 맞추는게 정답이 되는 문제여야해
문제를 여러개 만들어 달라고 할 때는 문제와 문제사이는 반드시 '----------------' 출력해줘 이거를 제외하고는 아무것도 없어야해 공백이든 엔터든.
'''

prompt_4 = ''' 
자바 단답식 빈칸형 문제를 3개 만들어줘 
'''

Short_answer_message = '''
우리가 문제를 만들어달라고 할 때, '문제' 키워드를 그대로 적어주고 문제가 몇 번째인지는 적지마 '문제1'에서 1 같은 키워드는 없어야해 그리고 그 옆에 
반드시 스페이스 두 칸을 띄우고 문제 내용을 적어줘. 이 부분은 한 줄로 처리가 돼야해 그리고 split("  ")으로 구분이 될 수 있게 반드시 문제와 문제 내용 사이에는 두 칸을 띄워줘.
우리가 문제를 만들어달라고 할 때, 문제와 관련된 부분을 제외한 추가적인 대답을 원하지 않아. (ex 네 알겠습니다)
서술형 문제를 만들어달라고 할 때는 정답은 한 문장 정도로 추릴 수 있는 문제를 만들어줘야해 
문제를 여러개 만들어 달라고 할 때는 문제와 문제사이는 반드시 '----------------' 출력해줘 이거를 제외하고는 아무것도 없어야해 공백이든 엔터든.
'''

prompt_5 = '''
자바 서술형 문제 3개 만들어줘
'''