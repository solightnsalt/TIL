# Django Auth

+ 왜
+ 상속? 부모 클래스에 정의된 속성/메서드(기능)을 가져와서 쓰는데 쓸거는 쓰고 필요없는거는 안써도.. 
+ ArticleForm? UserCreationForm? 
  + ArticleForm
    + Meta : 필드, 모델 
  + UserCreationForm
    + Meta : 필드, 모델
+ ModelForm 생각해보기 
  + 위에 둘 다 ModelForm을 상속 받아서 쓰는 애들인데 각각 meta아래 필드 구성, 표시하는 모델에 따라 달라진다 
+ user 변경 vs. 게시글 변경
  + 차이점? 유저 정보를 변경하려면 pw 필요 
  + 일반 정보 변경창과 pw 변경창은 보통 나눠져있다. 
  + Django has UserChangeForm and SetPasswordForm
    + UserChangeForm 
      + ModelForm
    + SetPasswordForm
      + forms.Form
+ 왜 get_user_model()을 써요?
  + User model이라는게 결국에는 변경이 가능한 객체?뭐시기이면서 Django + 사용자가 같이 쓰는 것
  + 결국에는 변경 가능한 것은 어찌됐든지 변수화 등을 통해서 얘를 호출해서 쓰는 것이 가장 좋다 
    + Like url  'accounts:index' url에 name을 붙이고 함수로 해석해서 쓰자 
  + 유저 모델 클래스는 어딘가에 있긴하겠지만, 이걸 get_user_model()로 호출해서 쓰자 
  + 그ㄹㅓ면 auth_user_model에 정의된 클래스를 준다 



## 로그인 

### http 특징

+ 비 연결 지향 
  + 서버는 요청에 대한 응답을 보낸 후 연결을 끊는다
+ 무상태
  + 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음 
  + 클라이언트와 서버가 주고 받는 메세지들은 서로 완전히 독립적



### Cookie

+ 서버가 사용자의 웹 브라우저(클라이언트)에 전송하는 작은 데이터 조각 

+ 사용자가 웹 사이트를 방문할 경우 해당 웹사이트의 서버를 통해 사용자의 컴터에 설치되는 작은 기록 정보 파일 

  + 로컬에 key-value의 데이터 형식으로 저장

+ 서로 다른 요청이 동일한 브라우저로부터 발생한 것인지 판달할 때 주로 사용됨 

  + 로그인 상태같은거 유지되는 원리 

  

### Session

+ 사이트와 특정 브라우저 사이의 state상태를 유지시키는 것 
+ 클라이언트가 서버에 접속하면 서버가 특정 sessiona id를 발급하고, 클라이언트는 session id를 쿠키에 저장 
+ session id는 세션을 구별하기 위해 필요. 쿠키에는 session id만 저장 



### session in Django

+ Data-backend data 저장 방식이 default

+ 'django.contrib.sessions' 세션 관리



#### middleware? 

+ 요청은 위에서 아래로 처리 
+ 응답은 아래에서 위로 



### 로그인 기능 구현 

1. url: get/accounts/login
2. form
3. Url: post/accounts/login
4. 로그인 로직 처리 사용자 인지 확인하고  django_session 테이블에 저장 
5. 게시글 목록 페이지로 redirect



#### views.py

```python

```



### Authentication Form

+ 로그인을 위한 built in form
  + 로그인을 위한 폼을 받음 
  + 검증
  + 게시글이랑 비슷한데 그 후의 로직이 좀 달라짐 



### `login()`

+ `Login(request, user, backend=None)`
+ 인증된 사용자를 로그인 
  + 유저id를 세션에 저장하여 세션을 기록 
+ Httprequest 객체와 user 객체가 필요 
  + `authentication()`를 활용한 인증 
  + AuthenticationForm을 활용한 is.valid? 못봣어 
  + `authenticate()`함수로 개별로 설정할수도 있다고함.. 검색해보기 



### 로그인 로직 작성 

+ 일반적인 modelform 기반의 create 로직과 동일 

  + But modelform이 아닌 form으로 필수 인자 구성이 초큼 다르다 
  + db에 저장하는 것 대신 세션에 유저를 기록하는 함수를 호출한다

  ```python
  from django.contrib.auth import login as auth_login
  
  def login(request):
    if requset.method == 'POST':
      
  ```

### `gut_user()`

+ 유효성 검사를 통과한 유저 정보를 돌려줌 



### 세션 데이터 확인하기 

```python
def create(request):
  if request.user.is_authenticated:
    if request.method == "POST":
      article_form 생략 
    
    
  # 로그인 안돼있으면 어케?  
  else: 
    return redirect("accounts:login")
```



🤔 **뭐가 다를까 ? **

1. 8000/accounts./login/ 
   + 걍 로그인하고 Login이랑 연결된 html로 연결됨

2. 8000/accounts/login/?next=/articles/1/update/

   + 로그인하고 redirect에서 articles:update로 보내주세요.
   + 어케 만드냐 

   ```python
   def login(request):
     if request.method == 'POST':
       form
       if form.is_valid():
         auth_login(request, form.get_user())
         redirect(request.GET.get('next')) or 
   ```

   

@login_required

??????????? 

??????????????

1. There is no button but users can access specific pages by using url

   + Then, how can we forbid those access? 

     : we can write the code about it in views.py 

2. we can code by ourselves whether user is authenticated or not
   + Use decorator @login_required
   + its role is to send users to url
3. Then users encounter login html form, fill out the form and will go create.html
4. Function to help login exists, then there might be the function to help logout?  
   + yes there is. `from django.contrib.auth import logout as `
5. help... 🥲

