# Django 11

## Authentication System

### 개요

+ 장고 기본 구성 안에 있는 인증 시스템 

+ 인증, 권한 부여를 함께 제공/처리한다.

  + User
  + 권한 및 그룹
  + 암호 해시 시스템
  + form & View 도구 
  + 기타 적용가능한 시스템 

| **Authentication(인증)**               | **Authorization(권한, 허가)**              |
| :------------------------------------- | ------------------------------------------ |
| + 신원 확인                            | 권한 부여                                  |
| + 사용자가 자신이 누구인지 확인하는 것 | 인증된 사용자가 수행할 수 있는 작업을 결정 |

+ 필수 구성은 setting.py > `installed_apps = []`에서 확인 가능 



### User Objects (객체)

+ 일반적으로 사이트와 상호작용하는 사람들을 나타냄 
+ 액세스 제한, 사용자 프로필 등록, 작성자와 콘텐츠 연결 등과 같은 작업을 활성화하는데 사용됨
+ The primary attributes of the default user : 
  + username
  + password
  + email
  + first_name
  + last_name



#### User 생성

+ The most direct way =  [`create_user()`](https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#django.contrib.auth.models.UserManager.create_user)

```python
from django.contrib.auth.models import User
user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
# At this point, user is a User object that has already been saved
# to the database. You can continue to change its attributes
# if you want to change other fields.
user.last_name = 'Lennon'
user.save()
```



#### superusers 생성

```bash
$ python manage.py createsuperuser
$ python manage.py createsuperuser --username=sol --email=sol@example.com
```

+ 전자는 이름, 이멜, 비번 물어보는 메세지 뜸



#### 비밀번호 변경

+ Django는 Users DB model에 원시 암호 저장x, only  해시코드만 저장

+ options to change a user's pw

  1. [`manage.py changepassword *username*`](https://docs.djangoproject.com/en/4.1/ref/django-admin/#django-admin-changepassword)

  2. [`set_password()`](https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#django.contrib.auth.models.User.set_password)

     ```python
     from django.contrib.auth.models import User
     user = User.objects.get(username='sol')
     user.set_password('new password')
     user.save()
     ```

  3.  Django admin 설치 후 [authentication system’s admin pages](https://docs.djangoproject.com/en/4.1/topics/auth/default/#auth-admin)에서도 변경 할 수 있다.
  4. views.py, forms.py 조작해서 사용자가 직접 변경할 수 있도록 꾸밀 수 있음 

+ 사용자 암호 변경 시 모든 세션 로그아웃됨 



#### 사용자 인증 

#### `authenticate(request=None, credentials)`

+ Use this to verify a set of credentials. 아이디 비번 맞는지 증명 

+ backend에서 저 set이 맞는게 증명되면 user object 반환. 아니면 none

  ```python
  from django.contrib.auth import authenticate
  user = authenticate(username='sol', password='1234')
  if user is not None:
      # A backend authenticated the credentials
  else:
      # No backend authenticated the credentials
  ```

  > You probably won’t use this. Rather if you’re looking for a way to login a user, use the [`LoginView`](https://docs.djangoproject.com/en/4.1/topics/auth/default/#django.contrib.auth.views.LoginView).



#### Permissions and Authorization

+ 장고엔 특정 사용자나 사용자 그룹에 권한을 할당하는 시스템이 내장되어 있음 
+ Django admin site에서 관리하거나 직접 코드 짜도 됨 



### 과정

#### 1. accounts app 생성 및  settings.py에 등록 

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



#### 2. url 분리 및 mapping

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



#### 3. user model 생성 

🌟 Django 내장 User 모델이 이미 있다 ! 

​	👉 따라서 기존 User 모델을 상속 받아서 사용하면 됨 



##### Django Default User Model을 Custom하여 사용하기 

AUTH_USER_MODEL = 'auth.User'

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



