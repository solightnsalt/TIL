# Django 

## Authentication System

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



### User 생성

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



### superusers 생성

```bash
$ python manage.py createsuperuser
$ python manage.py createsuperuser --username=sol --email=sol@example.com
```

+ 전자는 이름, 이멜, 비번 물어보는 메세지 뜸



### 비밀번호 변경

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



### 사용자 인증 

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



### Permissions and Authorization

+ 장고엔 특정 사용자나 사용자 그룹에 권한을 할당하는 시스템이 내장되어 있음 
+ Django admin site에서 관리하거나 직접 코드 짜도 됨 



