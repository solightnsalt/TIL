# Django

## How to manage ImageField in Models

### 설정 과정 

1. It Requires Pillow Library ( =Python Imageing Library), so install pillow using `pip install`

2. Set the FIeld and migrate

   `Image = models.ImageField(upload_to='images/', blank=True)`


3. Add Image to `filters=("image",)` `forms.py`
   + 여기까지 했을 때 html input o, imagefield o
   + 근데 왜 DB에 반영 안됨? 

4. HTMLFormElement를 같이 받아와야한다. 

   `<form action="" method="POST" enctype="multipart/form-data></form>"`

   + 이렇게까지 하고 Request Impormation을 보면 File 항목 받아온 것을 확인 할 수 있다. 

5. Static/images/에 첨부된 이미지가 저장된다. 

> Post = Review.objects.all()
>
> Post.

6. set Media_url, media_root in settings.pt

   ```python
   MEDIA_ROOt = BASE_DIR / "images"
   MEDIA_URL = ""
   ```

7. urls.py에 사진 경로를 추가
   ```python
      Urlpatters = 
   ```

      > HTML Form (enctype)
      >
      > View (request.FILES)

8. form에서 파일을 받아올 수 있게 View.py 코드를 수정

   ```python
   form = ReviewForm(request.POST, repost.Files)
   ```


> https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.ImageField





### 추가적으로 설정할 것들 

1. 파일 크기, 사진 사이즈 고려하기

2. 원본 그대로 저장? 아니면 조절해서 저장? 

   ```python
   image = ProcessedImageField(processors=[ResizeToFill(100, 50)], 
                               format='JPEG', 
                               options={'quality': 60})
   ```

   + https://django-imagekit.readthedocs.io/en/latest/

3. 첨부파일이 없는 경우가 있기 때문에 아래 구문 템플릿에 넣어줘야 오류 발생하지 않음

   ```django
   {% if article.image %}
   <img src="{{ article.img.url }}">
   {% endif %}
   ```

4. 장고 캡짱이라 수정하기 알아서 이미지 바꿀 수 있게 해준다. 단 하나 설정할 거 있음 

   ```python
   # views.py 
   def edit(request, post_pk)
   (request.POST, request.File)
   ```

   + 수정 템플릿에서도 폼에서 파일 받아올 수 있도록 수정해줘야한다. 

5. 이미지 여러개 받고 첨부받고싶으면?
   1.  이미지 테이블을 따로 만들어서 1:n관계를 만들어준다. 
   2. 모델폼에 이미지 여러개 선택할 수 있도록 변경 
   3. 알아서 해보기... 



From django.contrib import message

Get_messages(request)

in templates

{%.messages %}