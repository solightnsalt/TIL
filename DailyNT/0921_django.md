# Django

+ python으로 작성된 framework

+ == 서버를 구현하면 웹 프레임워크

> WEB 
>
> : 우리가 인터넷을 이용한다는 것 = 전 세계가 연결된 하나의 인프라를 이용하는 것 



## Client & Server 

+ 어떤 서비스를 만든다 ?
  + 어떻게 요청을 받고 > 누구에게 무엇을 어떻게 응답을 할지 가 가장 중요  
  + 요청하는 쪽 = client, 응답하는 쪽 = server 

+ 오늘날 우리가 사용하는 대부분의 웹서비스도 동일
  + 클라이언트-서버 구조 기반 

<img src="https://cdn-images-1.medium.com/max/1080/1*qzK0Z9vfDT4fVQu3G9OGPg.png" alt="diagram" style="zoom:50%;" />

### Client

+ 웹 사용자의 인터넷에 연결된 장치 (ex. wifi에 연결된 mobile, laptop 등)
+ 웹 브라우저 like Chrome, Firefox, etc.

+ 서비스를 요청하는 주체 



### Server 

+ 웹사이트의 원래 주소 = 숫자로 이루어져 있음 
  + 근데 클라이언트 입장에서는 헷갈리니까 도메인이라는 키워드로 대표

+ U



### web browser & web page

+ 정적 웹 페이지 
  + 이때까지 만들어 온 것 
  + static
  + Ex 대표적으로 회사 소개 페이지 같은 것들이 보통 스태틱 
+ 동적 웹 페이지 
  + 다이나믹 웹페이지 
  + 사용자의 요청에 따라 웹 페이지에 추가적인 수정이 되어 클라이언트에게 전달되는 페이지 
  + 웹 페이지의 내용을 바꿔주는 주체 == 서버
    + 서버에서 동작하고 있는 프로그램이 변경해줌 
    + 그 프로그램 중에 하나가 뭐다? 장고다 
  + 다양한 서버 사이드 프로그래밍 언어 사용 가능 
  + 파일을 처리하고 데이터베이스와의 상호작용이 이루어진다.



## Django 구조 이해하기(MTV Design )

> 가상환경 만드는 방법

> ```bash
> sol/desktop  > cd server
> desktop/server  > python -m venv server-venv ⭐️venv라는 파이썬 모듈을 쓸건데 이름을 server-venv라고 하자 
> desktop/server  > ls ⭐️만든거 확인
> server-venv
> desktop/server  > source server-venv/Scripts/activate ⭐️절대경로로 activate 실행시키기 
> source: no such file or directory: server-venv/Scripts/activate **이거는 window
> desktop/server  > source server-venv/bin/activate **이게 mac ⭐️그 폴더 안으로 가서 ./activate 해도됨
> (server-venv) desktop/server  > deactivate ⭐️다시 끄는 방법! 이거는 그냥 저 키워드만 쳐도 Ok
> (server-venv) desktop/server  > pip install django==3.2.13 ⭐️가상환경에서 설치한거라 글로벌엔 안 깔림
> (server-venv) desktop/server  > pip list ⭐️버전 명시할때는 ==임. 설치 됐는지 확인 
> Package    Version
> ---------- --------
> asgiref    3.5.2
> Django     3.2.13  ⭐️장고 깔린거 확인 
> pip        22.0.4
> pytz       2022.2.1
> setuptools 58.1.0
> (server-venv) desktop/server  > django-admin startproject firstpjt . ⭐️장고 새프로젝트를 firstpjt라는 이름으로 현재폴더에 만들자 ! [프로젝트명] [경로]
> (server-venv) desktop/server  > ls
> firstpjt	manage.py	server-venv
> (server-venv) desktop/server  > python manage.py runserver ⭐️서버를 돌려보자 ! 
> Watching for file changes with StatReloader
> Performing system checks...
> 
> System check identified no issues (0 silenced).
> ```

>http://localhost:8000/ 들어가보면 로컬 서버 확인 할 수 있음 🥳

+ 그럼 가상환경을 지우려면 저 폴더만 지우면 되나 ? 
  + 구글링으로 명령어 찾아보면 깔끔하게 지우는거 있다 ! 
  + rm 뭐 이런거 

+ 