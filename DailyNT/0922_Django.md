# Django

## 기본 환경 설정

+ `python manage.py startapp [앱이름]`

  + 새로운 앱의 껍데기를 만든 느낌 

+ 보통 앱 (어떤 기능을 가진) 이름은 복수형으로 쓴다. 

+ 지금까지 배운걸로는 가상환경에 장고가 깔려 있어서 가상환경 실행 안시키면 

  `source server_venv/bin/activate`를 했을 때 안되는게 맞음. 

  + 그런데 ! global에도 깔려있으면 가상환경 실행 안시켜도 저 명령어 실행됨

+ articles로 앱을 만들었을때 

  + 새로운 폴더 articles가 생기고 안에 다양한 py파일들이 생긴다. 
  + 그 중에 ⭐️**view**.py⭐️가 젤 중요함 ~! 



+ 새롭게 앱을 생성만 한 것 

+ 실제로 사용. 활용하려면 ? 

  + 장고한테 장고야 우리 이거 쓸건데 등록해줘 하고 시켜야됨  

  + how?

    + settings.py 안에 보면 INSTALLED_APPS 라는 리스트가 있음 

    + 그럼 이제 이렇게 생각하기. 설치된 앱 리스트에 뭔가 있네 ? 그럼 내 앱도 넣으면 ? 

    + note 1. 리스트 규칙에 맞게 안에 내가 만든 이름은 위에 !!!! 추가 해주기 

    + note 2. 마지막 요소 뒤에도 쉼표 써주기

    + Ex. INSTALLED_APPS = [

      'articles'

      'django.contrib.admin',

      ]

+ 그럼 만든 앱을 지우려면 ? 

  + 명령어는 없고, 리스트에서 지우고 파일 지우고 순서대로 

> Imperative 
>
> + 단계적으로 명령 다 해줘야됨
>
> declarative
>
> + 어,, 짜장면이 먹고 싶네? 장고한테 시키면 알아서 짜장면 만들어줌 ㅎ 
> + 선언 ! 



## project & application 

+ 하나의 프로젝트는 여러 앱을 가질 수 있다 



## 요청과 응답 

+ 요청은 url 
+ 응답은 문서(html)
  + url로 요청을 보내면 문서를 응답으로 받는다 
+ Ex. Client (우리 & 크롬) <--------------> server (네이버)



+ **url > view > template** 순으로 코드 작성하고, 데이터 흐름을 이해하기 

  1. 주문서 정의 -> urls.py
  2. 로직 구현 -> views.py
  3. Html 페이지 구성 -> template인데 내가 정의한 이름. ex. Index.py

  

  

+ render() 
  + 주어진 템플릿을 
+ templates
  + 실제 내용을 보여주는데 사용되는 파일 
  + 파일의 구조나 레이아웃을 정의 

+ articles에 새폴더 생성: templates
+ 

