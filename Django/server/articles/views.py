from multiprocessing import context
from django.shortcuts import render
import random 
# Create your views here.
def index(request): # ()이 인자는 보통 요청자(=사용자)의 정보 보통 request로 핸들한다. 
    # 환영하는 메인 페이지 
    names = ['안유진', '장원영', '이서', '레이', '가을']
    name = random.choice(names)
    context = {
        'name' : name,
        'img' : 'https://www.kmccoc.org/v1/wp-content/uploads/2018/07/WELCOME-ST-IVES.jpg',
    }
    return render(request, 'index.html', context) # () 첫번째 인자로 요청자?. 이 두줄의 포맷은 안 변한다. 

def welcome(request, name):
    # 주소에 /welcome/이름 입력하면, 그 이름과 환영인사 출력
    # print(name)
    images = ['https://www.kmccoc.org/v1/wp-content/uploads/2018/07/WELCOME-ST-IVES.jpg',
            'https://i.pinimg.com/originals/35/45/f4/3545f49ee7278db6a6d44e62e4e9bfeb.jpg',
            'https://img.freepik.com/free-vector/floral-welcome-lettering-concept_23-2147902326.jpg?w=2000',
            ]
    image = random.choice(images)        
    context = {
        'name' : name,
        'greetings' : [
            'Bonjour',
            'Hola',
            'Guten Tag',
            'Ciao',
            'Oi',
            'Namaste',
            ],
        'images' : image,
    }
    return render(request, 'welcome.html', context)