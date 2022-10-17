# Django Auth

## User CRUD

+ 인증(비밀번호)
  + 별도의 절차가 필요하다
    + 비밀번호 > 암호화
  + 로그인과 연결됨 

## Auth

'django.contrib.auth'가 제공해줌	

+ class AbstractUser 상속 받아서 활용 

+ Form

  + ModelForm - UserCreationForm

    + DB영향 - 저장, 수정

      (ex. 비번 2개 체크, 저장)

  + Form - AuthenticationForm

    (ex. 인증 여부, 인증완료시 user ..?)

+ views 함수 

  + decorator '@login_required'



## session? cookie? 

https://www.daleseo.com/http-session/

+ http protocol = connectionless & stateless
  + 서버가 클라이언트의 요청에 응답을 하는 순간 연결 끊어짐
  + 클라이언트에서 새로운 요청을 해야 다시 연결이 맺어진다.
  
+ 클라이언트와 연결이 유지되지 않는 상황에서 동시에 서버로 유입되는 수많은 요청이 각각 어느 사용자의 것인지 서버가 어케 판단 ? 

  + 하나의 브라우저로부터 순차적으로 들어오는 여러 개의 요청 = 동일한 사용자로 부터 오는 것

  + 각각의 요청이 독립적으로 취급되어 여러 페이지에 걸쳐 흐름이 이어져야하는 서비스 구현은 어케? 

    -> 그래서 필요한게 세션과 쿠키 = 클라이언트와 정부 유지를 하기 위해 사용하는 것


### session

+ 일정 시간동안 같은 사용자(브라우저)로부터 들어오는 일련의 요구 => 하나의 상태 => 서버에 저장

  + 일정 시간 = 방문자가 웹 브라우저를 통해 웹 서버에 접속한 시점~웹 브라우저 종료해서 연결을 끝내는 시점

  => 어떤 방문자가 웹 서버에 접속해 있는 상태 = 하나의 단위 = 세션

### cookie

+ 서버상에서 생성돼서 로컬에 뿌려지는(저장되는) 것 

```
HTTP의 일종으로 사용자가 어떠한 웹 사이트를 방문할 경우,
그 사이트가 사용하고 있는 서버에서 사용자의 컴퓨터에 저장하는 작은 기록 정보 파일
```

+ 서버가 쿠키를 한 번 브라우저에 저장

  + 브라우저는 해당 쿠키를 매 요청마다 계속해서 서버로 돌려 보냄

    = 다시 말해 서버가 브라우저에 쿠키 하나만 심어 놓으면 그 후로 브라우저는 성실하게 매번 서버를 방문할 때 마다 해당 쿠키를 다시 가져온다

  이러한 쿠키의 특성을 활용하면 서버는 각 요청이 어느 브라우저에서 오는 것인지 어렵지 않게 판단할 수 있습니다.



## Dirs

+ django.contrib.auth => login, logou
+ django.contrib.auth.models => AbstractUser
+ django.contrib.auth.decorators => login_requir
+ ed
+ django.contrib.auth.forms => UserCreationForm

### `INSTALLED_APPS = []`

즉, 

+ articles.forms => ArticleForm
+ articles.views => ?
+ articles.models => Article



## 게시글 작성한 유저만 수정 삭제 ?

+ 게시글에 user pk를 저장 

```django
{% if request.user == article.user %}
 삭제, 수정 버튼 보여줄게 
 아니면 안보여줘 
{% endif %}
```

+ 다음주에 할 거임 



## 회원정보 수정 

### 1. urls.py

+ url > /accounts/\<int:pk>/update/

+ 근데 왜 ? 

  + 회원 정보 수정을 하는데 1번 유저,, 2번 유저,, 이렇게 불러와야할 필요가?

  + 그냥 로그인한 유저의 아이디값을 받아서 수정하면?

    = url > /accounts/update/로그인한 사용자 

+ `path("update/", views.update, name="update"),`


### 2. views.py
  ```python
  def update(request):
      if request.methods == "POST":
          form = CustomUserChangeForm(request.POST, instance=re	uest.user)
          if form.is_valid():
              form.save()
              return redirect("accounts:detail". )
      else:
          form = CustomUserChanger(request, instance=request.user)
          
      context = {
          "form": form,
      }
    return render(request, "accounts/update.html", context)
  ```

  

### 3. models.py

```python
from ~~~forms import 회원가입폼, UserChangeForm

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        
```





