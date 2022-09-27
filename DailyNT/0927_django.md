# Django 

### app이 두개 이상이면 url을 어떻게 관리해야할까?

+ 하나일때 이때까지 urls.py에 from app이름 import views로 했음
+ But, 2개 이상인 경우 둘 다 views가 된다.  
+ 이 경우 아래 두가지 방법으로 관리 
  1. import articles.views
  2. from articles import views as articles_views (별칭 붙이기)



### index 순서 

+ App마다 Index.html이 있을 때 뭐부터? 어떤 index를 열어주나?

  : settings.py의 INSTALLED_APPS 리스트 맨 위 app의 인덱스를 열어준다.

+ 그럼 앱마다 index를 쓰려면 어떻게 해야할까

  : 앱마다 templates폴더 안에 그 앱 이름으로 폴더 하나를 더 만들고 거기 인덱스를 넣어준다. 

  : localhost:8000 원하는거에 부모템플맇ㅅ... 

  + 따라서 views에 루트도 바꿔주기. "앱이름/Html파일이름"

+ 원리? 

  : 앱마다 templates 폴더가 따로 있지만 사실은 하나의 폴더로 보면 됨 



## Django URLs

+ 지금은 몇 개 없지만 나중엔 수십개의 url이 생긴다. 
  + 따라서 지금처럼 urls.py > urlpatterns = [] 로만 관리하기가 어려움 
  + 나중에 회사가면 url만 관리하는 팀, templates만 관리하는 팀, 코드 분석만하는 팀 이런식으로 다 분리되어 있음. 
+ "Dispatcher(운행 관리원)로서의 url 이해하기"
  + 관제사와 비슷함. 내가 직접 비행기 운행하는 것이 아니라 요청을 핸들링하는 역할






### App URL mapping

+ 앱이 많아졌을 때 urls.py를 각 app에 Mapping하는 방법
  1. 앱 별로 urls.py를 만든다
  2. Urls.py 내 경로 지정 후 프젝폴더 urls.py처럼 경로 작성해주기
  3. 메인 문지기인 프로젝트 urls한테 경로 알려준다.





## Template inheritance

+ Settings.py > TEMPLATES = [{'DIRS' : [여기]}]
+ 앱이 아닌 프로젝트 폴더 안에 templates를 만들고 절대경로로 지정해준다 

+ 나는 누구.,,, 여긴 어디,, ,, 
+ 장고가 기본적으로 추구하는 컨벤션... 
+ 회사마다 추구하는 컨벤션..... 
+ base파일이 있으면 이건 특정 앱에 넣는게 아니라 아예 최상단에 넣어서 베이스템플릿을 분리해서 지정해주고, 이미 설정되어있는 경로 안에 집어 넣는다 ? 
+ App_name/templates/ 디렉토리 경로 이외에 ... 
+ 폴더 위치가 젤 중요하다 
  + 최상단에 ㄴ생성하기 

#### step

1.  폴더 다 접어서 최상위 폴더 안에 templates 폴더 생성 

2. 프로젝트 폴더의 셋팅 파일에 추가설정하기 

   + `BASE_DIR = Path(__file__).resolve().parent.parent`

   + ```python
     EMPLATES = [
         {
             "BACKEND": "django.template.backends.django.DjangoTemplates",
             "DIRS": [BASE_DIR/'templates'],
     ```

   + templates말고 어,, 전 폴더이름 base하고싶은데요? 하면 /'base'해도 작동됨

   + 이게 일반적인 경로설정 방법은 아니다. 살짝 속성.. 

   + 파이썬 os pathlib를 사용해서 좀 더 유연하고 광범위하게 설정하는게 정석



### DB 만들어서 서버 꺼도 데이터 유지시키기

1. 앱 폴더 내 models.py 에 아래 코드 추가하기 

```python
class Article(models.Model):
  content = models.TextField()
```

2. 터미널에서 명령어 실행 
   1. python manage.py makemigrations
   2. python manage.py migrate
3. 가상폴더 db.sqlite3 확인하면 생성돼있음. 
4. 이제 views에서 sql 쿼리 활용하여 코드 짜기 