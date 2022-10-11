# Django 10

## 복습 & 실습

🔥 아래의 문서는 꼭 읽어보세요.

- Django Auth 기본
  - https://docs.djangoproject.com/en/4.1/topics/auth/default/
- Django User Model
  - https://docs.djangoproject.com/en/4.1/ref/contrib/auth/
- Custominzing
  - https://docs.djangoproject.com/en/4.1/topics/auth/customizing/
- 비밀번호 암호화
  - https://docs.djangoproject.com/en/3.2/topics/auth/passwords/
  - https://d2.naver.com/helloworld/318732
  
  

>  [GitHub - kdt-live/01-django-modelform](https://github.com/kdt-live/01-django-modelform)



## 목표

Django **Auth**를 활용한 회원가입이 가능한 서비스를 개발



## 요구사항

### 모델 Model

- 모델 이름 : User

  Django **AbstractUser** 모델 상속

### **폼 Form**

- Django 내장 회원가입 폼 UserCreationForm을 상속받은 CustomUserCreationForm 생성 후 활용

  해당 폼은 아래 필드만 출력합니다.

  - username
  - email
  - password1
  - password2
  
  

### 기능 View

#### 회원가입 Create

- `POST` http://127.0.0.1:8000/accounts/signup/
- CustomUserCreationForm을 활용해서 회원가입 구현

#### 회원 목록 조회 Read(index)

- `GET` http://127.0.0.1:8000/accounts/

#### 회원 정보 조회 Read(detail)

- `GET` http://127.0.0.1:8000/accounts/<user_pk>/



### 화면 Template

#### 메인페이지

- `GET` http://127.0.0.1:8000/

- 회원가입 페이지 이동 버튼

- 회원 목록 페이지 이동 버튼

  ![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/fb2edac6-5056-4b5d-a067-200417f8149d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221011%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221011T045104Z&X-Amz-Expires=86400&X-Amz-Signature=0e63c42465abef04bc1aea41dfb55b6a7a9f8d205006e3f10659871dc20a94ed&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

#### 회원가입 페이지

- `GET` http://127.0.0.1:8000/accounts/signup/

- 회원가입 폼 ****

  ![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/e0faec52-56a9-4a13-8b3f-68d40622a98f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221011%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221011T045119Z&X-Amz-Expires=86400&X-Amz-Signature=f662d98204f01d493ca16ac479ad87cdf140628cc2157e2654510dfacef0e8a8&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

#### 회원 목록 페이지

- `GET` http://127.0.0.1:8000/accounts/

- 회원 목록 테이블

- **username** 클릭 시 해당 회원 조회 페이지(프로필 페이지)로 이동

  ![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/9b3e71b7-966b-4982-a51c-d537d9a927d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221011%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221011T045135Z&X-Amz-Expires=86400&X-Amz-Signature=35c7d8b8f03d68df37da86e091546f502d7d1e8e6d7e82e0330b8e5d424e0af0&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

#### 회원 조회 페이지(프로필 페이지)

- `GET` http://127.0.0.1:8000/accounts/<user_pk>/
- 회원 정보 출력



## 과정

### accounts app 생성 및  settings.py에 등록 

```bash
$ python manage.py startapp accounts
```

```python
# settings.py
INSTALLED_APPS = [
'articles'
'accounts'
...]
```

👏 auth와 관련한 경로나 키워드들을 Django 내부적으로 accounts 라는 이름으로 사용하고 있기 때문에 되도록 accounts 로 지정하는 것을 권장

👏 다른 이름으로 설정해도 되지만 나중에 추가 설정을 해야 할 일들이 생기게 된다.



### url 분리 및 mapping

```python
# project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
]
```

```python
# accounts/urls.py
from django.urls import path
from . import views
app_name = "accounts"
urlpatterns = [
    path("", views.index, name="index"),
    path("signin/", views.signin, name="signin"),
]
```



### Django Default User Model을 Custom하여 사용하기 

#### AUTH_USER_MODEL = 'auth.User'

+ 프로젝트에서 User를 나타낼 때 사용하는 모델 

+ 프로젝트가 진행되는 동안 변경할 수 없다 

  ```python
  # project/settings.py 파일 내에 아래 코드를 전부 작성해준다.
  AUTH_USER_MODEL = 'auth.User'
  ```



#### 1. AbstractUser를 상속받는 커스텀 User class 작성

+ 기존 User class도 AbstractUser를 상속 받기 때문에 Custom User class도 동일한 모습을 가진다. 

  ```python
  # accounts/models.py
  # accounts/models.py
  from django contrib auth models import AbstractUser
  
  class User(AbstractUser):
      pass
  ```

#### 2. User를 나타내는데 사용하는 모델을 '1'에서 생성한 Custom User Model로 지정

```python
# project/settings.py 
AUTH_USER_MODEL = accounts.User'
```

#### 3. admin.py에 Custom User Model을 등록 

+ default User Model이 아니기 때문에 등록하지 않으면 admin site에 출력되지 않으니 주의

  ```python
  # accounts/admin.py
  
  ```

  

### makemigrations > migrate

+ 프로젝트 중간일 경우 데이터베이스 초기화 후 하기 (실습시에만)
  + migrations 폴더 안 번호 붙은 파일 삭제
  + db.sqlite3 삭제



### Custom User로 변경된 테이블 확인

+ 기존 auth_user table이 아닌 accounts_user table을 사용하게 됨 

  ![auth](README.assets/화면 캡처 2022-10-11 170514.png) ![2](README.assets/화면 캡처 2022-10-11 170558.png)



### User Model 활용하기 

+ User 객체는 인증 시스템의 가장 기본

+ 기본 속성 :
  + username varchar(150)
  + password varchar(128)
  + email varchar(254)
  + first_name varchar(150)
  + last_name varchar(150)

#### 암호 관리 

+ 회원은 가입 시 암호 설정이 필수이고 암호는 별도의 처리가 필요함

+ Django에서는 Default로 단방향 해시 함수 SHA256 PBKDF2(Password-Based Key Derivation Function)를 사용하여 저장

+ 또 레인보우/무차별 대입 공격 등을 막기 위해 알아서 Salting과 key Stretching 기법을 추가적으로 활용한다. 

  + salting : 패스워드에 임의의 문자열을 소금 쳐서 다이제스트를 생성

  + key stretching : 해시를 여러 번 반복해서 계산 시간을 늘림

    (`<algorithm>$<iterations>$<salt>$<hash>`)



> ### User 객체 활용
>
> #### User 생성
>
> ```python
> user = User.objects.create_user("sol", "soldakm@gmail.com", '1q2w3e4r')
> ```
>
> #### User 비밀번호 변경
>
> ```python
> user = User.objects.get(pk=2)
> user.set_password('new pw')
> user.save()
> ```
>
> #### User 인증 ( 비번 확인 )
>
> ```python
> from django contrib auth import authenticate
> user = authenticate(username='john', password='secret')
> ```



### 회원가입 UserCreationForm

+ 주어진 username과 password로 권한이 없는 새 user를 생성하는 ModelForm

+ 3개의 default fields

  + username (from the 'User' model)
  + password 1
  + password 2 (비번 확인란)

  ```python 
  # accounts/forms.py 생성
  # from .models import User default user table이 아닌 custom user table을 사용하기때문에 이거 안 씀
  from django.contrib.auth.forms import UserCreationForm
  from django.contrib.auth import get_user_model
  
  class CustomUserCreationForm(UserCreationForm):
      class Meta:
          model = get_user_model()
          fields = (
              "username",
              "password",
          )
  ```

  ✨**get_user_model** 

  + 현재 프로젝트에서 활성화된 사용자 모델(active user model)을 반환
  + django에서 user class는 custom을 통해 변경 가능하고, 직접 참조하는 대신 get_user_model()을 사용하는 것을 권장

#### project/views.py 함수 정의 

```python
# from accounts.models import User forms.py랑 동일한 이유로 안 씀
from django.contrib.auth.forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("account:index")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)
```

